from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_years():
    return data_manager.execute_select('''
        SELECT EXTRACT(YEAR FROM shows.year) as year, ROUND(AVG(shows.rating), 2) as rating, COUNT(shows.id) as num_of_shows
        FROM shows
        WHERE 1970 <= EXTRACT(YEAR FROM shows.year) AND 2010 >= EXTRACT(YEAR FROM shows.year) 
        GROUP BY shows.year
    ''')