import matplotlib.pyplot as plt

x = [2, 4, 5]
x2 = [2, 7, 9]
y = [1, 4, 7]
y2 = [2, 4, 6]

# color, linestyle, linewidth, marker,markerfacecolor, markersize and a label can be added
plt.plot(x, y, color='green', linestyle='dashed', linewidth=2, marker='o', markerfacecolor='blue', markersize=12)
plt.plot(x2, y2, label='Line 2')

# to set thte limit of the graph
plt.xlim(1, 8)
plt.ylim(1, 8)

# to label the graph
plt.xlabel('X Axis')
plt.ylabel('y Axis')

plt.title("Demo Graph - Customisation")

# shows an indicator for each line
plt.legend()
plt.show()