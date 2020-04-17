from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_seasons(num_of_seasons):
    return data_manager.execute_select('''
        SELECT shows.title, COUNT(seasons.season_number) as Seasons
        FROM seasons
        INNER JOIN shows ON shows.id = seasons.show_id
        GROUP BY shows.id
        HAVING COUNT(seasons.season_number) <= %(num_of_seasons)s
        ORDER BY Seasons DESC;
    ''', {'num_of_seasons' : num_of_seasons})
