import runge_kutta
from scipy.integrate import odeint
import plotly.graph_objects as go
import numpy as np

m = float(input("m: "))
p = float(input("p: "))
k = float(input("k: "))
y_0 = float(input("y_0: "))
dy_0 = float(input("dy_0: "))
h = float(input("h: "))
number_of_steps = int(input("number of steps: "))

custom_result = runge_kutta.solution(m, p, k, y_0, dy_0, h, number_of_steps)
runge_kutta.print_solution(custom_result[0], custom_result[1])

time_values = np.linspace(0, h * number_of_steps, number_of_steps)
scipy_solution = odeint(
    lambda y, x: [y[1], -(p * y[1] + k * y[0]) / m], [y_0, dy_0],
    time_values
)

fig = go.Figure()
fig.add_trace(go.Scatter(x=time_values, y=custom_result[0], name="Собственная реализация Runge Kutta"))
fig.add_trace(go.Scatter(x=time_values, y=scipy_solution[:, 0], name="SciPy odeint решение"))
fig.update_layout(title="График сравнение решений y", xaxis_title="Время", yaxis_title="Значение y")
fig.show()

fig = go.Figure()
fig.add_trace(go.Scatter(x=time_values, y=custom_result[1], name="Собственная реализация Runge Kutta"))
fig.add_trace(go.Scatter(x=time_values, y=scipy_solution[:, 1], name="SciPy odeint"))
fig.update_layout(title="График сравнение решений dy", xaxis_title="Время", yaxis_title="Значение dy")
fig.show()

fig = go.Figure()
fig.add_trace(go.Scatter(x=time_values, y=custom_result[0], name="Собственная реализация Runge Kutta"))
fig.add_trace(go.Scatter(x=time_values, y=scipy_solution[:, 0], name="SciPy odeint"))
fig.update_layout(title="График сравнение решений в диапазоне [0.008:0.01] - y",
                  xaxis_title="Время",
                  yaxis_title="Значение y",
                  xaxis_range=[0.008, 0.01]
                  )
fig.show()

fig = go.Figure()
fig.add_trace(go.Scatter(x=time_values, y=custom_result[1], name="Собственная реализация Runge Kutta"))
fig.add_trace(go.Scatter(x=time_values, y=scipy_solution[:, 1], name="SciPy odeint"))
fig.update_layout(title="График сравнение решений в диапазоне [0.008:0.01] - dy",
                  xaxis_title="Время",
                  yaxis_title="Значение dy",
                  xaxis_range=[0.008, 0.01]
                  )
fig.show()