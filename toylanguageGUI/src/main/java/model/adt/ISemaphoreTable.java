package model.adt;

import exceptions.MyException;
import javafx.util.Pair;

import java.util.List;
import java.util.Map;
import java.util.concurrent.locks.Lock;

public interface ISemaphoreTable {
    void add(Pair<Integer, List<Integer>> val) throws MyException;
    Pair<Integer, List<Integer>> remove(int id) throws MyException;
    boolean isDefined(int id);
    Pair<Integer, List<Integer>> lookUp(int id);
    void update(int id, Pair<Integer, List<Integer>> val) throws MyException;
    Map<Integer, Pair<Integer, List<Integer>>> getContent();
    void setContent(Map<Integer, Pair<Integer, List<Integer>>> heap);
    int getNextFree();
    Lock getSemaphoreLock();
    List<SemaphoreDTO> getDTOList();
}
