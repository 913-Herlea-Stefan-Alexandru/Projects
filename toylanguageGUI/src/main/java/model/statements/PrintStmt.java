package model.statements;

import exceptions.MyException;
import model.PrgState;
import model.adt.IHeap;
import model.adt.MyIDictionary;
import model.adt.MyIList;
import model.expressions.Exp;
import model.types.Type;
import model.values.Value;

public class PrintStmt implements IStmt {

	private Exp exp;
	
	public PrintStmt(Exp exp) {
		this.exp = exp;
	}
	
	@Override
	public PrgState execute(PrgState state) throws MyException {
		MyIList<Value> out = state.getOut();
		MyIDictionary<String, Value> symTbl = state.getSymTable(); 
		IHeap<Value> heapTbl = state.getHeapTable();
		out.add(exp.eval(symTbl, heapTbl), out.size());
		return null;
	}
	
	@Override
	public String toString() {
		return "print(" + exp.toString() + ")";
	}

	@Override
	public IStmt deepCopy() {
		return new PrintStmt(this.exp.deepCopy());
	}

	@Override
	public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
		exp.typecheck(typeEnv);                        
		return typeEnv;
	}

}
