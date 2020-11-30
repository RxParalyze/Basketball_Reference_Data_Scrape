package com.basketball.lineups;

import java.util.ArrayList;
import java.util.List;

import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class PlayersController {
    private List<Players> entityList = new ArrayList<>();

    @RequestMapping("/entity/all")
    public List<Players> findAll() {
        return entityList;
    }
 
    @RequestMapping(value = "/entity", method = RequestMethod.POST)
    public Players addEntity(Players entity) {
        entityList.add(entity);
        return entity;
    }
 
    @RequestMapping("/entity/findby/{id}")
    public Players findById(@PathVariable String id) {
        return entityList.stream().
                 filter(entity -> entity.getPlayer_name() == id).
                   findFirst().get();
    }
}
