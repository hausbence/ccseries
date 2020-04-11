from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_shows_by_title(title):
    return data_manager.execute_select("""
        SELECT title, rating, year,trailer
        FROM shows
        WHERE title = %(title)s
    """, {'title' : title})