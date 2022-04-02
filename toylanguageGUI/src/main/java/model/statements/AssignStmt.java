package model.statements;

import exceptions.MyException;
import model.PrgState;
import model.adt.IHeap;
import model.adt.MyIDictionary;
import model.expressions.Exp;
import model.types.Type;
import model.values.Value;

public class AssignStmt implements IStmt {

	private String id;
	private Exp exp;
	
	public AssignStmt(String id, Exp exp) {
		this.id = id;
		this.exp = exp;
	}
	
	@Override
	public PrgState execute(PrgState state) throws MyException {
		MyIDictionary<String, Value> symTbl = state.getSymTable();
		IHeap<Value> heapTbl = state.getHeapTable();
		if (symTbl.isDefined(id)) {
			Value val = exp.eval(symTbl, heapTbl);
			Type typId = (symTbl.lookUp(id)).getType();
			if ((val.getType()).equals(typId)) {
				symTbl.update(id, val);
			}
			else
				throw new MyException("Declared type of variable " + id + " and type of the assigned expression do not mach!");
			
		}
		else
			throw new MyException("The used variable " + id + " was not declared before!");
		state.setSymTable(symTbl);
		return null;
	}
	
	@Override
	public String toString() {
		return id + "=" + exp.toString();
	}

	@Override
	public IStmt deepCopy() {
		return new AssignStmt(this.id, this.exp.deepCopy());
	}

	@Override
	public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
		Type typevar = typeEnv.lookUp(id);
		Type typexp = exp.typecheck(typeEnv);                        
		if (typevar.equals(typexp))
			return typeEnv;
		else 
			throw new MyException("Assignment: right hand side and left hand side have different types ");
	}

}
