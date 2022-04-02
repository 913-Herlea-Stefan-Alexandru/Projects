package model.statements;

import exceptions.MyException;
import javafx.util.Pair;
import model.PrgState;
import model.adt.IHeap;
import model.adt.ISemaphoreTable;
import model.adt.MyIDictionary;
import model.expressions.Exp;
import model.types.IntType;
import model.types.Type;
import model.values.IntValue;
import model.values.Value;

import java.util.ArrayList;
import java.util.List;

public class CreateSemaphoreStmt implements IStmt{

    private String var;
    private Exp exp;

    public CreateSemaphoreStmt(String var, Exp exp) {
        this.var = var;
        this.exp = exp;
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        MyIDictionary<String, Value> symTbl = state.getSymTable();
        IHeap<Value> heapTbl = state.getHeapTable();
        ISemaphoreTable semaphoreTbl = state.getSemaphoreTable();
        Value val = exp.eval(symTbl, heapTbl);
        if (val.getType().equals(new IntType())) {
            IntValue intVal = (IntValue) val;
            if (symTbl.isDefined(var)) {
                Value varVal = symTbl.lookUp(var);
                if (varVal.getType().equals(new IntType())) {
                    semaphoreTbl.getSemaphoreLock().lock();
                    int addr = semaphoreTbl.getNextFree();
                    semaphoreTbl.add(new Pair<>(intVal.getValue(), new ArrayList<>()));
                    symTbl.update(var, new IntValue(addr));
                    semaphoreTbl.getSemaphoreLock().unlock();
                }
                else
                    throw new MyException("The variable " + var + " must be of type int!");
            }
            else
                throw new MyException("Variable " + var + " is not defined!");
        }
        else
            throw new MyException("The expression " + exp.toString() + " must bew of type int!");
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        Type v = typeEnv.lookUp(var);
        Type e = exp.typecheck(typeEnv);
        if (v.equals(new IntType())) {
            if (e.equals(new IntType())) {
                return typeEnv;
            }
            else
                throw new MyException("The expression " + exp.toString() + " must bew of type int!");
        }
        else
            throw new MyException("The variable " + var + " must be of type int!");
    }

    @Override
    public IStmt deepCopy() {
        return new CreateSemaphoreStmt(this.var, this.exp.deepCopy());
    }

    @Override
    public String toString() {
        return "createSemaphore(" + var + ", " + exp.toString() + ")";
    }
}
