package model.expressions;

import exceptions.MyException;
import model.adt.IHeap;
import model.adt.MyIDictionary;
import model.types.Type;
import model.values.Value;

public class VarExp implements Exp{
	private String id;
	
	public VarExp(String id) {
		this.id = id;
	}

	@Override
	public Value eval(MyIDictionary<String, Value> tbl, IHeap<Value> hp) throws MyException {
		return tbl.lookUp(id);
	}
	
	@Override
	public String toString() {
		return id;
	}

	@Override
	public Exp deepCopy() {
		return new VarExp(this.id);
	}

	@Override
	public Type typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
		return typeEnv.lookUp(id);
	}
}
