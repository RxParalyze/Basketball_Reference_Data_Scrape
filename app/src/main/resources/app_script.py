import requests
#import postgresdb
#import postgres.connector
import psycopg2 as postgres
import pandas as pd
from psycopg2 import Error
from bs4 import BeautifulSoup

session = requests.Session()

payload = {
    'username': '<USERNAME>',
    'password': '<PASSWORD>'
}


# SQL connection data to connect and save data in
db = postgres.connect(
    host = "localhost",
    user = "postgres",
    password = "password",
    database = "postgres",
    port = 5432
)

game_location = "@"

# URL to be scraped
url_base = 'https://stathead.com/basketball/lineup_finder.cgi?request=1&match=game&lineup_type=2-man&output=total&is_playoffs=N&year_id='
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
        #print(url_final)


class row:
    def __init__(self, lineup_rank, player1_lineup, player2_lineup, game_date, team_name, home_or_away, opp_team, win_or_loss, minutes_played, team1_possessions, team2_possessions, pace_factor, field_goals, field_goal_attempts, field_goal_perc, three_pt_fgs, three_pt_fg_attempts, three_pt_fg_perc, effective_fg_perc, free_throws, free_throw_attempts, free_throw_perc, points):
        self.panda_dict = pd.DataFrame({
            "lineup_rank" : [lineup_rank],
        "player1_lineup" : [player1_lineup],
        "player2_lineup" : [player2_lineup],
        "game_date" : [game_date],
        "team_name" : [team_name],
        "home_or_away" : [home_or_away],
        "opp_team" : [opp_team],
        "win_or_loss" : [win_or_loss],
        "minutes_played" : [minutes_played],
        "team1_possessions" : [team1_possessions],
        "team2_possessions" : [team2_possessions],
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


# the rollback sql statement
sql_rollback = "SELECT LAST_INSERT_ID()"
# .format(lineup_rank, player1_lineup, player2_lineup, game_date, team_name, home_or_away, opp_team, win_or_loss, minutes_played, team1_possessions, team2_possessions, pace_factor, field_goals, field_goal_attempts, field_goal_perc, three_pt_fgs, three_pt_fg_attempts, three_pt_fg_perc, effective_fg_perc, free_throws, free_throw_attempts, free_throw_perc, points, 'NOW()', url)

# isolate the "th" tags in tbody from rest of table AND from table body headers


def has_csk(tag):
    return tag.name == "th" and tag.has_attr("csk")
def is_data(tag):
    return tag.name == "td" and tag.has_attr("data-stat")

for url in url_list:
    # Load html's plain data into a var
    plain_html_text = session.post("https://stathead.com/users/login.cgi", data = payload)
    print(url)
    plain_html_text = session.get(url, headers = dict(referer = url))
    print(plain_html_text.ok)
    # parse the data
    soup = BeautifulSoup(plain_html_text.text, "html5lib")
    print(soup.prettify)
    row_list = []

    # Find the table
    get_ranks = soup.find_all(has_csk)
    print(len(get_ranks))
    get_data = soup.find_all(is_data)

    for y in range(0, len(get_ranks)):
        get_ranks[y] = get_ranks[y].text.strip()
    for y in range(0, len(get_data)):
        get_data[y] = get_data[y].text.strip()

    for y in range(0, len(get_ranks)):
        #print(get_ranks[y])
        continue
    for y in range(0, len(get_data)):
        #print(get_data[y])
        if(get_data[y].__contains__("+")):
            get_data[y] = str(get_data[y]).replace("+","")

    data_panda = pd.DataFrame(get_data)
    data_row_count = 22

    # find the "td" tags
    for counter in range(0, len(get_ranks)):
        data = counter * data_row_count
        lineup_rank = get_ranks[0]
        player_lineup = get_data[data].split("|")
        print(player_lineup)
        player1_lineup = player_lineup[0]
        print(player1_lineup)
        player2_lineup = player_lineup[1]
        game_date = get_data[data+1]
        team_name = get_data[data+2]
        home_or_away = get_data[data+3]
        opp_team = get_data[data+4]
        win_or_loss = get_data[data+5]
        minutes_played = get_data[data+6]
        team1_possessions = get_data[data+7]
        team2_possessions = get_data[data+8]
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

        new_row = row(lineup_rank, player1_lineup, player2_lineup, game_date, team_name, home_or_away, opp_team, win_or_loss, minutes_played, team1_possessions, team2_possessions, pace_factor,
                      field_goals, field_goal_attempts, field_goal_perc, three_pt_fgs, three_pt_fg_attempts, three_pt_fg_perc, effective_fg_perc, free_throws, free_throw_attempts, free_throw_perc, points)

        get_ranks.pop(0)
        data_panda.append(new_row.panda_dict)

        home_team = ""
        away_team = ""

        if game_location in home_or_away:
            home_team = opp_team
            away_team = team_name
        else:
            home_team = team_name
            away_team = opp_team

        sql_teams = "INSERT INTO teams(players, game_date, winning_team) VALUES ('{}', {}, '{}')".format(
            [player1_lineup, player2_lineup], game_date, win_or_loss)
        #print(sql)
        sql_player_1 = "INSERT INTO players(player_name, lineup_rank, team_name) VALUES ('{}', {}, '{}')".format(
            player1_lineup, lineup_rank, team_name)

        sql_player_2 = "INSERT INTO players(player_name, lineup_rank, team_name) VALUES ('{}', {}, '{}')".format(
            player2_lineup, lineup_rank, team_name)

        sql_games = "INSERT INTO games(home_team, away_team,game_date, win_or_loss) VALUES ('{}', '{}', {}, '{}')".format(
            home_team, away_team, game_date, win_or_loss)

        sql_field_goals = "INSERT INTO field_goals(lineup_rank, field_goals, field_goal_attempts, field_goal_perc) VALUES ({}, {}, {}, {})".format(
            lineup_rank, field_goals, field_goal_attempts, field_goal_perc)

        sql_possessions = "INSERT INTO possessions(lineup_rank, team1_possessions, team2_possessions) VALUES ({}, {}, {})".format(
            lineup_rank, team1_possessions, team2_possessions)

        sql_three_pt_fgs = "INSERT INTO three_pt_fgs(lineup_rank, three_pt_fgs, three_pt_fg_attempts, three_pt_fg_perc, effective_fg_perc) VALUES ({}, {}, {}, {}, {})".format(
            lineup_rank, three_pt_fgs, three_pt_fg_attempts, three_pt_fg_perc, effective_fg_perc)

        sql_free_throws = "INSERT INTO free_throws(lineup_rank, free_throws, free_throw_attempts, free_throw_perc) VALUES ({}, {}, {}, {})".format(
            lineup_rank, free_throws, free_throw_attempts, free_throw_perc)


        # lineup_rank, player1_lineup, player2_lineup, game_date, team_name, home_or_away, opp_team, win_or_loss, minutes_played, team1_possessions, team2_possessions, pace_factor, field_goals, field_goal_attempts, field_goal_perc, three_pt_fgs, three_pt_fg_attempts, three_pt_fg_perc, effective_fg_perc, free_throws, free_throw_attempts, free_throw_perc, points

        data_panda.fillna(value = 0, inplace = True)
        cursor = db.cursor()
        try:
            print("starting execute")
            cursor.execute(sql_teams)
            cursor.execute(sql_player_1)
            cursor.execute(sql_player_2)
            cursor.execute(sql_games)
            cursor.execute(sql_field_goals)
            cursor.execute(sql_possessions)
            cursor.execute(sql_three_pt_fgs)
            cursor.execute(free_throws)
            # Commit your changes in the database
            db.commit()
            print("committed")
        except postgres.connector.Error as error:
            print("something messed up. Here's what went wrong: {}".format(error))
            cursor.execute(sql_rollback)
            # get the just inserted class id

        game_number_string = ("SELECT game_number FROM games WHERE game_date = {} AND home_team = '{}'").format(game_date, home_team)
        game_number = cursor.execute(game_number_string)

        sql_lineups = "INSERT INTO lineups(lineup_rank, player1, player2, game_number, minutes_played, pace_factor, points, url) VALUES ({}, '{}', '{}', {}, {}, {}, {}, '{}')".format(
            lineup_rank, player1_lineup, player2_lineup, game_number, minutes_played, pace_factor, points, url)

        try:
            print("starting execute")
            cursor.execute(sql_lineups)
            # Commit your changes in the database
            db.commit()
            print("committed")
        except postgres.connector.Error as error:
            print("something messed up. Here's what went wrong: {}".format(error))
            cursor.execute(sql_rollback)

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
