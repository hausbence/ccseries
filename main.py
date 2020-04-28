import json

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


@app.route('/genres/<genre_id>')
def list_shows(genre_id):
    shows = queries.get_shows_by_genreID(genre_id)
    return json.dumps(shows)


@app.route('/genres', methods=['GET', 'POST'])
def genres():
    genres = queries.get_genres()
    return render_template('genres.html', genres = genres)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
