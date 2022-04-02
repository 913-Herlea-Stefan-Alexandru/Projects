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

public class IfStmt implements IStmt {

	private Exp exp;
	private IStmt thenS;
	private IStmt elseS;
	
	public IfStmt(Exp exp, IStmt thenS, IStmt elseS) {
		this.exp = exp;
		this.thenS = thenS;
		this.elseS = elseS;
	}
	
	@Override
	public PrgState execute(PrgState state) throws MyException {
		MyIStack<IStmt> stk = state.getExeStack();
		MyIDictionary<String, Value> symTbl = state.getSymTable();
		IHeap<Value> heapTbl = state.getHeapTable();
		Value val = exp.eval(symTbl, heapTbl);
		if (val.getType().equals(new BoolType())) {
			BoolValue boolVal = (BoolValue) val;
			if (boolVal.getValue())
				stk.push(thenS);
			else
				stk.push(elseS);
		}
		else
			throw new MyException("The expression inside an if clause must be a BoolType");
		return null;
	}
	
	@Override
	public String toString() {
		return "if(" + exp.toString() + ") then (" + thenS.toString() + ") else (" + elseS.toString() + ")";
	}

	@Override
	public IStmt deepCopy() {
		return new IfStmt(this.exp.deepCopy(), this.thenS.deepCopy(), this.elseS.deepCopy());
	}

	@Override
	public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
		Type typexp = exp.typecheck(typeEnv);
		if (typexp.equals(new BoolType())) {
			thenS.typecheck(typeEnv.deepCopy());
			elseS.typecheck(typeEnv.deepCopy());
			return typeEnv;
		} 
		else
			throw new MyException("The condition of IF does not have the type bool"); 
	}

}
