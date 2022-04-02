package model.types;

import model.values.*;

public class IntType implements Type{
	
	public IntType() {
	}
	
	@Override
	public boolean equals(Object another) {
		if (another instanceof IntType) {
			return true;
		}
		else
			return false;
	}
	
	@Override
	public String toString() {
		return "int";
	}

	@Override
	public Value defaultValue() {
		return new IntValue(0);
	}

	@Override
	public Type deepCopy() {
		return new IntType();
	}
	
}
