from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_actor_for_longest_shows():
    return data_manager.execute_select('''
        SELECT shows.title, show_characters.character_name AS name, count(episodes.id) * shows.runtime AS runtime
        FROM shows
        JOIN seasons on shows.id = seasons.show_id
        JOIN episodes on seasons.id = episodes.season_id
        JOIN show_characters on shows.id = show_characters.show_id
        GROUP BY show_characters.id, shows.title, runtime
        ORDER BY runtime DESC
    ''')


def get_longest_show_actors(ids):
    return data_manager.execute_select("""
    SELECT character_name AS name, shows.title
    FROM show_characters
    JOIN shows on show_characters.show_id = shows.id
    WHERE show_id IN %(ids)s
    """, {'ids' : ids})


def get_longest_show():
    return data_manager.execute_select('''
    SELECT shows.id, shows.title, count(episodes.id) * shows.runtime AS runtime
    FROM shows
    JOIN seasons on shows.id = seasons.show_id
    JOIN episodes on seasons.id = episodes.season_id
    GROUP BY shows.id
    ORDER BY runtime DESC
    LIMIT 10
    ''')