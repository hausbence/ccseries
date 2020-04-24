from flask import Flask, render_template, url_for
from data import queries

app = Flask('codecool_series')


@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


@app.route('/design')
def design():
    return render_template('design.html')


@app.route('/years')
def years():
    years = queries.get_years()
    return render_template('years.html', years=years)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
