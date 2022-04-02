package model.statements;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

import exceptions.MyException;
import model.PrgState;
import model.adt.IHeap;
import model.adt.MyIDictionary;
import model.expressions.Exp;
import model.types.StringType;
import model.types.Type;
import model.values.StringValue;
import model.values.Value;

public class CloseRFileStmt implements IStmt {

	private Exp exp;
	
	public CloseRFileStmt(Exp exp) {
		this.exp = exp;
	}
	
	@Override
	public PrgState execute(PrgState state) throws MyException {
		MyIDictionary<String, Value> symTbl = state.getSymTable();
		IHeap<Value> heapTbl = state.getHeapTable();
		MyIDictionary<StringValue, BufferedReader> fileTbl = state.getFileTable();
		Value val = exp.eval(symTbl, heapTbl);
		if (val.getType().equals(new StringType())) {
			StringValue strVal = (StringValue) val;
			if (fileTbl.isDefined(strVal)) {
				BufferedReader bf = fileTbl.lookUp(strVal);
				try {
					bf.close();
				} catch (IOException e) {
					throw new MyException(e.getMessage());
				}
				fileTbl.remove(strVal);
			}
			else
				throw new MyException("The file " + strVal + " is not oppen");
		}
		else {
			throw new MyException("The name of a file must be a StringType");
		}
		return null;
	}

	@Override
	public String toString() {
		return "closeRFile(" + exp.toString() + ")";
	}
	
	@Override
	public IStmt deepCopy() {
		return new CloseRFileStmt(this.exp.deepCopy());
	}

	@Override
	public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
		Type typexp = exp.typecheck(typeEnv);
		if (typexp.equals(new StringType())) {
			return typeEnv;
		}
		else
			throw new MyException("File name must be a string type");
	}

}
