package model.statements;

import java.io.BufferedReader;
import java.io.IOException;

import exceptions.MyException;
import model.PrgState;
import model.adt.IHeap;
import model.adt.MyIDictionary;
import model.expressions.Exp;
import model.types.IntType;
import model.types.StringType;
import model.types.Type;
import model.values.IntValue;
import model.values.StringValue;
import model.values.Value;

public class ReadFileStmt implements IStmt {

	private Exp exp;
	private String var;
	
	public ReadFileStmt(Exp exp, String var) {
		this.exp = exp;
		this.var = var;
	}
	
	@Override
	public PrgState execute(PrgState state) throws MyException {
		MyIDictionary<String, Value> symTbl = state.getSymTable();
		IHeap<Value> heapTbl = state.getHeapTable();
		MyIDictionary<StringValue, BufferedReader> fileTbl = state.getFileTable();
		if (symTbl.isDefined(var)) {
			Value val = symTbl.lookUp(var);
			if (val.getType().equals(new IntType())) {
				val = exp.eval(symTbl, heapTbl);
				if (val.getType().equals(new StringType())) {
					StringValue strVal = (StringValue) val;
					if (fileTbl.isDefined(strVal)) {
						BufferedReader bf = fileTbl.lookUp(strVal);
						try {
							String line = bf.readLine();
							IntValue intVal;
							if (line == null || line.isEmpty() || line.isBlank()) {
								intVal = new IntValue(0);
							}
							else {
								intVal = new IntValue(Integer.parseInt(line));
							}
							symTbl.update(var, intVal);
						} catch (IOException e) {
							throw new MyException(e.getMessage());
						}
					}
					else
						throw new MyException("The file " + strVal + " was not oppened");
				}
				else
					throw new MyException("The name of the file must be a StringType");
			}
			else
				throw new MyException("Variable " + var + " must be of IntType");
		}
		else
			throw new MyException("The variable " + var + " is not defined");
		return null;
	}
	
	@Override
	public String toString() {
		return "readFile(" + exp.toString() + ", " + var + ")";
	}

	@Override
	public IStmt deepCopy() {
		return new ReadFileStmt(this.exp.deepCopy(), this.var);
	}

	@Override
	public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
		Type typevar = typeEnv.lookUp(var);
		Type typexp = exp.typecheck(typeEnv);
		if (typevar.equals(new IntType()) && typexp.equals(new StringType()))
			return typeEnv;
		else 
			throw new MyException("Invalid types");  
		
	}

}
