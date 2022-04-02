#include "SMIterator.h"
#include "SortedMap.h"
#include <exception>

using namespace std;

SMIterator::SMIterator(const SortedMap& m) : map(m){
	//TODO - Implementation
	this->poz = 0;
}

void SMIterator::first(){
	//TODO - Implementation
	this->poz = 0;
}

void SMIterator::next(){
	//TODO - Implementation
	if (this->poz < this->map.nr_of_elem)
	{
		this->poz++;
	}
	else
	{
		throw exception();
	}
}

bool SMIterator::valid() const{
	//TODO - Implementation
	if (this->poz >= this->map.nr_of_elem || this->map.isEmpty())
	{
		return false;
	}
	return true;
}

TElem SMIterator::getCurrent() const{
	//TODO - Implementation
	if (!this->valid())
	{
		throw exception();
	}
	return this->map.arr[poz];
}


