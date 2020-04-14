from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_actors():
    return data_manager.execute_select("""
        SELECT actors.name, COUNT(actor_id) as num_of_shows,
        CASE
         WHEN actors.death IS NOT NULL THEN EXTRACT(year from actors.death) - EXTRACT(year from actors.birthday)
         WHEN actors.death IS NULL THEN 2020 - EXTRACT(year from actors.birthday)
        END AS age
        FROM actors
        INNER JOIN show_characters ON show_characters.show_id = actors.id
        GROUP BY actors.id
    """)



def maryn():
    return data_manager.execute_select('''
    SELECT COUNT(show_characters.id) AS count_of_roles, name, death,actors.id,
            date_part('year', age(birthday))::int AS age,
            CASE WHEN death IS NULL THEN 'False' ELSE 'True' END AS dead
    FROM actors 
    JOIN show_characters ON show_characters.actor_id = actors.id
    GROUP BY actors.id
    ORDER BY count_of_roles DESC;
    ''')