package com.basketball.controller;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

import com.basketball.model.Lineup;
import com.basketball.service.LineupService;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/lineup")
public class LineupController {
    @Autowired LineupService lineupService;

    @RequestMapping("/all")
    public String findAll(Model model) {
        List<Lineup> lineups = (List<Lineup>) lineupService.findAll();

        model.addAttribute("lineups", lineups);

        return "lineups";
    }

    @RequestMapping("/findby/{id}")
    public String findById(@PathVariable int id) {
        Optional<Lineup> lineup = (Optional<Lineup>) lineupService.findId(id);

        if (lineup.isPresent())
            return lineup.toString();
        else
            return "Not found";
    }
}
