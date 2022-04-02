package model.adt;

import java.util.Collection;
import java.util.List;
import java.util.Map;

import exceptions.MyException;
import model.values.Value;
import model.Cloneable;

public interface MyIDictionary<T1, T2> extends Cloneable<MyIDictionary<T1, T2>>{
	void add(T1 key, T2 val) throws MyException;
	T2 remove(T1 key) throws MyException;
	void update(T1 key, T2 val) throws MyException;
	T2 lookUp(T1 key) throws MyException;
	boolean isEmpty();
	//True if the key is in dictionary
	boolean isDefined(T1 key);
	Collection<T2> values();
	Map<T1, T2> getContent();
	List<DictionaryDTO<T1, T2>> getDTOList();
}
