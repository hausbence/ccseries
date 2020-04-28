from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def fuzzy(charname):
    return data_manager.execute_select('''
        SELECT shows.title, actors.name as actor, show_characters.character_name
        from shows
        INNER JOIN show_characters ON shows.id = show_characters.show_id
        INNER JOIN actors ON show_characters.actor_id = actors.id
        WHERE show_characters.character_name ILIKE %(charname)s
    ''', {'charname' : charname})