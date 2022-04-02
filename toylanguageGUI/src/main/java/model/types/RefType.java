package model.types;

import model.values.RefValue;
import model.values.Value;

public class RefType implements Type {

	private Type inner;
	
	public RefType(Type inner) {
		this.inner = inner;
	}
	
	public Type getInner() {
		return this.inner;
	}
	
	@Override
	public boolean equals(Object another) {
		if (another instanceof RefType)
		{
			RefType oth = (RefType) another;
			return inner.equals(oth.getInner());
		}
		else
			return false;
	}
	
	@Override
	public String toString() {
		return "Ref(" + inner.toString() + ")";
	}
	
	@Override
	public Value defaultValue() {
		return new RefValue(0, inner);
	}

	@Override
	public Type deepCopy() {
		return new RefType(inner.deepCopy());
	}

}
