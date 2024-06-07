import random
import pytest
from scipy.integrate import odeint
import runge_kutta
import numpy as np

def test_basic():
    for i in range(100):
        m = random.uniform(1, 10)
        p = random.uniform(1, 10)
        k = random.uniform(1, 10)
        y_0 = random.uniform(1, 10)
        dy_0 = random.uniform(1, 10)
        h = 0.00001
        number_of_steps = 1000

        result = runge_kutta.solution(m, p, k, y_0, dy_0, h, number_of_steps)

        scipy_solution = odeint(
                                lambda y, x: [y[1], -(p * y[1] + k * y[0]) / m], [y_0, dy_0],
                                np.linspace(0, h * number_of_steps, number_of_steps)
                                )[number_of_steps-1]
        assert pytest.approx(result[0][number_of_steps], 0.00000001) == scipy_solution[0]
        assert pytest.approx(result[1][number_of_steps], 0.00000001) == scipy_solution[1]
