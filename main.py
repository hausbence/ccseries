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
        table = request.form["table"]
        order = request.form["order"]
        print(order)
        if "shows" in table:
            datas = queries.get_all_shows(order)
        if "seasons" in table:
            datas = queries.get_all_seasons(order)
        if "episodes" in table:
            datas = queries.get_all_episodes(order)
        return render_template('search.html', datas = datas, table = table)
    return render_template('search.html')

    
def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
