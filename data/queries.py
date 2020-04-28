from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_genres():
    return data_manager.execute_select('''
        SELECT name, id
        FROM genres
    ''')


def get_shows_by_genreID(genreid):
    return data_manager.execute_select('''
        SELECT shows.title, COUNT(episodes.episode_number) as num_of_episodes,
         MAX(seasons.season_number) as num_of_seasons
        FROM shows
        INNER JOIN seasons ON shows.id = seasons.show_id
        INNER JOIN episodes ON seasons.id = episodes.season_id
        INNER JOIN show_genres ON shows.id = show_genres.show_id
        WHERE show_genres.genre_id = %(genreid)s
        GROUP BY shows.id
        HAVING COUNT(episodes.episode_number) > 20
        ORDER BY num_of_episodes 
        LIMIT 50
    ''', {'genreid': genreid})