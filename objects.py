import matplotlib.pyplot as plt

class Charts:
    def __init__(self, x, y, linecolor="red"):
        self.x = x
        self.y = y
        self.linecolor = linecolor

    def line_chart(self):
        return plt.plot(self.x, self.y, color=self.linecolor)

    def pie_chart(self):
        return plt.pie(self.x, labels=self.y)

    def column_chart(self):
        return plt.bar(self.x, self.y)
