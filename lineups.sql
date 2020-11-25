DROP SCHEMA IF EXISTS "lineup_schema" CASCADE;
CREATE SCHEMA "lineup_schema";
SET search_path TO "lineup_schema";

CREATE TABLE "teams" (
  team_name VARCHAR(255)  NOT NULL,
  game_numbers INT ARRAY,
  players VARCHAR ARRAY,
  PRIMARY KEY (team_name)
) ;

CREATE TABLE "players" (
  player_name VARCHAR(255)  NOT NULL,
  player_lineups INTEGER ARRAY  NOT NULL,
  team_name VARCHAR(255)  DEFAULT NULL,
  PRIMARY KEY (player_name),
  FOREIGN KEY (team_name) REFERENCES teams(team_name)
) ;

CREATE TABLE "games" (
  game_number SERIAL,
  home_team VARCHAR(255)  NOT NULL,
  away_team VARCHAR(255)  NOT NULL,
  game_date DATE,
  winning_team VARCHAR(255)  NOT NULL,
  PRIMARY KEY (game_number),
  FOREIGN KEY (home_team) REFERENCES teams(team_name),
  FOREIGN KEY (away_team) REFERENCES teams(team_name)
);

CREATE TABLE "lineups" (
  lineup_rank INT  NOT NULL,
  player1 VARCHAR(255)  NOT NULL,
  player2 VARCHAR(255)  DEFAULT NULL,
  game_number INT  NOT NULL,
  pace_factor DECIMAL  NOT NULL,
  points INT  NOT NULL,
  pull_time TIMESTAMP DEFAULT NOW(),
  url TEXT  DEFAULT NULL,
  PRIMARY KEY (lineup_rank),
  FOREIGN KEY (player1) REFERENCES players(player_name),
  FOREIGN KEY (player2) REFERENCES players(player_name),
  FOREIGN KEY (game_number) REFERENCES games(game_number)
) ;

CREATE TABLE "field_goals" (
  lineup_rank INT  NOT NULL,
  field_goals INT  NOT NULL,
  field_goal_attempts INT  NOT NULL,
  field_goal_perc DECIMAL  DEFAULT NULL,
  FOREIGN KEY (lineup_rank) REFERENCES lineups(lineup_rank)
) ;

CREATE TABLE "possessions" (
  lineup_rank INT  NOT NULL,
  possessions_team1 INT  NOT NULL,
  possessions_team2 INT  NOT NULL,
  FOREIGN KEY (lineup_rank) REFERENCES lineups(lineup_rank)
) ;

CREATE TABLE "three_pt_fgs" (
  lineup_rank INT  NOT NULL,
  three_pt_fgs INT  NOT NULL,
  three_pt_fg_attempts INT  NOT NULL,
  three_pt_fg_perc DECIMAL  NOT NULL,
  effective_fg_perc DECIMAL  NOT NULL,
  FOREIGN KEY (lineup_rank) REFERENCES lineups(lineup_rank)
) ;

CREATE TABLE "free_throws" (
  lineup_rank INT  NOT NULL,
  free_throws INT  NOT NULL,
  free_throw_attempts INT  NOT NULL,
  free_throw_perc DECIMAL  DEFAULT NULL,
  FOREIGN KEY (lineup_rank) REFERENCES lineups(lineup_rank)
) ;