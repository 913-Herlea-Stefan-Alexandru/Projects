package model.statements;

import exceptions.MyException;
import model.PrgState;
import model.adt.IHeap;
import model.adt.MyIDictionary;
import model.expressions.Exp;
import model.types.RefType;
import model.types.Type;
import model.values.RefValue;
import model.values.Value;

public class HeapWriteStmt implements IStmt {
	
	private String name;
	private Exp exp;

	public HeapWriteStmt(String name, Exp exp) {
		this.name = name;
		this.exp = exp;
	}
	
	@Override
	public PrgState execute(PrgState state) throws MyException {
		MyIDictionary<String, Value> symTbl = state.getSymTable();
		IHeap<Value> heapTbl = state.getHeapTable();
		if (symTbl.isDefined(name)) {
			Value val = symTbl.lookUp(name);
			if (val.getType() instanceof RefType) {
				RefValue v = (RefValue) val;
				int addr = v.getAddr();
				if (heapTbl.isDefined(addr)) {
					Value e = exp.eval(symTbl, heapTbl);
					heapTbl.update(addr, e);
				}
				else
					throw new MyException("The address of variable " + name + " cannot be accessed!");
			}
			else
				throw new MyException("Type of variable " + name + " must be RefType!");
		}
		else
			throw new MyException("The variable " + name + " is undefined!");
		return null;
	}
	
	@Override
	public String toString() {
		return "wH(" + name + "," + exp.toString() + ")";
	}

	@Override
	public IStmt deepCopy() {
		return new HeapWriteStmt(name, exp.deepCopy());
	}

	@Override
	public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
		Type typevar = typeEnv.lookUp(name);
		Type typexp = exp.typecheck(typeEnv);
		if (typevar.equals(new RefType(typexp)))
			return typeEnv;
		else 
			throw new MyException("NEW stmt: right hand side and left hand side have different types ");
	}

}
