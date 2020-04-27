from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_actors():
    return data_manager.execute_select('''
        SELECT actors.name, COUNT(show_characters.actor_id) as num_of_roles, actors.id
        from actors
        INNER JOIN show_characters ON actors.id = show_characters.actor_id
        INNER JOIN shows ON show_characters.show_id = shows.id
        WHERE death IS NOT NULL
        GROUP BY actors.id
        ORDER BY num_of_roles DESC
        LIMIT 10
    ''')


def get_shows_by_actors(ids):
    return data_manager.execute_select('''
        SELECT show_characters.character_name, actors.name, shows.title
        FROM show_characters
        INNER JOIN actors ON show_characters.actor_id = actors.id
        INNER JOIN shows ON show_characters.show_id = shows.id
        WHERE show_characters.actor_id IN %(ids)s
    ''', {'ids': ids})
