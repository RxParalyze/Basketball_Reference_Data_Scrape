package com.basketball.service;

import java.util.List;
import java.util.Optional;

import com.basketball.model.Player;
import com.basketball.repository.PlayerRepo;

import org.springframework.beans.factory.annotation.Autowired;

public class PlayerService implements EntityService {
    @Autowired
    private PlayerRepo repository;

    @Override
    public List<Player> findAll() {
        List<Player> players = (List<Player>) repository.findAll();
        return players;
    }

    public Optional<Player> findId(String playerName) {
        Optional<Player> player = (Optional<Player>) repository.findById(playerName);
        return player;
    }

}
