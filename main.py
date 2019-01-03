from flask import Flask, render_template, request
from matplotlib.ticker import FuncFormatter
import numpy as np
import io
import base64
from objects import *

app = Flask(__name__)

@app.route('/')
def starting_page():
    return render_template("index.html")

@app.route('/chart', methods=['GET', 'POST'])
def charts():
    plot_url = ''
    if request.method == 'POST':

        beginning_x = request.form.get('x1', '1')
        ending_x = request.form.get('x2', '50')
        beginning_y = request.form.get('y1', '1')
        ending_y = request.form.get('y2', '50')
        multiplier = request.form.get('Z', '1')
        color = request.form.get('color', 'pink')

        x = np.linspace(int(beginning_x), int(ending_x))
        y = np.linspace(int(beginning_y), int(ending_y))

        img = io.BytesIO()

        line_plot = Charts(x, y ** int(multiplier), color)
        line_plot.line_chart()
        plt.savefig(img, format='png')
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode()
        plt.close()   # if you not close then next chart will be merged with the previous ones
        # check: https://technovechno.com/creating-graphs-in-python-using-matplotlib-flask-framework-pythonanywhere/
    return render_template('linechart.html', image=plot_url)


@app.route('/pie', methods=['GET', 'POST'])
def pie_charts():
    pie_plot_url = ''
    if request.method == 'POST':
        group1 = request.form['g1']
        group2 = request.form['g2']
        group3 = request.form['g3']
        group4 = request.form['g4']
        value1 = request.form['v1']
        value2 = request.form['v2']
        value3 = request.form['v3']
        value4 = request.form['v4']
        pie_pie = io.BytesIO()
        pie_labels = [group1, group2, group3, group4]
        sizes = [int(value1), int(value2), int(value3), int(value4)]
        pie_plot = Charts(sizes, pie_labels)
        pie_plot.pie_chart()
        plt.savefig(pie_pie, format='png')
        pie_pie.seek(0)
        pie_plot_url = base64.b64encode(pie_pie.getvalue()).decode()
        plt.close()
    return render_template('piechart.html', image=pie_plot_url)

@app.route('/column')
def column_charts():
    img = io.BytesIO()

    x = np.arange(5)
    money = [1.5e5, 2.5e6, 5.5e6, 2.0e7, 3.0e6]

    def millions(x, pos):
        'The two args are the value and tick position'
        return '$%1.1fM' % (x * 1e-6)

    formatter = FuncFormatter(millions)
    fig, ax = plt.subplots()
    ax.yaxis.set_major_formatter(formatter)
    plt.bar(x, money)
    plt.xticks(x, ('Bill', 'Fred', 'Mary', 'Sue', 'John'))
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return render_template('columnchart.html', image=plot_url)

@app.route('/csv')
def csv_table():
    return render_template('csv.html', csv="Tutaj możesz wygenerować tabelę csv!")

if __name__ == "__main__":
    app.run(debug=True)

# other ways to create graphs:
# https://blog.ruanbekker.com/blog/2017/12/14/graphing-pretty-charts-with-python-flask-and-chartjs/
# https://technovechno.com/creating-graphs-in-python-using-matplotlib-flask-framework-pythonanywhere/
# google: flask graph

# Flask templates
# http://flask.pocoo.org/docs/1.0/tutorial/templates/
