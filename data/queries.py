from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_shows_by_letter(letter):
    letter = letter + "%"
    return data_manager.execute_select('''
        SELECT shows.title, COUNT(seasons.season_number) as num_of_seasons
        FROM shows
        INNER JOIN seasons ON shows.id = seasons.show_id
        WHERE shows.title ILIKE %(letter)s
        GROUP BY shows.id
    ''', {'letter' : letter})