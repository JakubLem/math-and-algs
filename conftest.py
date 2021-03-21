import pytest
import random
from algs import models

@pytest.fixture
def correct_powers():
    correct_powers = list()
    i = 0
    while i < 1000:
        correct_powers.append(models.CorrectPower(random.randint(10, 100), random.randint(10, 100)))
        i += 1
    return correct_powers
