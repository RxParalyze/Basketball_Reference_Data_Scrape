package com.basketball.lineups;

import java.util.ArrayList;
import java.util.List;

import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class LineupsController {
    private List<Lineups> entityList = new ArrayList<>();
 
    @RequestMapping("/entity/all")
    public List<Lineups> findAll() {
        return entityList;
    }
 
    @RequestMapping(value = "/entity", method = RequestMethod.POST)
    public Lineups addEntity(Lineups entity) {
        entityList.add(entity);
        return entity;
    }
 
    @RequestMapping("/entity/findby/{id}")
    public Lineups findById(@PathVariable int id) {
        return entityList.stream().
                 filter(entity -> entity.getLineup_rank() == id).
                   findFirst().get();
    }
}
