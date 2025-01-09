from flask import Flask, render_template, request

from functions import ACTIONS


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':

        a = float(request.form.get('a'))
        b = float(request.form.get('b'))

        action = request.form.get('action')

        result = ACTIONS[action](a, b)

    else:
        result = None

    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
