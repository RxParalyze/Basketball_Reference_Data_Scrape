package com.basketball.repository;

import com.basketball.model.Lineups;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface LineupRepo extends CrudRepository<Lineups, Integer> {

}
