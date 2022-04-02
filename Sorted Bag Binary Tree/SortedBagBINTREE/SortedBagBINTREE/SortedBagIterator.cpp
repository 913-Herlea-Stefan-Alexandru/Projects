#include "SortedBagIterator.h"
#include "SortedBag.h"
#include <exception>

using namespace std;

SortedBagIterator::SortedBagIterator(const SortedBag& b) : bag(b) {
	//TODO - Implementation
	this->poz = this->bag.getMinimum();
}

TComp SortedBagIterator::getCurrent() {
	//TODO - Implementation
	if (!this->valid())
		throw exception();
	return this->bag.info[this->poz];
}

bool SortedBagIterator::valid() {
	//TODO - Implementation
	if (this->poz != -1)
		return true;
	return false;
}

void SortedBagIterator::next() {
	//TODO - Implementation
	if (!this->valid())
		throw exception();
	this->poz = this->bag.successor(this->poz);
}

void SortedBagIterator::first() {
	//TODO - Implementation
	this->poz = this->bag.getMinimum();
}

void SortedBagIterator::previous()
{
	if (!this->valid())
		throw exception();
	if (this->bag.left[this->poz] != -1)
	{
		int c = this->bag.left[this->poz];
		while (this->bag.right[c] != -1)
		{
			c = this->bag.right[c];
		}
		this->poz = c;
	}
	else
	{
		int c = this->poz;
		int p = this->bag.parent[this->poz];
		while (p != -1 && this->bag.right[p] != c)
		{
			c = p;
			p = this->bag.parent[p];
		}
		this->poz = p;
	}
	//this->poz = this->bag.predecessor(this->poz);
}

