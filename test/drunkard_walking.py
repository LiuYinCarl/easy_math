import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation


path_num = 50
path_length = [1, 3]


def calc():
    r = np.random.randint(path_length[0], path_length[1], path_num)
    theta = np.radians(np.random.randint(0, 361, path_num))
    x = [0]
    y = [0]
    for i in range(path_num):
        x.append(x[-1] + r[i] * np.cos(theta[i]))
        y.append(y[-1] + r[i] * np.sin(theta[i]))
    return x, y


fig, ax = plt.subplots()
x, y = calc()
l = ax.plot(x, y)
dot, = ax.plot([], [], 'ro')


def init():
    # ax.set_xlim(-10, 10)
    # ax.set_ylim(-10, 10)
    return l


def gen_dot():
    for i in range(len(x)):
        newdot = [x[i], y[i]]
        yield newdot


def update_dot(newdot):
    dot.set_data(newdot[0], newdot[1])
    return dot



ani = animation.FuncAnimation(fig, update_dot, frames=gen_dot, interval=100, init_func=init)
plt.annotate(text='start:%.3f,%.3f' % (x[0], y[0]), xy=(x[0], y[0]))
plt.annotate(text='end:%.3f,%.3f' % (x[-1], y[-1]), xy=(x[-1], y[-1]))

# ani.save('random_walking_50.gif', writer='imagemagick', fps=30)
plt.show()

# Writer = animation.writers['ffmpeg']
# writer = Writer(fps=30, metadata=dict(artist='Me'), bitrate=3600)
# ani.save('lines.mp4', writer=writer)
