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


@app.route('/genres/', methods=['GET', 'POST'])
def list_genres():
    all_genres = queries.get_all_genres()
    if request.method == "POST":
        shows = queries.get_shows_by_genre(genre_id)
        return render_template('genres.html', all_genres=all_genres, shows=shows)
    return render_template('genres.html', all_genres = all_genres)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
