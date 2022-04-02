package model.values;

import model.types.*;

public class IntValue implements Value{
	private int value;
	
	public IntValue(int value) {
		this.value = value;
	}
	
	public void setValue(int newVal) {
		this.value = newVal;
	}
	
	public int getValue() {
		return this.value;
	}
	
	public Type getType() {
		return new IntType();
	}
	
	@Override
	public boolean equals(Object another) {
		if (another instanceof IntValue) {
			IntValue intVal = (IntValue)another;
			if (intVal.getValue() == this.value)
				return true;
			return false;
		}
		return false;
	}
	
	@Override
	public String toString() {
		return "" + value;
	}

	@Override
	public Value deepCopy() {
		return new IntValue(this.value);
	}
}
