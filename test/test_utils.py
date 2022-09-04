from utils import utils
import pytest


def test_check_format():
    result = utils.check_format(["2022-07-10"])
    assert result == True

    with pytest.raises(ValueError):
        utils.check_format(["2022/07/10"])




def test_month_difference():
    result = utils.month_difference("2022-07-10", "2022-09-10")
    assert result == 2
