import numpy as np


def gravity_calculated(data):
    global dataset

    G = 6.67e-11
    data_g = []

    if data[0] == "The Sphere":
        p = data[1]
        r = data[2]
        do = data[3]
        zo = data[4]
        xo = data[5]
        xt = data[6]
        delta_x = data[7]

        data_x = tuple(np.arange(xo, xt + delta_x, delta_x))

        for i in range(len(data_x)):
            V = 4 / 3 * np.pi * r ** 3
            g = (G * p * V * zo) / (((do - data_x[i]) ** 2 + zo ** 2) ** 3 / 2)
            data_g.append(g)

        data_g = np.array(data_g)

        dataset = [data_x, data_g]

    elif data[0] == "The Horizontal Cylinder":
        p = data[1]
        r = data[2]
        do = data[3]
        zo = data[4]
        xo = data[5]
        xt = data[6]
        delta_x = data[7]
        total = 1

        data_x = tuple(np.arange(xo, xt + delta_x, delta_x))

        for i in range(total):
            g = 0
            for j in range(len(data_x)):
                V = 2 * np.pi * r ** 2
                g = (G * p * V * zo) / ((do - data_x[j]) ** 2 + zo ** 2)
                data_g.append(g)

        data_g = np.array(data_g)

        dataset = [data_x, data_g]

    elif data[0] == "The Dipping Thin Sheet with Finite Length":
        p = data[1]
        t = data[2]
        l = data[3]
        do = data[4]
        zo = data[5]
        xo = data[6]
        xt = data[7]
        delta_x = data[8]
        a = data[9]

        data_x = tuple(np.arange(xo, xt + delta_x, delta_x))

        for j in range(len(data_x)):
            V = 2 * np.pi * a ** 2
            g = (G * p * V * zo) / ((do - data_x[j]) ** 2 + zo ** 2)
            data_g.append(g)

        data_g = np.array(data_g)

        dataset = [data_x, data_g]

    elif data[0] == "The Semi-Infinite Horizontal Sheet":
        p = data[1]
        t = data[2]
        l = data[3]
        do = data[4]
        zo = data[5]
        xo = data[6]
        xt = data[7]
        delta_x = data[8]

        data_x = tuple(np.arange(xo, xt + delta_x, delta_x))
        data_l = tuple(np.arange(do, do + l + delta_x, delta_x))

        for i in range(len(data_x)):
            g = 0

            for j in range(len(data_l)):
                g += 2 * G * p * t * (np.pi - np.arctan(abs(data_l[j] - data_x[i]) / zo))

            data_g.append(g)

        data_g = np.array(data_g)

        dataset = [data_x, data_g]

    return dataset
