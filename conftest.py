import pytest
import random
from . import models

@pytest.fixture
def correct_powers():
    correct_powers = list()
    for i in range(10):
        correct_powers.append(models.CorrectPower(random.randint(10, 100), random.randint(10, 100)))
    return correct_powers
