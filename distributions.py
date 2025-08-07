print("DISTRIBUTIONS")
print("")

"""
NumPy is a Python library used for working with arrays.
It also has functions for working in domain of linear algebra, fourier transform, and matrices.

In Python we have lists that serve the purpose of arrays, but they are slow to process.
NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.
The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.
Arrays are very frequently used in data science, where speed and resources are very important.
"""

import numpy as np
from numpy import random

x = random.randint(100) #Integer
print(x)
x = random.rand() #Float
print(x)
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100)) # Array of 3, 5, 7, 9. P equals to posibilites of number appearing
print(x)
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5)) # Size of 3 rows with 5 items
print(x)

arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr) # Random shuffle of the original array
print(arr)

arr = np.array([1, 2, 3, 4, 5])
print(random.permutation(arr)) # Create a new array with random order

# Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot([0, 1, 2, 3, 4, 5])
plt.show()
sns.displot([0, 1, 2, 3, 4, 5], kind="kde")
plt.show()

# Gaussian distribution (normal)
"""
loc - (Mean) where the peak of the bell exists.
scale - (Standard Deviation) how flat the graph distribution should be.
size - The shape of the returned array.
"""
x = random.normal(size=(2, 3))
print(x)
sns.displot(random.normal(size=1000), kind="kde")
plt.show()

x = random.normal(loc=1, scale=2, size=(2, 3))
print(x)
# sns.displot(x, kind="kde")
# plt.show()

# Binomial distribution (Eg,. Tossing a coin)
"""
n - number of trials.
p - probability of occurence of each trial (e.g. for toss of a coin 0.5 each).
size - The shape of the returned array.
"""
x = random.binomial(n=10, p=0.5, size=10)
print(x)
sns.displot(x)
plt.show()

"""
The main difference is that normal distribution is continous whereas binomial is discrete, but if there are enough data points it will be quite similar to normal distribution with certain loc and scale.
"""

data = {
  "normal": random.normal(loc=50, scale=5, size=1000),
  "binomial": random.binomial(n=100, p=0.5, size=1000)
}

sns.displot(data, kind="kde")
plt.show()

# Poisson Distribution
"""
It estimates how many times an event can happen in a specified time. e.g. If someone eats twice a day what is the probability he will eat thrice?

lam - rate or known number of occurrences e.g. 2 for above problem.
size - The shape of the returned array.
"""
x = random.poisson(lam=2, size=1000)
sns.displot(x)
plt.show()

data = {
  "normal": random.normal(loc=50, scale=7, size=1000),
  "poisson": random.poisson(lam=50, size=1000)
}

sns.displot(data, kind="kde")
plt.show()

# Uniform Distribution - Used to describe probability where every event has equal chances of occuring (E.g. Generation of random numbers).
"""
low - lower bound - default 0 .0.
high - upper bound - default 1.0.
size - The shape of the returned array.
"""

sns.displot(random.uniform(size=1000), kind="kde")
plt.show()

# Logistic Distribution - Is used to describe growth. Used extensively in machine learning in logistic regression, neural networks etc.
"""
loc - mean, where the peak is. Default 0.
scale - standard deviation, the flatness of distribution. Default 1.
size - The shape of the returned array.
"""
x = random.logistic(loc=1, scale=2, size=(2, 3))
print(x)
sns.displot(x, kind="kde")
plt.show()

data = {
  "normal": random.normal(scale=2, size=1000),
  "logistic": random.logistic(size=1000)
}
sns.displot(data, kind="kde")
plt.show()

# Multinomial Distribution - Is a generalization of binomial distribution. It describes outcomes of multi-nomial scenarios unlike binomial where scenarios must be only one of two. e.g. Blood type of a population, dice roll outcome.
"""
n - number of times to run the experiment.
pvals - list of probabilties of outcomes (e.g. [1/6, 1/6, 1/6, 1/6, 1/6, 1/6] for dice roll).
size - The shape of the returned array.
"""
x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
sns.displot(x)
plt.show()
print(x)

# Exponential Distribution - Exponential distribution is used for describing time till next event e.g. failure/success etc.
"""
scale - inverse of rate ( see lam in poisson distribution ) defaults to 1.0.
size - The shape of the returned array.
"""
x = random.exponential(scale=2, size=(2, 3))
print(x)
sns.displot(x, kind="kde")
plt.show()

# Chi Square Distribution - Chi Square distribution is used as a basis to verify the hypothesis.
"""
df - (degree of freedom).
size - The shape of the returned array.
"""
x = random.chisquare(df=2, size=(2, 3))
print(x)
sns.displot(x, kind="kde")
plt.show()

# Rayleigh Distribution - Rayleigh distribution is used in signal processing.
"""
scale - (standard deviation) decides how flat the distribution will be default 1.0).
size - The shape of the returned array.
"""
x = random.rayleigh(scale=100, size=(2, 3))
print(x)
sns.displot(x, kind="kde")
plt.show()

# Pareto Distribution - A distribution following Pareto's law i.e. 80-20 distribution (20% factors cause 80% outcome).
"""
a - shape parameter.
size - The shape of the returned array.
"""
x = random.pareto(a=2, size=1000)
print(x)
sns.displot(x)
plt.show()

# Zipf Distribution - Zipf's Law: In a collection, the nth common term is 1/n times of the most common term. E.g. the 5th most common word in English occurs nearly 1/5 times as often as the most common word.
"""
a - distribution parameter.
size - The shape of the returned array.
"""
x = random.zipf(a=2, size=1000) # Sample 1000 points but plotting only ones with value < 10 for more meaningful chart.
sns.displot(x[x<10])
plt.show()