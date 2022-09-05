from utils import actions
import pytest

def test_check_args():
    first_scenario = actions.check_args(2, [1, 3])
    assert first_scenario == True

    with pytest.raises(ValueError):
        actions.check_args(3, [1, 2])
    


def test_check_age():
    with pytest.raises(ValueError):
        actions.check_age([17, 18, 15, 21])
