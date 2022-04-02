package model.expressions;

import exceptions.MyException;
import model.adt.*;
import model.values.Value;
import model.types.Type;
import model.Cloneable;

public interface Exp extends Cloneable<Exp> {
	Value eval(MyIDictionary<String,Value> tbl, IHeap<Value> hp) throws MyException;
	Type typecheck(MyIDictionary<String,Type> typeEnv) throws MyException;
	String toString();
	Exp deepCopy();
}