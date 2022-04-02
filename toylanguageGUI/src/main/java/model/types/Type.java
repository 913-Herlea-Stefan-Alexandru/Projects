package model.types;

import model.values.Value;
import model.Cloneable;

public interface Type extends Cloneable<Type>{
	public Value defaultValue();
	Type deepCopy();
}
