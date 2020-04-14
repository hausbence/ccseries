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


@app.route('/actors', methods=['GET', 'POST'])
def get_actors():
    if request.method == "POST":
        year = request.form['release']
        age_of_show = int(2020) - int(year)
        actors = queries.get_actors(year)
        return render_template('actors.html', actors = actors, year = year, age_of_show = age_of_show)
    return render_template('actors.html')

def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
