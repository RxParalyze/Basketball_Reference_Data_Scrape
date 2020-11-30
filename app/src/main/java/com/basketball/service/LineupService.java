package com.basketball.service;

import java.util.List;
import java.util.Optional;

import com.basketball.model.Lineup;
import com.basketball.repository.LineupRepo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class LineupService implements EntityService {
    @Autowired
    private LineupRepo repository;

    @Override
    public List<Lineup> findAll() {
        List<Lineup> lineups = (List<Lineup>) repository.findAll();
        return lineups;
    }

    public Optional<Lineup> findId(int lineupNum) {
        Optional<Lineup> lineup = (Optional<Lineup>) repository.findById(lineupNum);
        return lineup;
    }
}
