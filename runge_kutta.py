def solution(m, p, k, y_0, dy_0, h, number_of_steps):
    y = y_0
    dy = dy_0

    step_value_y = []
    step_value_dy = []

    for i in range(number_of_steps):
        step_value_y.append(y)
        step_value_dy.append(dy)

        k1 = h * dy
        l1 = h * second_derivate(m, p, k, y, dy)

        k2 = h * (dy + 1 / 2 * l1)
        l2 = h * second_derivate(m, p, k, y + 1 / 2 * k1, dy + 1 / 2 * l1)

        k3 = h * (dy + 1 / 2 * l2)
        l3 = h * second_derivate(m, p, k, y + 1 / 2 * k2, dy + 1 / 2 * l2)

        k4 = h * (dy + l3)
        l4 = h * second_derivate(m, p, k, y + k3, dy + l3)

        dy += (l1 + 2 * l2 + 2 * l3 + l4) / 6
        y += (k1 + 2 * k2 + 2 * k3 + k4) / 6

    step_value_y.append(y)
    step_value_dy.append(dy)

    return step_value_y, step_value_dy

def second_derivate(m, p, k, y, dy):
    return -(p * dy + k * y) / m

def print_solution(step_value_y, step_value_dy):
    print("start values: y = {y}, dy = {dy}".format(y=step_value_y[0], dy=step_value_dy[0]))

    for i in range(1, len(step_value_dy)):
        print("step {i} values: y = {y}, dy = {dy}".format(i=i, y=step_value_y[i], dy=step_value_dy[i]))
