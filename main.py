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


@app.route('/genres')
def genres():
    return render_template('genres.html')


@app.route('/shows/<letter>')
def list_shows(letter):
    shows = queries.get_shows_by_letter(letter)
    return render_template('shows.html', shows = shows)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
