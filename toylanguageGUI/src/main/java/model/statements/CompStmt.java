package model.statements;

import exceptions.MyException;
import model.PrgState;
import model.adt.MyIDictionary;
import model.adt.MyIStack;
import model.types.Type;

public class CompStmt implements IStmt {

	private IStmt first;
	private IStmt second;
	
	public CompStmt(IStmt first, IStmt second) {
		this.first = first;
		this.second = second;
	}
	
	@Override
	public PrgState execute(PrgState state) throws MyException {
		MyIStack<IStmt> stk = state.getExeStack();
		stk.push(second);
		stk.push(first);
		state.setExeStack(stk);
		return null;
	}
	
	@Override
	public String toString() {
		return first.toString() + "\n" + second.toString();
	}

	@Override
	public IStmt deepCopy() {
		return new CompStmt(this.first.deepCopy(), this.second.deepCopy());
	}

	@Override
	public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
		return second.typecheck(first.typecheck(typeEnv));
	}

}
