SET search_path TO "lineup_schema";

DROP INDEX rank_index;
DROP INDEX player_index;
DROP INDEX team_index;

CREATE INDEX rank_index ON lineups(lineup_rank);

CREATE INDEX player_index on players(player_name);

CREATE INDEX team_index ON teams(team_name);