#pragma once
#include <utility>
//DO NOT INCLUDE MAPITERATOR


//DO NOT CHANGE THIS PART
typedef int TKey;
typedef int TValue;
typedef std::pair<TKey, TValue> TElem;
#define NULL_TVALUE -111111
#define NULL_TELEM std::pair<TKey, TValue>(-111111, -111111)
class MapIterator;


class Map {
	//DO NOT CHANGE THIS PART
	friend class MapIterator;

	private:
		//TODO - Representation
		TElem* arr;
		int nr_of_elem;
		int allocated_size;

		void expand();

		void reduce();

	public:

	// implicit constructor
	Map();

	// adds a pair (key,value) to the map
	//if the key already exists in the map, then the value associated to the key is replaced by the new value and the old value is returned
	//if the key does not exist, a new pair is added and the value null is returned
	//BC=Theta(1), WC=Theta(n), AC=O(n)
	TValue add(TKey c, TValue v);

	//searches for the key and returns the value associated with the key if the map contains the key or null: NULL_TVALUE otherwise
	//BC=Theta(1), WC=Theta(n), AC=O(n)
	TValue search(TKey c) const;

	//removes a key from the map and returns the value associated with the key if the key existed or null: NULL_TVALUE otherwise
	//BC=Theta(1), WC=Theta(n), AC=O(n)
	TValue remove(TKey c);

	//returns the number of pairs (key,value) from the map
	//BC=WC=AC=Theta(1)
	int size() const;

	//checks whether the map is empty or not
	//BC=WC=AC=Theta(1)
	bool isEmpty() const;

	//returns the difference between the maximum and the minimum value (assume integer values) 
	//if the Map is empty or there is only one element in it the range is -1 
	//BC=Theta(1) -> when there are no elements inside the map or there is only one element
	//WC=Theta(n) -> when there are 2 or more elements inside the map
	//AC=O(n)
	int getValueRange() const;

	//returns an iterator for the map
	MapIterator iterator() const;

	// destructor
	~Map();

};



