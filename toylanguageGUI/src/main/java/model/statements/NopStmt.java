package model.statements;

import exceptions.MyException;
import model.PrgState;
import model.adt.MyIDictionary;
import model.types.Type;

public class NopStmt implements IStmt {

	@Override
	public PrgState execute(PrgState state) throws MyException {
		return null;
	}
	
	@Override
	public String toString() {
		return "Nop";
	}

	@Override
	public IStmt deepCopy() {
		return new NopStmt();
	}

	@Override
	public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
		return typeEnv;
	}
}
