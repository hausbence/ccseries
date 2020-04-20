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


@app.route('/genres', methods=['GET', 'POST'])
def show_by_genres():
    if request.method == 'POST':
        genre = request.form['genre']
        shows = queries.get_rated_shows(genre)
        return render_template('genres.html',shows = shows, genre=genre)
    return render_template('genres.html')


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
