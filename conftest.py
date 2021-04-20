import random
import pytest
from algs import models


@pytest.fixture
def correct_powers():
    correct_powers = list()
    i = 0
    while i < 1000:
        correct_powers.append(models.CorrectPower(random.randint(10, 100), random.randint(10, 100)))
        i += 1
    return correct_powers


@pytest.fixture
def my_lists():
    result = list()
    i = 0
    while i < 100:
        temp = list()
        x = 0
        while x < 50:
            temp.append(random.randint(0, 1000))
            x+= 1
        result.append(temp)
        i += 1
    return result

