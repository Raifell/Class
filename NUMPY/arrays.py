import numpy as np

a = np.zeros(10, 'int')
print(a)
a = np.arange(0, 10, 2)
print(a)
a = np.arange(12, 0, -3)
print(a)
a = [x*x for x in np.arange(0, 10)]
print(a)
a = np.arange(0, 10)
b = [np.arange(0, 10)[i] for i in range(len(np.arange(0, 10))) if i % 2 == 0]
print(b)
print(sum(b))