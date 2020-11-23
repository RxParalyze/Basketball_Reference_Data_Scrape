import requests
#import MySQLdb
#import mysql.connector
import psycopg2 as postgres
import pandas as pd
from psycopg2 import Error
from bs4 import BeautifulSoup

# SQL connection data to connect and save data in
db = postgres.connect(
    host = "localhost",
    username = "phil",
    password = "password",
    database = "player_db",
    port = 3000
)


# URL to be scraped
url_base = 'https://www.basketball-reference.com/play-index/lineup_finder.cgi?request=1&match=game&lineup_type=2-man&output=total&is_playoffs=N&year_id='
url_year_start = 2017
# CHANGE THIS TO 2018 WHEN FINISHED DEBUGGING
url_year_end = 2017
url_middle = '&game_num_min=0&game_num_max=99&order_by=diff_pts&offset='
url_offset_start = 0
# CHANGE THIS TO 150000 WHEN FINISHED DEBUGGING
url_offset_end = 15000

offset_increments_start = url_offset_start / 100
offset_increments_end = url_offset_end / 100

url_list = []

for url_year in range(url_year_start, url_year_end + 1):
    for offset in range(int(offset_increments_start), int(offset_increments_end)+1):
        url_offset = offset * 100
        url_final = url_base + str(url_year) + url_middle + str(url_offset)
        url_list.append(url_final)
        print(url_final)


class row:
    def __init__(self, player_rank, player1_lineup, player2_lineup, game_date, team_player1, home_or_away, team_player2, win_or_loss, minutes_played, possessions_team1, possessions_team2, pace_factor, field_goals, field_goal_attempts, field_goal_perc, three_pt_fgs, three_pt_fg_attempts, three_pt_fg_perc, effective_fg_perc, free_throws, free_throw_attempts, free_throw_perc, points):
        self.panda_dict = pd.DataFrame({
            "player_rank" : [player_rank],
        "player1_lineup" : [player1_lineup],
        "player2_lineup" : [player2_lineup],
        "game_date" : [game_date],
        "team_player1" : [team_player1],
        "home_or_away" : [home_or_away],
        "team_player2" : [team_player2],
        "win_or_loss" : [win_or_loss],
        "minutes_played" : [minutes_played],
        "possessions_team1" : [possessions_team1],
        "possessions_team2" : [possessions_team2],
        "pace_factor" : [pace_factor],
        "field_goals" : [field_goals],
        "field_goal_attempts" : [field_goal_attempts],
        "field_goal_perc" : [field_goal_perc],
        "three_pt_fgs" : [three_pt_fgs],
        "three_pt_fg_attempts" : [three_pt_fg_attempts],
        "three_pt_fg_perc" : [three_pt_fg_perc],
        "effective_fg_perc" : [effective_fg_perc],
        "free_throws" : [free_throws],
        "free_throw_attempts" : [free_throw_attempts],
        "free_throw_perc" : [free_throw_perc],
        "points" : [points]
        })


# Prepare SQL query statement to INSERT a record into the database.
sql_statement = "INSERT INTO lineups(player_rank, player1_lineup, player2_lineup, game_date, team_player1, home_or_away, team_player2, win_or_loss, minutes_played, possessions_team1, possessions_team2, pace_factor, field_goals, field_goal_attempts, field_goal_perc, three_pt_fgs, three_pt_fg_attempts, three_pt_fg_perc, effective_fg_perc, free_throws, free_throw_attempts, free_throw_perc, points, url) VALUES ({}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, '{}')"

# the rollback sql statement
sql_rollback = "SELECT LAST_INSERT_ID()"
# .format(player_rank, player1_lineup, player2_lineup, game_date, team_player1, home_or_away, team_player2, win_or_loss, minutes_played, possessions_team1, possessions_team2, pace_factor, field_goals, field_goal_attempts, field_goal_perc, three_pt_fgs, three_pt_fg_attempts, three_pt_fg_perc, effective_fg_perc, free_throws, free_throw_attempts, free_throw_perc, points, 'NOW()', url)

# isolate the "th" tags in tbody from rest of table AND from table body headers


def has_csk(tag):
    return tag.has_attr("csk") and tag.name == "th"
def is_data(tag):
    return tag.has_attr("data-stat") and tag.name == "td"

for url in url_list:
    # Load html's plain data into a var
    plain_html_text = requests.get(url)
    # parse the data
    soup = BeautifulSoup(plain_html_text.text, "html5lib")
    # print(soup.prettify)
    row_list = []

    # Find the table
    get_ranks = soup.find_all(has_csk)
    get_data = soup.find_all(is_data)

    for y in range(0, len(get_ranks)):
        get_ranks[y] = get_ranks[y].text.strip()
    for y in range(0, len(get_data)):
        get_data[y] = get_data[y].text.strip()

    for y in range(0, len(get_ranks)):
        print(get_ranks[y])
    for y in range(0, len(get_data)):
        print(get_data[y])
        if(get_data[y].__contains__("+")):
            get_data[y] = str(get_data[y]).replace("+","")

    data_panda = pd.DataFrame(get_data)
    data_row_count = 21

    # find the "td" tags
    for counter in range(0, len(get_ranks)):
        data = counter * data_row_count
        player_rank = get_ranks[0]

        player_lineup = get_data[data].split("|")
        player1_lineup = player_lineup[0]
        player2_lineup = player_lineup[1]

        game_date = get_data[data+1]
        team_player1 = get_data[data+2]
        home_or_away = get_data[data+3]
        team_player2 = get_data[data+4]
        win_or_loss = get_data[data+5]
        minutes_played = get_data[data+6]
        possessions_team1 = get_data[data+7]
        possessions_team2 = get_data[data+8]
        pace_factor = get_data[data+9]
        field_goals = get_data[data+10]
        field_goal_attempts = get_data[data+11]
        field_goal_perc = get_data[data+12]
        three_pt_fgs = get_data[data+13]
        three_pt_fg_attempts = get_data[data+14]
        three_pt_fg_perc = get_data[data+15]
        effective_fg_perc = get_data[data+16]
        free_throws = get_data[data+17]
        free_throw_attempts = get_data[data+18]
        free_throw_perc = get_data[data+19]
        points = get_data[data+20]

        new_row = row(player_rank, player1_lineup, player2_lineup, game_date, team_player1, home_or_away, team_player2, win_or_loss, minutes_played, possessions_team1, possessions_team2, pace_factor,
                      field_goals, field_goal_attempts, field_goal_perc, three_pt_fgs, three_pt_fg_attempts, three_pt_fg_perc, effective_fg_perc, free_throws, free_throw_attempts, free_throw_perc, points)

        get_ranks.pop(0)
        data_panda.append(new_row.panda_dict)
        sql = "INSERT INTO lineups(player_rank, player1_lineup, player2_lineup, game_date, team_player1, home_or_away, team_player2, win_or_loss, minutes_played, possessions_team1, possessions_team2, pace_factor, field_goals, field_goal_attempts, field_goal_perc, three_pt_fgs, three_pt_fg_attempts, three_pt_fg_perc, effective_fg_perc, free_throws, free_throw_attempts, free_throw_perc, points,url) VALUES ({}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, '{}')".format(
            player_rank, player1_lineup, player2_lineup, game_date, team_player1, home_or_away, team_player2, win_or_loss, minutes_played, possessions_team1, possessions_team2, pace_factor, field_goals, field_goal_attempts, field_goal_perc, three_pt_fgs, three_pt_fg_attempts, three_pt_fg_perc, effective_fg_perc, free_throws, free_throw_attempts, free_throw_perc, points, url)
        #print(sql)

        # player_rank, player1_lineup, player2_lineup, game_date, team_player1, home_or_away, team_player2, win_or_loss, minutes_played, possessions_team1, possessions_team2, pace_factor, field_goals, field_goal_attempts, field_goal_perc, three_pt_fgs, three_pt_fg_attempts, three_pt_fg_perc, effective_fg_perc, free_throws, free_throw_attempts, free_throw_perc, points

        data_panda.fillna(value = -1776, inplace = True)

        try:
            cursor = db.cursor()
            print('about to execute')
            cursor.execute(sql)
            print("executed, about to commit")
            # Commit your changes in the database
            db.commit()
            print("committed")
        except mysql.connector.Error as error:
            print("something fucked up. Here's what went wrong: {}".format(error))
            cursor.execute(sql_rollback)
            # get the just inserted class id

        try:
            result = cursor.fetchone()
            # Set the class id to the just inserted class
            class_id = result[0]
            cursor.close()
        except:
            # disconnect from server
            cursor.close()
            # on error set the class_id to -1
            class_id = -1
db.commit()
db.close()
