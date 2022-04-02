package model.values;

import model.types.Type;
import model.Cloneable;

public interface Value extends Cloneable<Value>{
	Type  getType(); 
	Value deepCopy();
}
