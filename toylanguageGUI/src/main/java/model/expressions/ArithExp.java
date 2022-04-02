package model.expressions;

import exceptions.MyException;
import model.adt.*;
import model.types.IntType;
import model.types.Type;
import model.values.IntValue;
import model.values.Value;

public class ArithExp implements Exp{
	
	private Exp first;
	private Exp second;
	private char op;
	
	public ArithExp(char op, Exp first, Exp second) {
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
				case '+':
					return new IntValue(n1 + n2);
				case '-':
					return new IntValue(n1 - n2);
				case '*':
					return new IntValue(n1 * n2);
				case '/':
					if (n2 == 0)
						throw new MyException("Division by 0!"); //DivisionBy0Exception()
					return new IntValue(n1 / n2);
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
		return  '(' + first.toString() + op + second.toString() + ')';
	}

	@Override
	public Exp deepCopy() {
		return new ArithExp(this.op, this.first.deepCopy(), this.second.deepCopy());
	}

	@Override
	public Type typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
		Type typ1, typ2;                        
		typ1=first.typecheck(typeEnv);                        
		typ2=second.typecheck(typeEnv);
        if (typ1.equals(new IntType())) {
        	if (typ2.equals(new IntType())) {
        		return new IntType();                                   
        	} 
        	else      
        		throw new MyException("second operand is not an integer");
        } 
        else 
        	throw new MyException("first operand is not an integer");           
    }

}
