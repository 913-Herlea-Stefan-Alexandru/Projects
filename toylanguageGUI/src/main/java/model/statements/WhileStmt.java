package model.statements;

import exceptions.MyException;
import model.PrgState;
import model.adt.IHeap;
import model.adt.MyIDictionary;
import model.adt.MyIStack;
import model.expressions.Exp;
import model.types.BoolType;
import model.types.Type;
import model.values.BoolValue;
import model.values.Value;

public class WhileStmt implements IStmt {

	private Exp exp;
	private IStmt stmt;
	
	public WhileStmt(Exp exp, IStmt stmt) {
		this.exp = exp;
		this.stmt = stmt;
	}
	
	@Override
	public PrgState execute(PrgState state) throws MyException {
		MyIStack<IStmt> stk = state.getExeStack();
		MyIDictionary<String, Value> symTbl = state.getSymTable();
		IHeap<Value> heapTbl = state.getHeapTable();
		Value val = exp.eval(symTbl, heapTbl);
		if (val.getType().equals(new BoolType())) {
			BoolValue v = (BoolValue) val;
			if (v.getValue()) {
				stk.push(this);
				stk.push(stmt);
			}
		}
		else
			throw new MyException("Expression in while statement should be of BoolType!");
		return null;
	}
	
	@Override
	public String toString() {
		return "while(" + exp.toString() + ") (" + stmt.toString() + ")";
	}

	@Override
	public IStmt deepCopy() {
		return new WhileStmt(exp.deepCopy(), stmt.deepCopy());
	}

	@Override
	public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
		Type typexp = exp.typecheck(typeEnv);
		if (typexp.equals(new BoolType())) {
			stmt.typecheck(typeEnv.deepCopy());
			return typeEnv;
		} 
		else
			throw new MyException("The condition of IF does not have the type bool"); 
	}

}
