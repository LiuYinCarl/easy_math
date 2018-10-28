import matplotlib.pyplot as plt

# define figure
fig = plt.figure()

# define data
x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 3, 4, 2, 5, 8, 6]

left, bottom, width, height = 0.1, 0.1, 0.8, 0.8

ax1 = fig.add_axes([left, bottom, width, height])
ax1.plot(x, y, 'r')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('test')

# Method 1
left, bottom, width, height = 0.2, 0.6, 0.25, 0.25
ax2 = fig.add_axes([left, bottom, width, height])
ax2.plot(x, y, 'r')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('part1')

# Method 2
plt.axes([bottom, left, width, height])
plt.plot(x, y, 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.title('part2')

plt.show()