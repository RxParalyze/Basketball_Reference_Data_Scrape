package com.basketball.lineups;

import java.util.ArrayList;
import java.util.List;

import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class PlayersController {
    private List<Players> playerList = new ArrayList<>();

    @RequestMapping("/player/all")
    public List<Players> findAll() {
        return playerList;
    }
 
    @RequestMapping(value = "/player", method = RequestMethod.POST)
    public Players addplayer(Players player) {
        playerList.add(player);
        return player;
    }
 
    @RequestMapping("/player/findby/{id}")
    public Players findById(@PathVariable String id) {
        return playerList.stream().
                 filter(player -> player.getPlayer_name() == id).
                   findFirst().get();
    }
}
