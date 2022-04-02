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

public class HeapAllocStmt implements IStmt {

	String name;
	Exp exp;
	
	public HeapAllocStmt(String name, Exp exp) {
		this.name = name;
		this.exp = exp;
	}
	
	@Override
	public PrgState execute(PrgState state) throws MyException {
		MyIDictionary<String, Value> symTbl = state.getSymTable();
		IHeap<Value> heapTbl = state.getHeapTable();
		if (symTbl.isDefined(name)) {
			Value var = symTbl.lookUp(name);
			if (var.getType() instanceof RefType) {
				RefValue v = (RefValue) var;
				Value e = exp.eval(symTbl, heapTbl);
				if (e.getType().equals(v.getLocationType())) {
					int addr = heapTbl.getNextFree();
					heapTbl.add(e);
					RefValue newVal = new RefValue(addr, v.getLocationType());
					symTbl.update(name, newVal);
				}
				else
					throw new MyException("Type of pointer not the same with the type of the expression!");
			}
			else
				throw new MyException("Variable type not a RefType!");
		}
		else
			throw new MyException("Variable not defined!");
		return null;
	}
	
	@Override
	public String toString() {
		return "new(" + name + "," + exp.toString() + ")";
	}

	@Override
	public IStmt deepCopy() {
		return new HeapAllocStmt(name, exp.deepCopy());
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
