package model.values;

import model.types.Type;
import model.types.StringType;

public class StringValue implements Value {
	
	private String value;
	
	public StringValue(String value) {
		this.value = value;
	}
	
	public void setValue(String newVal) {
		this.value = newVal;
	}
	
	public String getValue() {
		return this.value;
	}
	
	@Override
	public boolean equals(Object another) {
		if (another instanceof StringValue) {
			StringValue stringVal = (StringValue)another;
			if (stringVal.getValue() == this.value)
				return true;
			return false;
		}
		return false;
	}
	
	@Override
	public Type getType() {
		return new StringType();
	}
	
	@Override
	public String toString() {
		return "\"" + this.value + "\"";
	}

	@Override
	public Value deepCopy() {
		return new StringValue(this.value);
	}

}
