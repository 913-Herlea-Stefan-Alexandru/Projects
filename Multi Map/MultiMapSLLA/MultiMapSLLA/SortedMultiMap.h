#pragma once
//DO NOT INCLUDE SMMITERATOR

//DO NOT CHANGE THIS PART
#include <vector>
#include <utility>
typedef int TKey;
typedef int TValue;
typedef std::pair<TKey, TValue> TElem;
#define NULL_TVALUE -111111
#define NULL_TELEM pair<TKey, TValue>(-111111, -111111);
using namespace std;
class SLLA;
class SMMIterator;
typedef bool(*Relation)(TKey, TKey);

typedef std::pair<TKey, SLLA*> TE;

class SortedMultiMap {
	friend class SMMIterator;
    
    private:
		//TODO - Representation
        //vector
        //TE* elems;

        //SLLA
        TE* elems;
        int* next;
        int firstEmpty;
        int head;

        //both
        int cap;
        int length;
        Relation r;

        void expand();

    public:

    // constructor
    SortedMultiMap(Relation r);

	//adds a new key value pair to the sorted multi map
    void add(TKey c, TValue v);

	//returns the values belonging to a given key
    vector<TValue> search(TKey c) const;

	//removes a key value pair from the sorted multimap
	//returns true if the pair was removed (it was part of the multimap), false if nothing is removed
    bool remove(TKey c, TValue v);

    //returns the number of key-value pairs from the sorted multimap
    int size() const;

    //verifies if the sorted multi map is empty
    bool isEmpty() const;

    // returns an iterator for the sorted multimap. The iterator will returns the pairs as required by the relation (given to the constructor)	
    SMMIterator iterator() const;

    //modifies the values of those keys that are in smm to be equal to their value from smm 
    //returns the number of modified pairs 
    //BC
    //WC AC = O(n*m) -> we need to search through all elements and the search operation for the given smm has a complexity of O(m)
    int updateValues(SortedMultiMap& sm);

    // destructor
    ~SortedMultiMap();
};

class SLLA
{
private:
    TValue* elems;
    int* next;
    int cap;
    int head;
    int firstEmpty;
    int length;

    void expand();

public:
    SLLA();

    ~SLLA();

    void insertFirst(TValue val);

    bool deleteElem(TValue val);

    TValue getByIndex(int index);

    vector<TValue> toVect();

    int size();
};
