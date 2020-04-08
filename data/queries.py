from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def list_shows_with_episodes_num():
    return data_manager.execute_select(
    """
    SELECT COUNT(episodes.episode_number) AS number_of_episodes, shows.title
    FROM episodes
    JOIN seasons ON seasons.id = episodes.season_id
    JOIN shows ON seasons.show_id = shows.id
    GROUP BY shows.title
    """)


def get_actors():
    return data_manager.execute_select('''
    SELECT COUNT(show_characters.id) AS count_of_roles, name, death,
            date_part('year', age(birthday))::int AS age,
            CASE WHEN death IS NULL THEN 'False' ELSE 'True' END AS dead
    FROM actors 
    JOIN show_characters ON show_characters.actor_id = actors.id
    GROUP BY actors.id
    ORDER BY count_of_roles DESC;
    ''')