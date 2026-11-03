import matplotlib.pyplot as plt

x = [i / 10 for i in range(-50, 51)]

plt.plot(x, [3 * v - 2 for v in x], label="y = 3x - 2")
plt.plot(x, [-v + 4 for v in x], label="y = -x + 4")
plt.legend()
plt.grid()
plt.title("Графіки функцій")
plt.show()