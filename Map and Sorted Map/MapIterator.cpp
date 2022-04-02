#include "Map.h"
#include "MapIterator.h"
#include <exception>
using namespace std;


MapIterator::MapIterator(const Map& d) : map(d)
{
	//TODO - Implementation
	this->poz = 0;
}


void MapIterator::first() {
	//TODO - Implementation
	this->poz = 0;
}


void MapIterator::next() {
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


TElem MapIterator::getCurrent(){
	//TODO - Implementation
	if (!this->valid())
	{
		throw exception();
	}
	return this->map.arr[poz];
}


bool MapIterator::valid() const {
	//TODO - Implementation
	if (this->poz >= this->map.nr_of_elem || this->map.isEmpty())
	{
		return false;
	}
	return true;
}



