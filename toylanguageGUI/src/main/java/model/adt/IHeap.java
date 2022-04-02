package model.adt;

import java.util.List;
import java.util.Map;

import exceptions.MyException;
import model.values.Value;

public interface IHeap<Val> {
	public void add(Val val) throws MyException;
	public Val remove(int id) throws MyException;
	public boolean isDefined(int id);
	public Val lookUp(int id);
	public void update(int id, Val val) throws MyException;
	public Map<Integer, Val> getContent();
	public void setContent(Map<Integer, Val> heap);
	public int getNextFree();
	List<DictionaryDTO<Integer, Val>> getDTOList();
}
