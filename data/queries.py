from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_all_genres():
    return data_manager.execute_select("""
        SELECT *
        FROM genres
    """)


def get_shows_by_genre(id):
    return data_manager.execute_select("""
        SELECT shows.title, shows.id, COUNT(episodes.episode_number) as num_of_episodes,
         MAX(seasons.season_number) as num_of_seasons
        FROM shows
        INNER JOIN show_genres ON show_genres.show_id = shows.id
        INNER JOIN seasons ON seasons.show_id = shows.id
        INNER JOIN episodes ON episodes.season_id = seasons.id
        WHERE genre_id = %(id)s
        GROUP BY shows.id, seasons.show_id
        HAVING COUNT(episodes.episode_number) > 20
        ORDER BY num_of_episodes
    """, {"id" : id})

def gettttt():
    return data_manager.execute_select('''
        SELECT COUNT(seasons.season_number) as num_of_seasons
        FROM seasons
        GROUP BY seasons.show_id
    ''')