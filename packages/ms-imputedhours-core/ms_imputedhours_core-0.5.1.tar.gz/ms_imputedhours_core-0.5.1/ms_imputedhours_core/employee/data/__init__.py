import datetime

from ms_imputedhours_core.agreements import Agreements
from ms_imputedhours_core.employee import calculate_real_capacity, get_real_fte
from ms_imputedhours_core.employee.data.bigquery import (
    get_all_data,
    get_all_data_by_dates,
    get_all_employee_capacity,
    get_imputed_hours,
    get_out_date_imputations,
    get_successfactor_all_data,
)
from ms_imputedhours_core.employee.data.helpers.alert import (
    should_exclude_employee,
)
from ms_imputedhours_core.employee.data.helpers.dates import (
    get_first_day,
    get_last_day,
)
from ms_imputedhours_core.employee.data.transformers.hours import (
    group_task_by_email,
    group_task_by_outdated,
    transform_all_capacities,
    transform_successfactor_all_data,
)
from ms_imputedhours_core.office import get_real_office_name

AGREEMENTS_SPREADSHEET_ID = '1gMQ30Sl0QHhocTQgbYpWvS6DarhcRIeBIANW8FYLTTQ'
AWAIT_FOR_GOOLE_API_BACK_PRESSURE = 5
EMPTY_SUCCESSFACTOR_DATA = {
    'office_name': '',
    'FTE': 0,
    'hiring_date': None,
    'enddate': None,
}
EMPTY_AGREEMENT_HOURS_DATA = {'totalHours': 0.0, 'days': {}}
EMPTY_EMPLOYEE_DATA = {
    'data': {},
    'yearSelected': 0,
    'monthSelected': 0,
    'agreementHours': 0,
    'successfactor_data': EMPTY_SUCCESSFACTOR_DATA,
}
GOOGLE_API_MAX_REQUESTS_PER_SEG = 60


def get_all_employees_monthly_data_by_office(date, office_name):
    data = {}
    first_date = get_first_day(date)
    last_day = get_last_day(date)
    agreement_hours = Agreements(AGREEMENTS_SPREADSHEET_ID).get_hours_by_range(
        first_date, last_day, office_name
    )
    successfactor_all_data = transform_successfactor_all_data(
        get_successfactor_all_data(office_name, only_actives=False)
    )
    if successfactor_all_data:
        office_emails = successfactor_all_data.keys()
        current_month_data = group_task_by_email(
            get_all_data(date, office_emails)
        )
        all_employee_ftes = transform_all_capacities(
            get_all_employee_capacity(date.month, date.year)
        )

        for email in office_emails:
            successfactor_data = successfactor_all_data.get(
                email, EMPTY_SUCCESSFACTOR_DATA
            )

            if should_exclude_employee(
                email,
                date,
                successfactor_data['hiring_date'],
                successfactor_data['enddate'],
            ):
                continue

            office_name = get_real_office_name(
                successfactor_data.get('office_name')
            )

            fte = get_real_fte(
                successfactor_data, all_employee_ftes.get(email), date
            )

            real_capacity = calculate_real_capacity(
                agreement_hours,
                successfactor_data.get('hiring_date'),
                successfactor_data.get('enddate'),
                first_date,
                last_day,
                fte,
                True,
            )

            # Updating fte value
            successfactor_data['FTE'] = fte

            if email not in data.keys():
                data[email] = {
                    'data': {
                        'totalTimeSpent': current_month_data.get(
                            email, {}
                        ).get('totalHours', 0)
                    },
                    'agreementHours': {
                        'totalHours': agreement_hours.get('totalHours', 0),
                        'realcapacity': real_capacity,
                    },
                    'successfactor_data': successfactor_data,
                    'yearSelected': date.year,
                    'monthSelected': date.month,
                }

    return data


def get_all_employee_data_by_range(from_date, to_date, office_name):
    employees_data = {}
    agreement_hours = Agreements(AGREEMENTS_SPREADSHEET_ID).get_hours_by_range(
        from_date, to_date, office_name
    )
    successfactor_all_data = transform_successfactor_all_data(
        get_successfactor_all_data(office_name)
    )
    office_emails = successfactor_all_data.keys()
    current_month_data = group_task_by_email(
        get_all_data_by_dates(from_date, to_date, office_emails)
    )
    all_employee_ftes = transform_all_capacities(
        get_all_employee_capacity(from_date.month, from_date.year)
    )

    for email in office_emails:
        successfactor_data = successfactor_all_data.get(
            email, EMPTY_SUCCESSFACTOR_DATA
        )

        if should_exclude_employee(
            email,
            from_date,
            successfactor_data['hiring_date'],
            successfactor_data['enddate'],
        ):
            continue

        employee_fte = get_real_fte(
            successfactor_data, all_employee_ftes.get(email), from_date
        )
        employee_current_capacity = (
            current_month_data.get(email, EMPTY_AGREEMENT_HOURS_DATA)[
                'totalHours'
            ]
            / 3600
        )

        employee_real_capacity = calculate_real_capacity(
            agreement_hours,
            successfactor_data.get('hiring_date'),
            successfactor_data.get('enddate'),
            from_date,
            to_date,
            employee_fte,
            calculate_range=True,
        )

        capacity_percentage = 0
        if employee_real_capacity == 0:
            capacity_percentage = 100
        else:
            capacity_percentage = round(
                (employee_current_capacity * 100) / employee_real_capacity, 2
            )

        employees_data[email] = {
            'real_capacity': employee_real_capacity,
            'current_capacity': employee_current_capacity,
            'current_percentage_hours_imputed': capacity_percentage,
            'supervisor': successfactor_data['supervisor'],
            'name': successfactor_data['name'],
        }

    return employees_data


def get_all_imputations_per_day(from_date, to_date):
    current_month_data = group_task_by_email(
        get_imputed_hours(from_date, to_date)
    )

    return current_month_data


def get_all_out_date_imputations(first_day, last_day, office_name):
    successfactor_all_data = transform_successfactor_all_data(
        get_successfactor_all_data(office_name)
    )
    current_data = group_task_by_outdated(
        get_out_date_imputations(first_day, last_day)
    )
    employees_data = {}
    for email in successfactor_all_data.keys():
        successfactor_data = successfactor_all_data.get(
            email, EMPTY_SUCCESSFACTOR_DATA
        )

        if should_exclude_employee(
            email,
            first_day,
            successfactor_data['hiring_date'],
            successfactor_data['enddate'],
        ):
            continue

        if current_data.get(email):
            supervisor_email = successfactor_data['supervisor']
            if supervisor_email not in employees_data.keys():
                employees_data[supervisor_email] = {}

            employees_data[supervisor_email][email] = {
                'data': current_data[email],
                'name': successfactor_data['name'],
            }

    return employees_data


def get_all_employees_daily_data_by_office(date, office_name):
    data = {}
    first_date = get_first_day(date)
    last_day = get_last_day(date)
    agreement_hours = Agreements(AGREEMENTS_SPREADSHEET_ID).get_hours_by_range(
        first_date, last_day, office_name
    )
    successfactor_all_data = transform_successfactor_all_data(
        get_successfactor_all_data(office_name, only_actives=False)
    )
    if successfactor_all_data:
        office_emails = successfactor_all_data.keys()

        current_month_data = group_task_by_email(
            get_all_data(date, office_emails),
        )

        all_employee_ftes = transform_all_capacities(
            get_all_employee_capacity(date.month, date.year)
        )

        for email in office_emails:
            successfactor_data = successfactor_all_data.get(
                email, EMPTY_SUCCESSFACTOR_DATA
            )

            if should_exclude_employee(
                email,
                date,
                successfactor_data['hiring_date'],
                successfactor_data['enddate'],
            ):
                continue

            office_name = get_real_office_name(
                successfactor_data.get('office_name')
            )

            fte = get_real_fte(
                successfactor_data,
                all_employee_ftes.get(email),
                date,
            )

            # Updating fte value
            successfactor_data['FTE'] = fte

            employee_daily_data = current_month_data.get(email, {}).get(
                "days", {}
            )

            if email not in data.keys():
                data[email] = {
                    'data': employee_daily_data,
                    'agreementHours': {"days": {}},
                    'successfactor_data': successfactor_data,
                    'yearSelected': date.year,
                    'monthSelected': date.month,
                }

            # Calculating real capacity for each day of month
            current_day = first_date
            while current_day <= last_day:
                agreement_daily_hours = agreement_hours["days"]
                agreement_daily_key = f"{current_day.day}-{current_day.month}"
                agreement_daily_total_hours = float(
                    agreement_daily_hours.get(agreement_daily_key, 0)
                )

                real_daily_capacity = calculate_real_capacity(
                    agreement_hours,
                    successfactor_data.get('hiring_date'),
                    successfactor_data.get('enddate'),
                    current_day,
                    current_day,
                    fte,
                    True,
                )

                if (
                    current_day.day
                    not in data[email]["agreementHours"]["days"]
                ):
                    data[email]["agreementHours"]["days"][current_day.day] = {
                        "agreement": agreement_daily_total_hours,
                        "real_capacity": real_daily_capacity,
                    }

                # Increment the date
                current_day += datetime.timedelta(days=1)

    return data
