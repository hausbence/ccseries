from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_actors(year):
    return data_manager.execute_select("""
        SELECT actors.name, 2019 - EXTRACT(year from actors.birthday) AS age, EXTRACT(year from shows.year) as release
        FROM actors
        INNER JOIN show_characters ON show_characters.actor_id = actors.id
        INNER JOIN shows ON shows.id = show_characters.show_id
        WHERE EXTRACT(year from shows.year) = %(year)s AND actors.birthday IS NOT NULL
        ORDER BY age DESC
    """, {'year' : year})
