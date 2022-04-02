package model.values;

import model.types.RefType;
import model.types.Type;

public class RefValue implements Value {
	
	private int address;
	private Type locationType;
	
	public RefValue(int address, Type locationType) {
		this.address = address;
		this.locationType = locationType;
	}
	
	public int getAddr() {
		return address;
	}
	
	public Type getLocationType() {
		return this.locationType;
	}
	
	@Override
	public Type getType() {
		return new RefType(locationType);
	}
	
	@Override
	public boolean equals(Object another) {
		if (another instanceof RefValue) {
			RefValue intVal = (RefValue)another;
			if (intVal.getAddr() == this.address)
				return true;
			return false;
		}
		return false;
	}
	
	@Override
	public String toString() {
		return "(" + address + "," + locationType + ")";
	}

	@Override
	public Value deepCopy() {
		return new RefValue(address, locationType);
	}

}
