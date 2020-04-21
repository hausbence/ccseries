from flask import Flask, render_template, url_for, request
from data import queries

app = Flask('codecool_series')


@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


@app.route('/design')
def design():
    return render_template('design.html')


@app.route('/fuzzy', methods=['GET', 'POST'])
def fuzzy():
    if request.method == "POST":
        charname = request.form['charname']
        datas = queries.fuzzy(charname)
        return render_template('fuzzy.html', datas = datas)
    return render_template('fuzzy.html')


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
