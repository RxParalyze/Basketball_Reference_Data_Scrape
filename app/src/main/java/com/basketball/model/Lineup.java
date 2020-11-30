package com.basketball.model;

import java.sql.Date;

import javax.persistence.Entity;
import javax.persistence.Table;

@Entity
@Table(name = "lineups")
public class Lineup {
    private int lineup_rank;
    private String player1;
    private String player2;
    private int game_number;
    private double pace_factor;
    private int points;
    private Date pull_time;
    private String url;

    public int getLineup_rank() {
        return lineup_rank;
    }

    public void setLineup_rank(int lineup_rank) {
        this.lineup_rank = lineup_rank;
    }

    public String getPlayer1() {
        return player1;
    }

    public void setPlayer1(String player1) {
        this.player1 = player1;
    }

    public String getPlayer2() {
        return player2;
    }

    public void setPlayer2(String player2) {
        this.player2 = player2;
    }

    public int getGame_number() {
        return game_number;
    }

    public void setGame_number(int game_number) {
        this.game_number = game_number;
    }

    public double getPace_factor() {
        return pace_factor;
    }

    public void setPace_factor(double pace_factor) {
        this.pace_factor = pace_factor;
    }

    public int getPoints() {
        return points;
    }

    public void setPoints(int points) {
        this.points = points;
    }

    public Date getPull_time() {
        return pull_time;
    }

    public void setPull_time(Date pull_time) {
        this.pull_time = pull_time;
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

}