import matplotlib.pyplot as plt
import numpy as np

class Charts:
    def __init__(self, x, y, label):
        self.x = x
        self.y = y
        self.label = label

    def line_chart(self):
        return plt.plot(self.x, self.y, label=self.label)

    def pie_chart(self):
        return plt.pie(self.x, self.y)

    def column_chart(self):
        return plt.bar(self.x, self.y)


e = np.linspace(10, 100)
d = np.linspace(1, 1000)

p = Charts(e**2, d, label='test data')
p.line_chart()
plt.legend(loc='upper right', frameon=False)