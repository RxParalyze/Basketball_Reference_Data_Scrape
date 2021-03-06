package com.basketball.repository;

import com.basketball.model.Lineup;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Repository;

@Repository
public interface LineupRepo extends CrudRepository<Lineup, Integer> {

}
