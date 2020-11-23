DROP DATABASE IF EXISTS lineup_db;
CREATE DATABASE lineup_db;
USE lineup_db;
CREATE TABLE lineups (
  row_num INT NOT NULL AUTO_INCREMENT,
  lineup_rank INT COLLATE utf8_unicode_ci NOT NULL,
  player1_lineup VARCHAR(255) COLLATE utf8_unicode_ci NOT NULL,
  player2_lineup VARCHAR(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  game_date DATE COLLATE utf8_unicode_ci DEFAULT NULL,
  lineup_team VARCHAR(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  home_or_away VARCHAR(3) COLLATE utf8_unicode_ci DEFAULT NULL,
  opp_team VARCHAR(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  win_or_loss VARCHAR(3) COLLATE utf8_unicode_ci DEFAULT NULL,
  minutes_played DECIMAL COLLATE utf8_unicode_ci NOT NULL,
  possessions_team1 INT COLLATE utf8_unicode_ci NOT NULL,
  possessions_team2 INT COLLATE utf8_unicode_ci NOT NULL,
  pace_factor DECIMAL COLLATE utf8_unicode_ci NOT NULL,
  field_goals INT COLLATE utf8_unicode_ci NOT NULL,
  field_goal_attempts INT COLLATE utf8_unicode_ci NOT NULL,
  field_goal_perc DECIMAL COLLATE utf8_unicode_ci DEFAULT NULL,
  three_pt_fgs INT COLLATE utf8_unicode_ci NOT NULL,
  three_pt_fg_attempts INT COLLATE utf8_unicode_ci NOT NULL,
  three_pt_fg_perc DECIMAL COLLATE utf8_unicode_ci NOT NULL,
  effective_fg_perc DECIMAL COLLATE utf8_unicode_ci NOT NULL,
  free_throws INT COLLATE utf8_unicode_ci NOT NULL,
  free_throw_attempts INT COLLATE utf8_unicode_ci NOT NULL,
  free_throw_perc DECIMAL COLLATE utf8_unicode_ci DEFAULT NULL,
  points INT COLLATE utf8_unicode_ci NOT NULL,
  pull_time TIMESTAMP DEFAULT NOW(),
  url TEXT COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (row_num),
  FOREIGN KEY (lineup_rank) REFERENCES players(lineup_rank)
) ENGINE = InnoDB AUTO_INCREMENT = 0 DEFAULT CHARSET = utf8 COLLATE = utf8_unicode_ci;

CREATE TABLE players (
  player_name VARCHAR(255) COLLATE utf8_unicode_ci NOT NULL,
  player_lineups INTEGER ARRAY COLLATE utf8_unicode_ci NOT NULL,
  player2_lineup VARCHAR(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  game_date DATE COLLATE utf8_unicode_ci DEFAULT NULL,
  lineup_team VARCHAR(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  win_or_loss VARCHAR(3) COLLATE utf8_unicode_ci DEFAULT NULL,
  minutes_played DECIMAL COLLATE utf8_unicode_ci NOT NULL,
  possessions_team1 INT COLLATE utf8_unicode_ci NOT NULL,
  possessions_team2 INT COLLATE utf8_unicode_ci NOT NULL,
  pace_factor DECIMAL COLLATE utf8_unicode_ci NOT NULL,

  points INT COLLATE utf8_unicode_ci NOT NULL,
  pull_time TIMESTAMP DEFAULT NOW(),
  url TEXT COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (lineup_rank),
  FOREIGN KEY (lineup_rank) REFERENCES players(lineup_rank)
) ENGINE = InnoDB AUTO_INCREMENT = 0 DEFAULT CHARSET = utf8 COLLATE = utf8_unicode_ci;

CREATE TABLE field_goals (
  field_goals INT COLLATE utf8_unicode_ci NOT NULL,
  field_goal_attempts INT COLLATE utf8_unicode_ci NOT NULL,
  field_goal_perc DECIMAL COLLATE utf8_unicode_ci DEFAULT NULL,
  FOREIGN KEY (lineup_rank) REFERENCES lineups(lineup_rank)
) ENGINE = InnoDB AUTO_INCREMENT = 0 DEFAULT CHARSET = utf8 COLLATE = utf8_unicode_ci;

CREATE TABLE possessions (
  FOREIGN KEY (lineup_rank) REFERENCES lineups(lineup_rank)
) ENGINE = InnoDB AUTO_INCREMENT = 0 DEFAULT CHARSET = utf8 COLLATE = utf8_unicode_ci;

CREATE TABLE three_pt_fgs (
  three_pt_fgs INT COLLATE utf8_unicode_ci NOT NULL,
  three_pt_fg_attempts INT COLLATE utf8_unicode_ci NOT NULL,
  three_pt_fg_perc DECIMAL COLLATE utf8_unicode_ci NOT NULL,
  effective_fg_perc DECIMAL COLLATE utf8_unicode_ci NOT NULL,
  FOREIGN KEY (lineup_rank) REFERENCES lineups(lineup_rank)
) ENGINE = InnoDB AUTO_INCREMENT = 0 DEFAULT CHARSET = utf8 COLLATE = utf8_unicode_ci;

CREATE TABLE free_throws (
  free_throws INT COLLATE utf8_unicode_ci NOT NULL,
  free_throw_attempts INT COLLATE utf8_unicode_ci NOT NULL,
  free_throw_perc DECIMAL COLLATE utf8_unicode_ci DEFAULT NULL,
  FOREIGN KEY (lineup_rank) REFERENCES lineups(lineup_rank)
) ENGINE = InnoDB AUTO_INCREMENT = 0 DEFAULT CHARSET = utf8 COLLATE = utf8_unicode_ci;

CREATE TABLE teams (
  FOREIGN KEY (lineup_rank) REFERENCES lineups(lineup_rank)
) ENGINE = InnoDB AUTO_INCREMENT = 0 DEFAULT CHARSET = utf8 COLLATE = utf8_unicode_ci;

CREATE TABLE location_stats (
  FOREIGN KEY (lineup_rank) REFERENCES lineups(lineup_rank)
) ENGINE = InnoDB AUTO_INCREMENT = 0 DEFAULT CHARSET = utf8 COLLATE = utf8_unicode_ci;


