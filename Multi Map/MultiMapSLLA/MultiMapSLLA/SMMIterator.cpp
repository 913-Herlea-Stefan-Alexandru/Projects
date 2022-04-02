#include "SMMIterator.h"
#include "SortedMultiMap.h"

SMMIterator::SMMIterator(const SortedMultiMap& d) : map(d){
	//TODO - Implementation
	//vector
	//this->mapPos = 0;
	this->pos = 0;

	//SLLA
	this->mapPos = this->map.head;
}

void SMMIterator::first(){
	//TODO - Implementation
	//vector
	//this->mapPos = 0;
	this->pos = 0;

	//SLLA
	this->mapPos = this->map.head;
}

void SMMIterator::next(){
	//TODO - Implementation
	if (!this->valid())
	{
		throw exception();
	}
	//vector
	this->pos++;
	//if (this->pos >= this->map.elems[this->mapPos].second->size())
	//{
	//	this->pos = 0;
	//	this->mapPos++;
	//}

	//SLLA
	if (this->pos >= this->map.elems[this->mapPos].second->size())
	{
		this->pos = 0;
		this->mapPos = this->map.next[mapPos];
	}
}

bool SMMIterator::valid() const{
	//TODO - Implementation
	//vector
	//if (this->mapPos < this->map.length)
	//	return true;
	//return false;

	//SLLA
	if (this->mapPos != -1)
		return true;
	return false;
}

TElem SMMIterator::getCurrent() const{
	//TODO - Implementation
	if (!this->valid())
	{
		throw exception();
	}
	//vector
	TElem elem;
	elem.first = this->map.elems[this->mapPos].first;
	elem.second = this->map.elems[this->mapPos].second->getByIndex(pos);
	return elem;

	//SLLA
}


