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


@app.route('/longest')
def top_longest():
    shows = queries.get_longest_show()
    list_of_dict = json.loads(json.dumps(shows))
    ids = tuple([x['id'] for x in list_of_dict])
    actors = queries.get_longest_show_actors(ids)
    print(actors)
    return render_template('longest.html', shows = shows, actors = actors)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
