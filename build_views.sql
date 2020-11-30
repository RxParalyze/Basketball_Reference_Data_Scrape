SET search_path TO "lineup_schema";

/*
DROP VIEW rank_view;
DROP VIEW high_scores;
DROP VIEW best_field_goal_perc;
*/

CREATE OR REPLACE VIEW rank_view(ranks, player1, player2) AS
    SELECT lineup_rank, player1, player2
    FROM lineups NATURAL JOIN players
    GROUP BY lineup_rank, players.player_name;

CREATE OR REPLACE VIEW high_scores(player1, player2, points) AS
    SELECT player1, player2, points
    FROM lineups
    WHERE lineups.pace_factor > 100
    GROUP BY lineup_rank;

CREATE OR REPLACE VIEW best_field_goal_perc(top_team) AS
    SELECT lineup_rank, player1, player2, field_goal_perc
    FROM lineups NATURAL JOIN field_goals
    WHERE field_goals.field_goal_perc =
        (SELECT MAX(field_goal_perc) FROM field_goals)
    GROUP BY lineup_rank, field_goals.field_goal_perc;
