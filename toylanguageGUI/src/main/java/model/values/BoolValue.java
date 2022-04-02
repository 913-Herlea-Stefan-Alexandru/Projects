package model.values;

import model.types.*;

public class BoolValue implements Value {
	private boolean value;
	
	public BoolValue(boolean value) {
		this.value = value;
	}
	
	public void setValue(boolean newVal) {
		this.value = newVal;
	}
	
	public boolean getValue() {
		return this.value;
	}
	
	public Type getType() {
		return new BoolType();
	}
	
	@Override
	public boolean equals(Object another) {
		if (another instanceof BoolValue) {
			BoolValue boolVal = (BoolValue)another;
			if (boolVal.getValue() == this.value)
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
		return new BoolValue(this.value);
	}
}
