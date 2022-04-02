package model.expressions;
import model.values.Value;
import exceptions.MyException;
import model.adt.IHeap;
import model.adt.MyIDictionary;
import model.types.Type;

public class ValExp implements Exp{
	private Value e;
	
	public ValExp(Value e) {
		this.e = e;
	}
	
	@Override
	public Value eval(MyIDictionary<String,Value> tbl, IHeap<Value> hp) throws MyException {
		return e;
	}
	
	@Override
	public String toString() {
		return e.toString();
	}

	@Override
	public Exp deepCopy() {
		return new ValExp(this.e.deepCopy());
	}

	@Override
	public Type typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
		return e.getType();
	}
}
