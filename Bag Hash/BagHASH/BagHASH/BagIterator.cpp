#include <exception>
#include "BagIterator.h"
#include "Bag.h"

using namespace std;


BagIterator::BagIterator(Bag& c): bag(c)
{
	//TODO - Implementation
	this->pos = 0;
	if (this->bag.nrOfElems == 0)
	{
		this->pos = this->bag.m;
		return;
	}
	for (int i = 0; i < this->bag.m; i++)
	{
		if (this->bag.elems[i] != NULL_TELEM && this->bag.elems[i] != DELETED_TELEM)
		{
			this->pos = i;
			return;
		}
	}
}

void BagIterator::first() {
	//TODO - Implementation
	this->pos = 0;
	if (this->bag.nrOfElems == 0)
	{
		this->pos = this->bag.m;
		return;
	}
	for (int i = 0; i < this->bag.m; i++)
	{
		if (this->bag.elems[i] != NULL_TELEM && this->bag.elems[i] != DELETED_TELEM)
		{
			this->pos = i;
			break;
		}
	}
}


void BagIterator::next() {
	//TODO - Implementation
	if (!this->valid())
	{
		throw exception();
	}
	this->pos++;
	while (this->pos < this->bag.m && (this->bag.elems[this->pos] == NULL_TELEM || this->bag.elems[this->pos] == DELETED_TELEM))
	{
		this->pos++;
	}
}


bool BagIterator::valid() const {
	//TODO - Implementation
	if (this->pos >= this->bag.m)
	{
		return false;
	}
	return true;
}

TElem BagIterator::remove()
{
	if (!this->valid())
	{
		throw exception();
	}
	TElem elem = this->getCurrent();
	this->bag.elems[this->pos] = DELETED_TELEM;
	return elem;
}

TElem BagIterator::getCurrent() const
{
	//TODO - Implementation
	if (!this->valid())
	{
		throw exception();
	}
	return this->bag.elems[this->pos];
}
