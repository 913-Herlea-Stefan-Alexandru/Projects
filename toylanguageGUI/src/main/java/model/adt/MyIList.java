package model.adt;

import exceptions.MyException;

public interface MyIList<T> {
	int size();
	T get(int poz) throws MyException;
	void remove(int poz) throws MyException;
	void add(T val, int poz) throws MyException;
	boolean isEmpty();
}
