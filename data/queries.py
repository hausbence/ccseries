from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_actors():
    return data_manager.execute_select("""
        SELECT actors.name, CAST(EXTRACT(YEAR FROM actors.birthday) AS INT)  as birthday,
                CAST(EXTRACT(YEAR FROM actors.death) AS INT) as death 
        FROM actors
        INNER JOIN show_characters ON actors.id = show_characters.actor_id
        INNER JOIN shows ON show_characters.show_id = shows.id
        INNER JOIN show_genres ON shows.id = show_genres.show_id
        INNER JOIN genres ON show_genres.genre_id = genres.id
        WHERE genres.name = 'Horror' AND actors.death IS NOT NULL
    """)