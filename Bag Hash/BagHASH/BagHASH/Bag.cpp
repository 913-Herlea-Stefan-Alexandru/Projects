#include "Bag.h"
#include "BagIterator.h"
#include <exception>
#include <iostream>
#include <math.h>
using namespace std;


int Bag::h1(TElem e) const
{
	return abs(e) % this->m;
}

int Bag::h2(TElem e) const
{
	return 1 + (abs(e) % (this->m - 1));
}

int Bag::h(TElem e, int i) const
{
	return (this->h1(e) + i * this->h2(e)) % this->m;
}

bool Bag::prime(int n)
{
	for (int d = 2; d < n / 2; d++)
	{
		if (n % d == 0)
		{
			return false;
		}
	}
	return true;
}

void Bag::resize()
{
	int old_m = this->m;
	this->m *= 2;
	while (!this->prime(this->m))
	{
		this->m++;
	}
	TElem* arr = this->elems;
	this->elems = new TElem[this->m];
	for (int i = 0; i < m; i++)
	{
		this->elems[i] = NULL_TELEM;
	}
	for (int i = 0; i < old_m; i++)
	{
		this->add(arr[i]);
		this->nrOfElems--;
	}
	delete[] arr;
}

Bag::Bag() {
	//TODO - Implementation
	this->m = 11;
	this->elems = new TElem[this->m];
	for (int i = 0; i < m; i++)
	{
		this->elems[i] = NULL_TELEM;
	}
	this->nrOfElems = 0;
}


void Bag::add(TElem elem) {
	//TODO - Implementation
	int i = 0;
	int pos = this->h(elem, i);
	
	while (i < m && this->elems[pos] != NULL_TELEM)
	{
		i++;
		pos = this->h(elem, i);
	}

	if (i >= m)
	{
		this->resize();

		i = 0;
		pos = this->h(elem, i);

		while (i < m && this->elems[pos] != NULL_TELEM)
		{
			i++;
			pos = this->h(elem, i);
		}
		this->elems[pos] = elem;
	}
	else
	{
		this->elems[pos] = elem;
	}

	this->nrOfElems++;
}


bool Bag::remove(TElem elem) {
	//TODO - Implementation
	int i = 0;
	int pos = this->h(elem, i);

	while (i < m && this->elems[pos] != elem && this->elems[pos] != NULL_TELEM)
	{
		i++;
		pos = this->h(elem, i);
	}
	
	if (i >= m || this->elems[pos] == NULL_TELEM)
	{
		return false;
	}
	else
	{
		this->elems[pos] = DELETED_TELEM;
		this->nrOfElems--;
		return true;
	}
}


bool Bag::search(TElem elem) const {
	//TODO - Implementation
	int i = 0;
	int pos = this->h(elem, i);

	while (i < m && this->elems[pos] != elem && this->elems[pos] != NULL_TELEM)
	{
		i++;
		pos = this->h(elem, i);
	}

	if (i >= m || this->elems[pos] == NULL_TELEM)
	{
		return false;
	}
	else
	{
		return true;
	}
}

int Bag::nrOccurrences(TElem elem) const {
	//TODO - Implementation
	int i = 0;
	int pos = this->h(elem, i);
	int occ = 0;

	while (i < m && this->elems[pos] != NULL_TELEM)
	{
		if (this->elems[pos] == elem)
		{
			occ++;
		}
		i++;
		pos = this->h(elem, i);
	}
	return occ; 
}


int Bag::size() const {
	//TODO - Implementation
	return this->nrOfElems;
}


bool Bag::isEmpty() const {
	//TODO - Implementation
	return this->nrOfElems == 0;
}

BagIterator Bag::iterator() {
	return BagIterator(*this);
}


Bag::~Bag() {
	//TODO - Implementation
	delete[] this->elems;
}

