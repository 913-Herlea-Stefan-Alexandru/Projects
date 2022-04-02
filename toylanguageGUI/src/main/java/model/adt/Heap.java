package model.adt;

import java.util.*;

import exceptions.MyException;
import model.values.Value;

public class Heap<Val> implements IHeap<Val> {
	
	private Map<Integer, Val> map;
	private int freeLoc;
	
	public Heap() {
		this.map = new HashMap<Integer, Val>();
		this.freeLoc = 1;
	}
	
	private void calculateNextFree() {
		while (map.containsKey(freeLoc))
			freeLoc++;
	}
	
	@Override
	public void add(Val val) throws MyException {
		map.put(freeLoc, val);
		calculateNextFree();
	}

	@Override
	public Val remove(int id) throws MyException {
		return map.remove(id);
	}

	@Override
	public boolean isDefined(int id) {
		return map.containsKey(id);
	}

	@Override
	public Val lookUp(int id) {
		return map.get(id);
	}

	@Override
	public void update(int id, Val val) throws MyException {
		map.replace(id, val);
	}

	@Override
	public Map<Integer, Val> getContent() {
		return map;
	}

	@Override
	public void setContent(Map<Integer, Val> heap) {
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
	public List<DictionaryDTO<Integer, Val>> getDTOList() {
		List<DictionaryDTO<Integer, Val>> list = new ArrayList<>();
		for (Integer key: map.keySet()) {
			list.add(new DictionaryDTO<>(key, map.get(key)));
		}
		return list;
	}

}
