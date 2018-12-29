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
    if request.method == 'POST':
        beginning_x = request.form['x1']
        ending_x = request.form['x2']
        beginning_y = request.form['y1']
        ending_y = request.form['y2']
        multiplier = request.form['Z']

        x = np.linspace(int(beginning_x), int(ending_x))
        y = np.linspace(int(beginning_y), int(ending_y))

        img = io.BytesIO()
        if request.form.get('czerwony'):
            curvecolor = 'red'
        elif request.form.get('zielony'):
            curvecolor = 'green'
        elif request.form.get('blue'):
            curvecolor = 'blue'
        else:
            curvecolor = 'black'

        line_plot = Charts(x, y ** int(multiplier), curvecolor)
        line_plot.line_chart()
        plt.savefig(img, format='png')
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode()

        return '<img src="data:image/png;base64,{}">'.format(plot_url)
    else:
        return render_template('linechart.html')

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
