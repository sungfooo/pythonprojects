import random
import matplotlib.pyplot as plt

max=100

array=[]
for i in range(0,max):
    array.append(random.randint(1,max))

print array
average = sum(array)/len(array)
average_array = [average] * max

print average_array

fig, ax = plt.subplots()

x = range(0,max)

ax.plot(x, array)
ax.plot(x, average_array)


plt.show()
