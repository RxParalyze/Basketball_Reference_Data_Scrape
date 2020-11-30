package com.basketball.controller;

import java.util.ArrayList;
import java.util.List;

import com.basketball.model.Lineups;

import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/lineup")
public class LineupsController {
    private List<Lineups> lineupList = new ArrayList<>();

    @RequestMapping("/all")
    public List<Lineups> findAll() {
        return lineupList;
    }

    @RequestMapping(value = "/add", method = RequestMethod.POST)
    public Lineups addlineup(Lineups lineup) {
        lineupList.add(lineup);
        return lineup;
    }

    @RequestMapping("/findby/{id}")
    public Lineups findById(@PathVariable int id) {
        return lineupList.stream().
                 filter(lineup -> lineup.getLineup_rank() == id).
                   findFirst().get();
    }
}
