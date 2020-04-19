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


@app.route('/ranges', methods=['GET', 'POST'])
def range():
    ranges = queries.get_seasons()
    return render_template('ranges.html', ranges=ranges)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
