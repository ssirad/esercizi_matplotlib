# Pag. 237 es. 409

# E: Se(t) = 50t
# F1: Sf(t) = 700           se 0<=t<=2
# F2: Sf(t) = -100t+900     se t>2
import matplotlib.pyplot as plt


def crea(m, q, xi, xf):
    x = list()
    y = list()
    for i in range(xi, xf+1):
        x.append(i)
        y.append(m*i+q)
    return x, y


def grafico(x_e, y_e, x_f1, y_f1, x_f2, y_f2):
    plt.title('E in confronto a F')
    plt.plot(x_e, y_e, label='E', color='blue')
    plt.plot(x_f1, y_f1, label='F1', color='green')
    plt.plot(x_f2, y_f2, label='F2', color='green')
    plt.xlabel('x: tempo (min)')
    plt.ylabel('y: spazio (m)')
    plt.grid()
    plt.legend()
    plt.show()


def main():
    m_e = 50
    q_e = 0
    xi_e = 0
    xf_e = 10
    m_f1 = 0
    q_f1 = 700
    xi_f1 = 0
    xf_f1 = 2
    m_f2 = -100
    q_f2 = 900
    xi_f2 = 2
    xf_f2 = 10
    x_e, y_e = crea(m_e, q_e, xi_e, xf_e)
    x_f1, y_f1 = crea(m_f1, q_f1, xi_f1, xf_f1)
    x_f2, y_f2 = crea(m_f2, q_f2, xi_f2, xf_f2)
    grafico(x_e, y_e, x_f1, y_f1, x_f2, y_f2)


main()
