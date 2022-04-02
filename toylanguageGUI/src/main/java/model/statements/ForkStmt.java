package model.statements;

import exceptions.MyException;
import model.PrgState;
import model.adt.MyIDictionary;
import model.adt.MyStack;
import model.types.Type;

public class ForkStmt implements IStmt {

	private IStmt stmt;
	
	public ForkStmt(IStmt stmt) {
		this.stmt = stmt;
	}
	
	@Override
	public PrgState execute(PrgState state) throws MyException {
		PrgState newPrg = new PrgState(new MyStack<IStmt>(), state.getSymTable().deepCopy(), state.getOut(), state.getFileTable(), state.getHeapTable(), state.getSemaphoreTable(), stmt);
		return newPrg;
	}

	@Override
	public IStmt deepCopy() {
		return new ForkStmt(stmt.deepCopy());
	}
	
	@Override
	public String toString() {
		return "fork(" + stmt.toString() + ")";
	}

	@Override
	public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
		return stmt.typecheck(typeEnv);
	}

}
