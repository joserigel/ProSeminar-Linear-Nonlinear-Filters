import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math

mu = 0
variance = 1
sigma = math.sqrt(variance)
x = np.linspace(mu - 5*sigma, mu + 5*sigma, 100)
plt.plot(x, stats.norm.pdf(x, mu, sigma))
plt.plot(x, stats.norm.pdf(x, mu, sigma * 2))
plt.plot(x, stats.norm.pdf(x, mu, sigma * 3))
plt.legend(["sigma=1", "sigma=2", "sigma=3"])
plt.show()
plt.clf()
plt.plot([-2, -1, 0, 1, 2], [0, 0, 1, 0, 0])
plt.show()

plt.plot([-2, -1, -1, 0, 1, 1, 2], [0, 0, 0.5, 0.5, 0.5, 0, 0])
plt.show()