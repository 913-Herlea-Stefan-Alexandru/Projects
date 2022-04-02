package model.adt;

import java.util.LinkedList;
import exceptions.MyException;

public class MyList<T> implements MyIList<T> {
	
	private LinkedList<T> list;
	
	public MyList() {
		this.list = new LinkedList<T>();
	}
	
	@Override
	public int size() {
		return list.size();
	}

	@Override
	public T get(int poz) throws MyException {
		try {
			return list.get(poz);
		}
		catch (Exception e) {
			throw new MyException("Position index out of range!");
		}
	}

	@Override
	public void remove(int poz) throws MyException {
		try {
			list.remove(poz);
		}
		catch (Exception e) {
			throw new MyException("Position index out of range!");
		}
	}

	@Override
	public void add(T val, int poz) throws MyException {
		try {
			list.add(poz, val);
		}
		catch (Exception e) {
			throw new MyException("Position index out of range!");
		}
		
	}

	@Override
	public boolean isEmpty() {
		return list.isEmpty();
	}
	
	@Override
	public String toString() {
		return list.toString();
	}

}
