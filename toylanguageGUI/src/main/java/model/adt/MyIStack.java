package model.adt;

import exceptions.MyException;

import java.util.List;

public interface MyIStack<T> {
	int size();
	T pop() throws MyException;
	void push(T val);
	boolean isEmpty();
	List<T> toList();
}
