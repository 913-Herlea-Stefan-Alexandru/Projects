package model.adt;

import java.util.*;
import java.util.concurrent.ConcurrentHashMap;

import exceptions.MyException;
import model.Cloneable;

public class MyDictionary<T1, T2> implements MyIDictionary<T1, T2> {
	
	private Map<T1, T2> map;
	
	public MyDictionary(Map<T1, T2> map) {
		this.map = new ConcurrentHashMap<T1, T2>(map);
	}
	
	public MyDictionary() {
		map = new ConcurrentHashMap<T1, T2>();
	}
	
	@Override
	public void add(T1 key, T2 val) {
		try {
			map.put(key, val);
		}
		catch (Exception e) {
			throw new MyException("We cannot add null values to dictionary!");
		}
	}

	@Override
	public T2 remove(T1 key) throws MyException {
		try {
			return map.remove(key);
		}
		catch (Exception e) {
			throw new MyException("The specified key does not exist!");
		}
	}

	@Override
	public void update(T1 key, T2 val) throws MyException {
		try {
			map.replace(key, val);
		}
		catch (Exception e) {
			throw new MyException("The specified key does not exist!");
		}
	}

	@Override
	public T2 lookUp(T1 key) throws MyException {
		try {
			return map.get(key);
		}
		catch (Exception e) {
			throw new MyException("The specified key does not exist!");
		}
	}

	@Override
	public boolean isEmpty() {
		return map.isEmpty();
	}

	@Override
	public boolean isDefined(T1 key) {
		return map.containsKey(key);
	}

	@Override
	public Collection<T2> values(){
		return map.values();
	}
	
	@Override
	public String toString() {
		return map.toString();
	}

	@Override
	public Map<T1, T2> getContent() {
		return map;
	}

	public List<DictionaryDTO<T1, T2>> getDTOList() {
		List<DictionaryDTO<T1, T2>> list = new ArrayList<>();
		for (T1 key: map.keySet()) {
			list.add(new DictionaryDTO<>(key, map.get(key)));
		}
		return list;
	}

	@Override
	public MyDictionary<T1, T2> deepCopy() {
		Map<T1, T2> copy = new HashMap<T1, T2>();
		for (T1 k: map.keySet()) {
			if (map.get(k) instanceof Cloneable) {
				Cloneable<T2> v = (Cloneable<T2>) map.get(k);
				copy.put(k, v.deepCopy());
			}
			else 
				throw new MyException("Not a map of clonable objects");
		}
		return new MyDictionary<T1, T2>(copy);
	}
}
