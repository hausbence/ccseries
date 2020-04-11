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


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        title = request.form['title']
        results = queries.get_shows_by_title(title)
        return render_template('search.html', results = results)
    return render_template('search.html')


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
