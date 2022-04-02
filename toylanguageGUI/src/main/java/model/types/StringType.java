package model.types;

import model.values.Value;
import model.values.StringValue;

public class StringType implements Type {

	public StringType() {
		
	}
	
	@Override
	public boolean equals(Object another) {
		if (another instanceof StringType) {
			return true;
		}
		else
			return false;
	}
	
	@Override
	public String toString() {
		return "string";
	}
	
	@Override
	public Value defaultValue() {
		return new StringValue("");
	}

	@Override
	public Type deepCopy() {
		return new StringType();
	}

}
