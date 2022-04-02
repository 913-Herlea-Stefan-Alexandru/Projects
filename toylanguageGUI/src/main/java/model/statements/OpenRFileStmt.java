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

public class OpenRFileStmt implements IStmt {

	private Exp exp;
	
	public OpenRFileStmt(Exp exp) {
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
				throw new MyException("The file " + strVal + "is already open");
			}
			try {
				FileReader file = new FileReader(strVal.getValue());
				BufferedReader bf = new BufferedReader(file);
				fileTbl.add(strVal, bf);
			}
			catch (FileNotFoundException ex) {
				throw new MyException(ex.getMessage());
			}
			catch (IOException ex) {
				throw new MyException(ex.getMessage());
			}
		}
		else {
			throw new MyException("The name of a file must be a StringType");
		}
		return null;
	}
	
	@Override
	public String toString() {
		return "openRFile(" + exp.toString() + ")";
	}

	@Override
	public IStmt deepCopy() {
		// TODO Auto-generated method stub
		return new OpenRFileStmt(this.exp.deepCopy());
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
