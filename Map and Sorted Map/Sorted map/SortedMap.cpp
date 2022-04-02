#include "SMIterator.h"
#include "SortedMap.h"
#include <exception>
#include <math.h>
using namespace std;

SortedMap::SortedMap(Relation r) {
	//TODO - Implementation
	this->allocated_size = 5;
	this->arr = new TElem[this->allocated_size];
	this->nr_of_elem = 0;
	for (int i = 0; i < 5; i++)
	{
		this->arr[i] = NULL_TPAIR;
	}
	this->rel = r;
}

TValue SortedMap::add(TKey k, TValue v) {
	//TODO - Implementation
	TValue former = NULL_TVALUE;

	for (int i = 0; i < this->nr_of_elem; i++)
	{
		if (this->arr[i].first == k)
		{
			former = this->arr[i].second;
			this->arr[i].second = v;
			break;
		}
	}

	if (former == NULL_TVALUE)
	{
		for (int i = 0; i < this->nr_of_elem; i++)
		{
			if (this->rel(k, this->arr[i].first))
			{
				this->nr_of_elem++;
				if (this->nr_of_elem >= this->allocated_size)
				{
					this->expand();
				}

				for (int j = this->nr_of_elem; j > i; j--)
				{
					this->arr[j] = this->arr[j - 1];
				}
				this->arr[i].first = k;
				this->arr[i].second = v;
				return former;
			}
		}
		this->nr_of_elem++;
		if (this->nr_of_elem >= this->allocated_size)
		{
			this->expand();
		}
		this->arr[this->nr_of_elem - 1].first = k;
		this->arr[this->nr_of_elem - 1].second = v;
	}

	return former;
}

TValue SortedMap::search(TKey k) const {
	//TODO - Implementation
	for (int i = 0; i < this->nr_of_elem; i++)
	{
		if (this->arr[i].first == k)
		{
			return this->arr[i].second;
		}
	}
	return NULL_TVALUE;
}

TValue SortedMap::remove(TKey k) {
	//TODO - Implementation
	TValue former = NULL_TVALUE;

	for (int i = 0; i < this->nr_of_elem; i++)
	{
		if (this->arr[i].first == k)
		{
			former = this->arr[i].second;
			for (int j = i; j < this->nr_of_elem - 1; j++)
			{
				this->arr[j] = this->arr[j + 1];
			}
			this->nr_of_elem--;
			if (this->nr_of_elem <= this->allocated_size / 2)
			{
				this->reduce();
			}
			break;
		}
	}

	return former;
}

int SortedMap::size() const {
	//TODO - Implementation
	return this->nr_of_elem;
}

bool SortedMap::isEmpty() const {
	//TODO - Implementation
	return this->nr_of_elem == 0;
}

int SortedMap::getKeyRange() const
{
	if (this->isEmpty() || this->size() <= 1)
		return -1;

	/*TValue max = NULL_TVALUE, min = NULL_TVALUE;

	for (int i = 0; i < this->size(); i++)
	{
		if (max == NULL_TVALUE && min == NULL_TVALUE)
		{
			max = this->arr[i].first;
			min = this->arr[i].first;
		}
		else
		{
			if (this->arr[i].first > max)
			{
				max = this->arr[i].first;
			}
			if (this->arr[i].first < min)
			{
				min = this->arr[i].first;
			}
		}
	}*/

	return abs(this->arr[0].first - this->arr[this->nr_of_elem - 1].first);
}

SMIterator SortedMap::iterator() const {
	return SMIterator(*this);
}

SortedMap::~SortedMap() {
	//TODO - Implementation
	delete[] this->arr;
}

void SortedMap::expand()
{
	TElem* cp = new TElem[this->allocated_size];

	for (int i = 0; i < allocated_size; i++)
	{
		cp[i] = this->arr[i];
	}

	delete[] this->arr;

	this->arr = new TElem[this->allocated_size * 2];

	for (int i = 0; i < allocated_size; i++)
	{
		this->arr[i] = cp[i];
	}
	for (int i = allocated_size; i < allocated_size * 2; i++)
	{
		this->arr[i] = NULL_TPAIR;
	}

	this->allocated_size *= 2;

	delete[] cp;
}

void SortedMap::reduce()
{
	TElem* cp = new TElem[this->allocated_size / 2];

	for (int i = 0; i < allocated_size / 2; i++)
	{
		cp[i] = this->arr[i];
	}

	delete[] this->arr;

	this->arr = new TElem[this->allocated_size / 2];

	for (int i = 0; i < allocated_size / 2; i++)
	{
		this->arr[i] = cp[i];
	}

	this->allocated_size /= 2;

	delete[] cp;
}
