package model;

import java.io.BufferedReader;
import java.util.List;

import exceptions.MyException;
import javafx.util.Pair;
import model.adt.*;
import model.statements.IStmt;
import model.values.StringValue;
import model.values.Value;

public class PrgState {

	private MyIStack<IStmt> exeStack;
	private MyIDictionary<String, Value> symTable;
	private MyIList<Value> out;
	private MyIDictionary<StringValue, BufferedReader> fileTable;
	private IHeap<Value> heapTable;
	private ISemaphoreTable semaphoreTable;
	private int stateId;
	public static int id;
	
	private IStmt originalProgram;
	
	public PrgState(MyIStack<IStmt> stk, MyIDictionary<String, Value> symtbl, MyIList<Value> ot, IStmt prg) {
		setExeStack(stk);
		setSymTable(symtbl);
		setOut(ot);
		stk.push(prg);
		this.originalProgram = prg.deepCopy();
		stateId = getNewProgramStateID();
	}
	
	public PrgState(MyIStack<IStmt> stk, MyIDictionary<String, Value> symtbl, MyIList<Value> ot ,MyIDictionary<StringValue, BufferedReader> filetbl, IStmt prg) {
		setExeStack(stk);
		setSymTable(symtbl);
		setOut(ot);
		setFileTable(filetbl);
		stk.push(prg);
		this.originalProgram = prg.deepCopy();
		stateId = getNewProgramStateID();
	}
	
	public PrgState(MyIStack<IStmt> stk, MyIDictionary<String, Value> symtbl, MyIList<Value> ot ,MyIDictionary<StringValue, BufferedReader> filetbl, IHeap<Value> heapTable, IStmt prg) {
		setExeStack(stk);
		setSymTable(symtbl);
		setOut(ot);
		setFileTable(filetbl);
		setHeapTable(heapTable);
		stk.push(prg);
		this.originalProgram = prg.deepCopy();
		stateId = getNewProgramStateID();
	}

	public PrgState(MyIStack<IStmt> stk, MyIDictionary<String, Value> symtbl, MyIList<Value> ot ,MyIDictionary<StringValue, BufferedReader> filetbl, IHeap<Value> heapTable, ISemaphoreTable semaphoreTable, IStmt prg) {
		setExeStack(stk);
		setSymTable(symtbl);
		setOut(ot);
		setFileTable(filetbl);
		setHeapTable(heapTable);
		setSemaphoreTable(semaphoreTable);
		stk.push(prg);
		this.originalProgram = prg.deepCopy();
		stateId = getNewProgramStateID();
	}
	
	public int getStateId() {
		return stateId;
	}
	
	public synchronized int getNewProgramStateID() {
        ++id;
        return id;
    }

	public MyIStack<IStmt> getExeStack() {
		return exeStack;
	}

	public void setExeStack(MyIStack<IStmt> exeStack) {
		this.exeStack = exeStack;
	}

	public MyIDictionary<String, Value> getSymTable() {
		return symTable;
	}

	public void setSymTable(MyIDictionary<String, Value> symTable) {
		this.symTable = symTable;
	}

	public MyIList<Value> getOut() {
		return out;
	}

	public void setOut(MyIList<Value> out) {
		this.out = out;
	}
	
	public MyIDictionary<StringValue, BufferedReader> getFileTable() {
		return fileTable;
	}

	public void setFileTable(MyIDictionary<StringValue, BufferedReader> fileTable) {
		this.fileTable = fileTable;
	}
	
	public IHeap<Value> getHeapTable() {
		return this.heapTable;
	}
	
	public void setHeapTable(IHeap<Value> heapTable) {
		this.heapTable = heapTable;
	}

	public ISemaphoreTable getSemaphoreTable() {
		return semaphoreTable;
	}

	public void setSemaphoreTable(ISemaphoreTable semaphoreTable) {
		this.semaphoreTable = semaphoreTable;
	}


	public Boolean isNotCompleted() {
		return !this.exeStack.isEmpty();
	}
	
	public PrgState oneStep() throws MyException{   
		if(exeStack.isEmpty()) 
			throw new MyException("prgstate stack is empty");
		IStmt  crtStmt = exeStack.pop();
		return crtStmt.execute(this);
	}
	
	@Override
	public String toString() {
		return  "Id: " + stateId + '\n' +
				"Exe stack: \n" + 
				this.exeStack.toString() + "\n" + 
				"Symbol table: \n" +
				this.symTable.toString() + "\n" + 
				"Out: \n" +
				this.out.toString() + "\n" + 
				"File table: \n" +
				this.fileTable.toString() + "\n" + 
				"Heap table: \n" + 
				this.heapTable.toString() + "\n" +
				"Semaphore table: \n" +
				this.semaphoreTable.toString() + "\n";
	}
}
