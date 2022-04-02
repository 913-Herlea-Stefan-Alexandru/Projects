package model.expressions;

import exceptions.MyException;
import model.types.IntType;
import model.types.Type;
import model.values.IntValue;
import model.values.Value;

import exceptions.MyException;
import model.adt.*;
import model.types.BoolType;
import model.values.BoolValue;
import model.values.Value;

public class LogicExp implements Exp{
	private Exp first;
	private Exp second;
	private int op;
	
	public LogicExp(Exp first, Exp second, int op) {
		this.first = first;
		this.second = second;
		this.op = op;
	}
	
	@Override
	public Value eval(MyIDictionary<String, Value> tbl, IHeap<Value> hp) throws MyException {
		Value v1,v2;                            
		v1 = first.eval(tbl, hp);
		if (v1.getType().equals(new BoolType())) {
			v2 = second.eval(tbl, hp);
			if (v2.getType().equals(new BoolType())) {
				boolean n1 = ((BoolValue)v1).getValue();
				boolean n2 = ((BoolValue)v2).getValue();
				switch (op) {
				case 1:
					return new BoolValue(n1 && n2);
				case 2:
					return new BoolValue(n1 || n2);
				default:
					throw new MyException("Wrong operation!");
				}
			}
			else 
				throw new MyException("The second operator is not an integer!");
		}
		else 
			throw new MyException("The first operator is not an integer!");
	}
	
	@Override
	public String toString() {
		String oper = "";
		switch (op) {
		case 1:
			oper = "AND";
		case 2:
			oper = "OR";
		}
		return first.toString() + oper + second.toString();
	}

	@Override
	public Exp deepCopy() {
		return new LogicExp(this.first.deepCopy(), this.second.deepCopy(), this.op);
	}

	@Override
	public Type typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
		Type typ1, typ2;                        
		typ1=first.typecheck(typeEnv);                        
		typ2=second.typecheck(typeEnv);
        if (typ1.equals(new BoolType())) {
        	if (typ2.equals(new BoolType())) {
        		return new BoolType();                                   
        	} 
        	else      
        		throw new MyException("second operand is not a boolean");
        } 
        else 
        	throw new MyException("first operand is not a boolean");   
	}
}
