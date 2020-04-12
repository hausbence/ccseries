from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_actors(year):
    return data_manager.execute_select("""
        SELECT actors.name, actors.birthday, COUNT(show_characters.actor_id) as num_of_roles,
            CAST(AVG(shows.rating) AS DECIMAL(10,2)) as rating
        FROM actors
        INNER JOIN show_characters ON show_characters.actor_id = actors.id
        INNER JOIN shows ON shows.id = show_characters.show_id
        WHERE EXTRACT(year from actors.birthday) > %(year)s
        GROUP BY actors.birthday, actors.name
    """, {'year' : year})