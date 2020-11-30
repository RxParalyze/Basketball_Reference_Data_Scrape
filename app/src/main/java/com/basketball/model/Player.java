package com.basketball.model;

import javax.persistence.Entity;
import javax.persistence.Table;

@Entity
@Table(name="players")
public class Player {
    private String player_name;
    private int[] player_lineups;
    private String team_name;

    public String getPlayer_name() {
        return player_name;
    }

    public void setPlayer_name(String player_name) {
        this.player_name = player_name;
    }

    public int[] getPlayer_lineups() {
        return player_lineups;
    }

    public void setPlayer_lineups(int[] player_lineups) {
        this.player_lineups = player_lineups;
    }

    public String getTeam_name() {
        return team_name;
    }

    public void setTeam_name(String team_name) {
        this.team_name = team_name;
    }
}
