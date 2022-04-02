package model.expressions;

import exceptions.MyException;
import model.adt.IHeap;
import model.adt.MyIDictionary;
import model.types.RefType;
import model.types.Type;
import model.values.RefValue;
import model.values.Value;

public class HeapReadExp implements Exp {

	private Exp exp;
	
	public HeapReadExp(Exp exp) {
		this.exp = exp;
	}
	
	@Override
	public Value eval(MyIDictionary<String, Value> tbl, IHeap<Value> hp) throws MyException {
		Value val = exp.eval(tbl, hp);
		if (val instanceof RefValue) {
			RefValue v = (RefValue) val;
			int addr = v.getAddr();
			if (hp.isDefined(addr)) {
				return hp.lookUp(addr);
			}
			else
				throw new MyException("The RefValue " + v.toString() + " is not defined!");
		}
		else
			throw new MyException("The expression " + exp.toString() + " is not a RefValue!");
	}
	
	@Override
	public String toString() {
		return "rH(" + exp.toString() + ")";
	}

	@Override
	public Exp deepCopy() {
		return new HeapReadExp(exp.deepCopy());
	}

	@Override
	public Type typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
		Type typ = exp.typecheck(typeEnv);
		if (typ instanceof RefType) {
			RefType reft = (RefType) typ;                                    
			return reft.getInner();                        
		} 
		else     
			throw new MyException("the rH argument is not a Ref Type"); 
	}

}
