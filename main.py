from flask import Flask, render_template, request
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np
import io
import base64
import pandas as pd
from objects import *

app = Flask(__name__)

@app.route('/')
def starting_page():
    return render_template("index.html")

@app.route('/chart')
def charts():
    img = io.BytesIO()
    x = np.linspace(1, 10)
    y = np.linspace(60, 70)
    plt.plot(x, y, color='blue')
    plt.savefig(img, format='png')
    img.seek(0)

    plot_url = base64.b64encode(img.getvalue()).decode()

    return '<img src="data:image/png;base64,{}">'.format(plot_url)

@app.route('/pie')
def pie_charts():
    img = io.BytesIO()
    x = np.linspace(1, 10)
    plt.pie(x)
    plt.savefig(img, format='png')
    img.seek(0)

    plot_url = base64.b64encode(img.getvalue()).decode()

    return '<img src="data:image/png;base64,{}">'.format(plot_url)

@app.route('/column')
def column_charts():
    img = io.BytesIO()

    x = np.arange(4)
    money = [1.5e5, 2.5e6, 5.5e6, 2.0e7]

    def millions(x, pos):
        'The two args are the value and tick position'
        return '$%1.1fM' % (x * 1e-6)

    formatter = FuncFormatter(millions)
    fig, ax = plt.subplots()
    ax.yaxis.set_major_formatter(formatter)
    plt.bar(x, money)
    plt.xticks(x, ('Bill', 'Fred', 'Mary', 'Sue'))
    plt.savefig(img, format='png')
    img.seek(0)

    plot_url = base64.b64encode(img.getvalue()).decode()

    return '<img src="data:image/png;base64,{}">'.format(plot_url)

@app.route('/csv')
def csv_table():
    return "Tutaj możesz wygenerować tabelę csv!"

if __name__ == "__main__":
    app.run(debug=True)
