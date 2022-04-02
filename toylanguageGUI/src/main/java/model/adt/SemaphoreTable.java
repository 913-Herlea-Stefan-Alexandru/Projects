package model.adt;

import exceptions.MyException;
import javafx.util.Pair;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class SemaphoreTable implements ISemaphoreTable{
    private Map<Integer, Pair<Integer, List<Integer>>> map;
    private int freeLoc;
    private Lock lock;

    public SemaphoreTable() {
        this.map = new HashMap<Integer, Pair<Integer, List<Integer>>>();
        this.freeLoc = 1;
        this.lock = new ReentrantLock();
    }

    private void calculateNextFree() {
        while (map.containsKey(freeLoc))
            freeLoc++;
    }

    @Override
    public void add(Pair<Integer, List<Integer>> val) throws MyException {
        map.put(freeLoc, val);
        calculateNextFree();
    }

    @Override
    public Pair<Integer, List<Integer>> remove(int id) throws MyException {
        return map.remove(id);
    }

    @Override
    public boolean isDefined(int id) {
        return map.containsKey(id);
    }

    @Override
    public Pair<Integer, List<Integer>> lookUp(int id) {
        return map.get(id);
    }

    @Override
    public void update(int id, Pair<Integer, List<Integer>> val) throws MyException {
        map.replace(id, val);
    }

    @Override
    public Map<Integer, Pair<Integer, List<Integer>>> getContent() {
        return map;
    }

    @Override
    public void setContent(Map<Integer, Pair<Integer, List<Integer>>> heap) {
        map = heap;
        freeLoc = 1;
        calculateNextFree();
    }

    @Override
    public int getNextFree() {
        return freeLoc;
    }

    @Override
    public String toString() {
        return map.toString();
    }

    @Override
    public List<SemaphoreDTO> getDTOList() {
        List<SemaphoreDTO> list = new ArrayList<>();
        for (Integer key: map.keySet()) {
            list.add(new SemaphoreDTO(key, map.get(key).getKey(), map.get(key).getValue().toString()));
        }
        return list;
    }

    @Override
    public Lock getSemaphoreLock() {
        return this.lock;
    }
}
