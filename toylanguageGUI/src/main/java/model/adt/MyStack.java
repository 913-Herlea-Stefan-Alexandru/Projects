package model.adt;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;
import exceptions.MyException;

public class MyStack<T> implements MyIStack<T>{
	
	private Stack<T> stack;
	
	public MyStack() {
		stack = new Stack<T>();
	}
	
	@Override
	public int size() {
		// TODO Auto-generated method stub
		return stack.size();
	}

	@Override
	public T pop() throws MyException {
		try {
			return stack.pop();
		}
		catch (Exception e) {
			throw new MyException("Stack is empty!");
		}
	}

	@Override
	public List<T> toList() {
		List<T> list = new ArrayList<>();
		while (!stack.isEmpty()) {
			T elem = stack.pop();
			list.add(elem);
		}

		for (int i = list.size(); i-- > 0; ) {
			stack.push(list.get(i));
		}

		return list;
	}

	@Override
	public void push(T val) {
		stack.push(val);
	}

	@Override
	public boolean isEmpty() {
		return stack.isEmpty();
	}
	
	@Override
	public String toString() {
		return stack.toString();
	}
}
