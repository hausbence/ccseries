from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_rated_shows(genre):
    return data_manager.execute_select('''
        SELECT shows.title, shows.year,ROUND(shows.rating) as rating
        FROM shows
        INNER JOIN show_genres ON show_genres.show_id = shows.id
        INNER JOIN genres ON genres.id = show_genres.genre_id
        WHERE genres.name = %(genre)s
        ORDER BY rating DESC
        LIMIT 10
    ''',{'genre' : genre})