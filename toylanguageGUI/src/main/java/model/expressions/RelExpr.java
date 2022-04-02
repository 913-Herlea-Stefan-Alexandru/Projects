package model.expressions;

import exceptions.MyException;
import model.adt.IHeap;
import model.adt.MyIDictionary;
import model.types.BoolType;
import model.types.IntType;
import model.types.Type;
import model.values.BoolValue;
import model.values.IntValue;
import model.values.Value;

public class RelExpr implements Exp {
	private Exp first;
	private Exp second;
	private String op;
	
	public RelExpr(String op, Exp first, Exp second) {
		this.first = first;
		this.second = second;
		this.op = op;
	}
	
	@Override
	public Value eval(MyIDictionary<String, Value> tbl, IHeap<Value> hp) throws MyException {
		Value v1,v2;                            
		v1 = first.eval(tbl, hp);
		if (v1.getType().equals(new IntType())) {
			v2 = second.eval(tbl, hp);
			if (v2.getType().equals(new IntType())) {
				int n1 = ((IntValue)v1).getValue();
				int n2 = ((IntValue)v2).getValue();
				switch (op) {
				case "==":
					return new BoolValue(n1 == n2);
				case "!=":
					return new BoolValue(n1 != n2);
				case ">=":
					return new BoolValue(n1 >= n2);
				case ">":
					return new BoolValue(n1 > n2);
				case "<=":
					return new BoolValue(n1 <= n2);
				case "<":
					return new BoolValue(n1 < n2);
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
	public Exp deepCopy() {
		return new RelExpr(this.op, this.first.deepCopy(), this.second.deepCopy());
	}
	
	@Override
	public String toString() {
		return this.first.toString() + this.op + this.second.toString();
	}

	@Override
	public Type typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
		Type typ1, typ2;                        
		typ1=first.typecheck(typeEnv);                        
		typ2=second.typecheck(typeEnv);
        if (typ1.equals(new IntType())) {
        	if (typ2.equals(new IntType())) {
        		return new BoolType();
        	} 
        	else      
        		throw new MyException("second operand is not an integer");
        } 
        else 
        	throw new MyException("first operand is not an integer");   
	}

}
