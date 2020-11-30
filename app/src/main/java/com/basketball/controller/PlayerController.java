package com.basketball.controller;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

import com.basketball.model.Player;
import com.basketball.service.PlayerService;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/player")
public class PlayerController {
    @Autowired PlayerService playerService;

    @RequestMapping("/all")
    public String findAll(Model model) {
        List<Player> players = (List<Player>) playerService.findAll();

        model.addAttribute("players", players);

        return "players";
    }

    @RequestMapping("/findby/{id}")
    public String findById(@PathVariable String id) {
        Optional<Player> player = (Optional<Player>) playerService.findId(id);

        if (player.isPresent())
            return player.get().toString();
        else
            return "not found";
    }
}
