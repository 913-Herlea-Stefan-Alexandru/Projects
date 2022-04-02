package model.statements;

import exceptions.MyException;
import javafx.util.Pair;
import model.PrgState;
import model.adt.IHeap;
import model.adt.ISemaphoreTable;
import model.adt.MyIDictionary;
import model.adt.MyIStack;
import model.types.IntType;
import model.types.Type;
import model.values.IntValue;
import model.values.Value;

import java.util.List;

public class AcquireStmt implements IStmt{

    private String var;

    public AcquireStmt(String var) {
        this.var = var;
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        MyIStack<IStmt> stk = state.getExeStack();
        MyIDictionary<String, Value> symTbl = state.getSymTable();
        ISemaphoreTable semaphoreTbl = state.getSemaphoreTable();
        if (symTbl.isDefined(var)) {
            Value val = symTbl.lookUp(var);
            if (val.getType().equals(new IntType())) {
                IntValue intVal = (IntValue) val;
                int addr = intVal.getValue();
                semaphoreTbl.getSemaphoreLock().lock();
                if (semaphoreTbl.isDefined(addr)) {
                    Pair<Integer, List<Integer>> p = semaphoreTbl.lookUp(addr);
                    int count = p.getKey();
                    List<Integer> list = p.getValue();
                    if (count > list.size()) {
                        if (!list.contains(state.getStateId())) {
                            list.add(state.getStateId());
                        }
                    }
                    else {
                        stk.push(this);
                    }
                    semaphoreTbl.getSemaphoreLock().unlock();
                    return null;
                }
                else {
                    semaphoreTbl.getSemaphoreLock().unlock();
                    throw new MyException("The semaphore " + var + " is not defined!");
                }
            }
            else
                throw new MyException("The variable " + var + " must be of type int!");
        }
        else
            throw new MyException("Variable " + var + " is not defined!");
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        Type v = typeEnv.lookUp(var);
        if (v.equals(new IntType())) {
            return typeEnv;
        }
        else
            throw new MyException("The variable " + var + " must be of type int!");
    }

    @Override
    public IStmt deepCopy() {
        return new AcquireStmt(this.var);
    }

    @Override
    public String toString() {
        return "acquire(" + var + ")";
    }
}
