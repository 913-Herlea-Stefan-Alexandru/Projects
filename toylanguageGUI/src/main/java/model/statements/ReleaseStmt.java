package model.statements;

import exceptions.MyException;
import javafx.util.Pair;
import model.PrgState;
import model.adt.IHeap;
import model.adt.ISemaphoreTable;
import model.adt.MyIDictionary;
import model.types.IntType;
import model.types.Type;
import model.values.IntValue;
import model.values.Value;

import java.util.List;

public class ReleaseStmt implements IStmt{

    private String var;

    public ReleaseStmt(String var) {
        this.var = var;
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
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
                    List<Integer> list = p.getValue();
                    System.out.println("In release");
                    if (list.contains(state.getStateId())) {
                        System.out.println("Deleting");
                        int ind = list.indexOf(state.getStateId());
                        System.out.println(ind);
                        list.remove(ind);
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
        return new ReleaseStmt(this.var);
    }

    @Override
    public String toString() {
        return "release(" + var + ")";
    }
}
