package model.statements;

import exceptions.MyException;
import model.PrgState;
import model.adt.MyIDictionary;
import model.types.Type;
import model.Cloneable;

public interface IStmt extends Cloneable<IStmt>{
	PrgState execute(PrgState state) throws MyException;
	MyIDictionary<String,Type> typecheck(MyIDictionary<String,Type> typeEnv) throws MyException;
	IStmt deepCopy();
}
