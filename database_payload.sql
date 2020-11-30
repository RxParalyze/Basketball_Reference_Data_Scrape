SET search_path TO "lineup_schema";

INSERT INTO teams(team_name, game_numbers, players) VALUES
    ('WAS', '{1}', '{I. Mahinmi, J. Wall}'),
    ('LAC', '{2, 3, 4, 5}', '{B. Griffin, . Redick, L. Mbah a Moute, C. Paul, D. Jordan}'),
    ('PHO', '{1}', '{}'),
    ('BRK', '{2, 3, 4, 5}', '{}')
;

INSERT INTO players(player_name, player_lineups, team_name) VALUES
    ('B. Griffin', '{2, 5}', 'LAC'),
    ('J. Redick', '{2, 4}', 'LAC'),
    ('L. Mbah a Moute', '{3}', 'LAC'),
    ('C. Paul', '{3, 4}', 'LAC'),
    ('D. Jordan', '{5}', 'LAC'),
    ('I. Mahinmi', '{1}', 'WAS'),
    ('J. Wall', '{1}', 'WAS')
;

INSERT INTO games(home_team, away_team, game_date, winning_team) VALUES
    ('PHO', 'WAS', '2017-03-07', 'WAS'),
    ('LAC', 'BRK', '2016-11-14', 'LAC')
;

INSERT INTO lineups(lineup_rank, player1, player2, game_number, pace_factor, points, url) VALUES
    (1, 'I. Mahinmi', 'J. Wall', 1, 110.3, 43, 'https://stathead.com/basketball/lineup_finder.cgi?request=1&match=game&lineup_type=2-man&output=total&is_playoffs=N&year_id=2017'),
    (2, 'B. Griffin', 'J. Redick', 2, 98.2, 43, 'https://stathead.com/basketball/lineup_finder.cgi?request=1&match=game&lineup_type=2-man&output=total&is_playoffs=N&year_id=2017'),
    (3, 'L. Mbah a Moute', 'C. Paul', 2, 98.2, 43, 'https://stathead.com/basketball/lineup_finder.cgi?request=1&match=game&lineup_type=2-man&output=total&is_playoffs=N&year_id=2017'),
    (4, 'C. Paul', 'J. Redick', 2, 98.2, 43, 'https://stathead.com/basketball/lineup_finder.cgi?request=1&match=game&lineup_type=2-man&output=total&is_playoffs=N&year_id=2017'),
    (5, 'B. Griffin', 'D. Jordan', 2, 96.7, 43, 'https://stathead.com/basketball/lineup_finder.cgi?request=1&match=game&lineup_type=2-man&output=total&is_playoffs=N&year_id=2017')
;

INSERT INTO field_goals(lineup_rank, field_goals, field_goal_attempts, field_goal_perc) VALUES
    (1, 12, 6, .38),
    (2, 19, 16, .294),
    (3, 19, 16, .294),
    (4, 19, 16, .294),
    (5, 19, 16, .292)
;

INSERT INTO possessions(lineup_rank, possessions_team1, possessions_team2) VALUES
    (1, 36, 33),
    (2, 48, 46),
    (3, 48, 46),
    (4, 48, 46),
    (5, 48, 47)
;

INSERT INTO three_pt_fgs(lineup_rank, three_pt_fgs, three_pt_fg_attempts, three_pt_fg_perc, effective_fg_perc) VALUES
    (1, 4, 2, .5, .451),
    (2, 1, -7, .306, .283),
    (3, 1, -7, .306, .283),
    (4, 1, -7, .306, .283),
    (5, 1, -8, .320, .281)
;

INSERT INTO free_throws(lineup_rank, free_throws, free_throw_attempts, free_throw_perc) VALUES
    (1, 15, 24, -.107),
    (2, 4, 6, -.182),
    (3, 4, 6, -.182),
    (4, 4, 6, -.182),
    (5, 4, 6, -.182)
;
