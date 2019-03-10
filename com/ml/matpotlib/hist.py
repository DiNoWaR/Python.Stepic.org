from matplotlib import pyplot as plt

x = [item for item in range(0, 100)]
y = [item * item for item in range(0, 101)]

plt.hist(y)

plt.show()
