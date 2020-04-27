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


@app.route('/actors')
def get_actors():
    actor_names = queries.get_actors()
    list_of_dict = json.loads(json.dumps(actor_names))
    ids = tuple([x['id'] for x in list_of_dict])
    actors = queries.get_shows_by_actors(ids)
    return render_template('actors.html', actors = actors)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
