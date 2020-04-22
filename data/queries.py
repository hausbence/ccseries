from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_all_shows(input1):
    return data_manager.execute_select('''
        SELECT shows.title, shows.year, ROUND(shows.rating, 2) as rating, shows.overview
        from shows
        ORDER BY title LIKE (%(input1)s)
        LIMIT 50
    ''', {'input1' : input1})


def get_all_seasons(input1):
    return data_manager.execute_select('''
        SELECT shows.title as show_title, seasons.title as season_title, seasons.overview
        from seasons
        INNER JOIN shows ON seasons.show_id = shows.id
        ORDER BY shows.title LIKE(%(input1)s)
        LIMIT 50
    ''', {'input1': input1})


def get_all_episodes(input1):
    return data_manager.execute_select('''
        SELECT shows.title as show_title, seasons.season_number, episodes.episode_number, episodes.title as episode_name,
                episodes.overview 
        from episodes
        INNER JOIN seasons ON episodes.season_id = seasons.id
        INNER JOIN shows ON seasons.show_id = shows.id
        ORDER BY episodes.title LIKE(%(input1)s)
        LIMIT 50
    ''', {'input1': input1})