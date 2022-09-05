from typing import List
from booking import constants


def check_args(count: int, age: List[int]) -> bool:
    if len(age) == count:
        return True
    raise ValueError("The age list must have lenght as count")

def check_age(ages: List[int]) -> bool:
    max = 0

    for age in ages:
        if age > max:
            max = age

    if max <= constants.MAX_CHILD_AGE:
        return True

    if max > constants.MAX_CHILD_AGE:
        raise ValueError("The maximum age of a child is %s" % constants.MAX_CHILD_AGE)

