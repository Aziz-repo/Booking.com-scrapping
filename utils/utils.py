from typing import List
import datetime


def check_format(dates: List[str]) -> bool:
    for date in dates:
        try:
            datetime.datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Incorrect date format, Must be YYYY-MM-DD")
    return True


def month_difference(check_in_date: str, check_out_date: str) -> int:
    if check_format([check_in_date, check_out_date]):   

        # Converting the string to date
        check_in = datetime.datetime.strptime(check_in_date, "%Y-%m-%d")
        check_out = datetime.datetime.strptime(check_out_date, "%Y-%m-%d")

        # calculating the difference in months
        difference = (check_out.year - check_in.year) * 12 + (
            check_out.month - check_in.month
        )

        return difference
