from flask import Flask, render_template, request
from forms import ChartForm, PieColumnForm
import numpy as np
import io
import base64
import matplotlib.pyplot as plt

app = Flask(__name__)
app.config['SECRET_KEY'] = '828f0089fdb1b7d3433f7d9e1388f1c3'

@app.route('/', methods=['GET', 'POST'])
def home():
        return render_template('index.html')

@app.route('/line', methods=['GET', 'POST'])
def line():
    form = ChartForm()
    plot_url = ""
    if request.method == 'POST':
        x = np.linspace(form.start_x.data, form.end_x.data)
        func = (form.coeff_a.data * x ** 2) + (form.coeff_b.data * x) + form.coeff_c.data
        img = io.BytesIO()
        plt.title(f"Square function of {form.coeff_a.data} * x**2 + {form.coeff_b.data} * x + {form.coeff_c.data}")
        plt.plot(x, func, color=form.color.data, linewidth=0.5, label='data')
        plt.grid()
        plt.legend(loc='upper right', frameon=False)
        plt.xlabel('x data')
        plt.ylabel('y data')
        plt.savefig(img, format='png')
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode()
        plt.close()
    return render_template('line.html', image=plot_url, form=form)

@app.route('/pie', methods=['GET', 'POST'])
def pie():
    pie_form = PieColumnForm()
    pie_plot_url = ''
    if request.method == 'POST':
        pie_labels = []
        sizes = []

        if pie_form.submit.data:
            return render_template('pie.html', pie_form=pie_form)
        elif pie_form.draw.data:
            for i in range(pie_form.number_of_rows.data):
                group = request.form[f'g{i}']
                value = request.form[f'v{i}']
                pie_labels.append(group)
                sizes.append(int(value))
            if sum(sizes) > 100:
                message = 'More than 100%'
                return render_template('pie.html', pie_form=pie_form, message=message)
            elif sum(sizes) < 100:
                message = 'Less than 100%'
                return render_template('pie.html', pie_form=pie_form, message=message)
            else:
                img = io.BytesIO()
                plt.title("Pie chart for: ")
                plt.pie(sizes, labels=pie_labels, autopct='%1.1f%%', startangle=90, shadow=True)
                plt.savefig(img, format='png')
                img.seek(0)
                pie_plot_url = base64.b64encode(img.getvalue()).decode()
                plt.close()
                return render_template('pie.html', image=pie_plot_url, pie_form=pie_form)
    return render_template('pie.html', image=pie_plot_url, pie_form=pie_form)

@app.route('/column', methods=['GET', 'POST'])
def column():
    column_form = PieColumnForm()
    column_plot_url = ''
    if request.method == 'POST':
        column_labels = []
        values = []
        if column_form.submit.data:
            return render_template('column.html', column_form=column_form)
        elif column_form.draw.data:
            for i in range(column_form.number_of_rows.data):
                label = request.form[f'l{i}']
                value = request.form[f'v{i}']
                column_labels.append(label)
                values.append(int(value))
            img = io.BytesIO()
            plt.title("Column chart for: ")
            x = np.arange(column_form.number_of_rows.data)
            plt.bar(x, values)
            plt.xticks(x, tuple(column_labels))
            plt.xlabel('Labels')
            plt.ylabel('y data')
            plt.savefig(img, format='png')
            img.seek(0)
            column_plot_url = base64.b64encode(img.getvalue()).decode()
            plt.close()
            return render_template('column.html', image=column_plot_url, column_form=column_form)
    return render_template('column.html', image=column_plot_url, column_form=column_form)

if __name__ == "__main__":
    app.run(debug=True)
