package model.statements;

import exceptions.MyException;
import model.PrgState;
import model.adt.IHeap;
import model.adt.MyIDictionary;
import model.adt.MyIStack;
import model.expressions.Exp;
import model.expressions.RelExpr;
import model.types.Type;
import model.values.Value;

public class SwitchStmt implements IStmt{

    private Exp exp, exp1, exp2;
    private IStmt stmt1, stmt2, stmt3;

    public SwitchStmt(Exp exp, Exp exp1, IStmt stmt1, Exp exp2, IStmt stmt2, IStmt stmt3) {
        this.exp = exp;
        this.exp1 = exp1;
        this.stmt1 = stmt1;
        this.exp2 = exp2;
        this.stmt2 = stmt2;
        this.stmt3 = stmt3;
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        MyIStack<IStmt> stk = state.getExeStack();
        MyIDictionary<String, Value> symTbl = state.getSymTable();
        IHeap<Value> heapTbl = state.getHeapTable();

        IStmt secondIf = new IfStmt(new RelExpr("==", exp, exp2),  stmt2,stmt3);
        IStmt firstIf = new IfStmt(new RelExpr("==", exp, exp1), stmt1, secondIf);

        stk.push(firstIf);

        return null;
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        Type e = exp.typecheck(typeEnv);
        Type e1 = exp1.typecheck(typeEnv);
        Type e2 = exp2.typecheck(typeEnv);
        if (e.equals(e1) && e.equals(e2)) {
            stmt1.typecheck(typeEnv.deepCopy());
            stmt2.typecheck(typeEnv.deepCopy());
            stmt3.typecheck(typeEnv.deepCopy());
            return typeEnv;
        }
        else
            throw new MyException("The types of the expressions must be the same!");
    }

    @Override
    public IStmt deepCopy() {
        return new SwitchStmt(this.exp.deepCopy(), this.exp1.deepCopy(), this.stmt1.deepCopy(), this.exp2.deepCopy(), this.stmt2.deepCopy(), this.stmt3.deepCopy());
    }

    @Override
    public String toString() {
        return "(switch(" + exp.toString() + ")\n" +
                "\tcase " + exp1.toString() + ": " + stmt1.toString() + "\n" +
                "\tcase " + exp2.toString() + ": " + stmt2.toString() + "\n" +
                "\tdefault: " + stmt3.toString() + "\n)";
    }
}
