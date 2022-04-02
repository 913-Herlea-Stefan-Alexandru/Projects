package model.statements;

import exceptions.MyException;
import model.PrgState;
import model.adt.IHeap;
import model.adt.MyIDictionary;
import model.types.Type;
import model.values.Value;

public class VarDeclStmt implements IStmt {

	private String name;
	private Type typ;
	
	public VarDeclStmt(String name, Type typ) {
		this.name = name;
		this.typ = typ;
	}
	
	@Override
	public PrgState execute(PrgState state) throws MyException {
		MyIDictionary<String, Value> symTbl = state.getSymTable();
		if (symTbl.isDefined(name)) 
			throw new MyException("The variable " + name + " is already defined!");
		
		symTbl.add(name, typ.defaultValue());
		
		return null;
	}
	
	@Override
	public String toString() {
		return typ.toString() + " " + name;
	}

	@Override
	public IStmt deepCopy() {
		return new VarDeclStmt(this.name, this.typ);
	}

	@Override
	public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
		typeEnv.add(name,typ);
		return typeEnv;
	}

}
