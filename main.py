import json

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


@app.route('/search/<charname>')
def search(charname):
    shows = queries.fuzzy(charname)
    return json.dumps(shows)


@app.route('/search', methods=['GET', 'POST'])
def fuzzy():
    return render_template('fuzzy.html')


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
