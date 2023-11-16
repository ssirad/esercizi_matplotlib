# Classroom

# A: y = 0.5x+1000
# B: y = 0.9x+500
import matplotlib.pyplot as plt


def det(r, s, t, w):
    d = r*w - s*t
    return d


def cramer(a1, b1, c1, a2, b2, c2):
    d = det(a1, b1, a2, b2)
    if d == 0:
        print('sistema indeterminato o impossibile')
    else:
        dx = det(c1, b1, c2, b2)
        dy = det(a1, c1, a2, c2)
        x = dx/d
        y = dy/d
        return x, y


def crea(m, q, xi, xf):
    x = list()
    y = list()
    for i in range(xi, xf+1):
        x.append(i)
        y.append(m*i+q)
    return x, y


def grafico(x_a, y_a, x_b, y_b, px, py):
    plt.title('A in confronto a B')
    plt.plot(x_a, y_a, label='A', color='blue')
    plt.plot(x_b, y_b, label='B', color='green')
    plt.xlabel('x: merce (quintali)')
    plt.ylabel('y: costo (euro)')
    plt.plot(px, py, color='red', marker='*')
    plt.grid()
    plt.legend()
    plt.show()


def main():
    m_a = 0.5
    q_a = 1000
    m_b = 0.9
    q_b = 500
    xi = 200
    xf = 400
    x_a, y_a = crea(m_a, q_a, xi, xf)
    x_b, y_b = crea(m_b, q_b, xi, xf)
    px, py = cramer(-m_a, 1, q_a, -m_b, 1, q_b)
    grafico(x_a, y_a, x_b, y_b, px, py)


main()
