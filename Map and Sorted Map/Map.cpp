#include "Map.h"
#include "MapIterator.h"


Map::Map() {
	//TODO - Implementation
	this->allocated_size = 5;
	this->arr = new TElem[this->allocated_size];
	this->nr_of_elem = 0;
	for (int i = 0; i < 5; i++)
	{
		this->arr[i] = NULL_TELEM;
	}
}

Map::~Map() {
	//TODO - Implementation
	delete[] this->arr;
}

TValue Map::add(TKey c, TValue v){
	//TODO - Implementation
	TValue former = NULL_TVALUE;

	for (int i = 0; i < this->nr_of_elem; i++)
	{
		if (this->arr[i].first == c)
		{
			former = this->arr[i].second;
			this->arr[i].second = v;
			break;
		}
	}

	if (former == NULL_TVALUE)
	{
		this->nr_of_elem++;
		if (this->nr_of_elem > this->allocated_size)
		{
			this->expand();
		}

		this->arr[nr_of_elem - 1].first = c;
		this->arr[nr_of_elem - 1].second = v;
	}

	return former;
}

TValue Map::search(TKey c) const{
	//TODO - Implementation
	for (int i = 0; i < this->nr_of_elem; i++)
	{
		if (this->arr[i].first == c)
		{
			return this->arr[i].second;
		}
	}
	return NULL_TVALUE;
}

TValue Map::remove(TKey c){
	//TODO - Implementation
	TValue former = NULL_TVALUE;

	for (int i = 0; i < this->nr_of_elem; i++)
	{
		if (this->arr[i].first == c)
		{
			former = this->arr[i].second;
			this->arr[i] = this->arr[this->nr_of_elem - 1];
			this->nr_of_elem--;
			break;
		}
	}

	return former;
}


int Map::size() const {
	//TODO - Implementation
	return this->nr_of_elem;
}

bool Map::isEmpty() const{
	//TODO - Implementation
	return this->nr_of_elem == 0;
}

int Map::getValueRange() const
{
	if (this->isEmpty() || this->size() == 1)
		return -1;

	TValue max = NULL_TVALUE, min = NULL_TVALUE;

	for (int i = 0; i < this->size(); i++)
	{
		if (max == NULL_TVALUE && min == NULL_TVALUE)
		{
			max = this->arr[i].second;
			min = this->arr[i].second;
		}
		else
		{
			if (this->arr[i].second > max)
			{
				max = this->arr[i].second;
			}
			if (this->arr[i].second < min)
			{
				min = this->arr[i].second;
			}
		}
	}

	return max - min;
}

MapIterator Map::iterator() const {
	return MapIterator(*this);
}

void Map::expand()
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
	for (int i = allocated_size; i < allocated_size*2; i++)
	{
		this->arr[i] = NULL_TELEM;
	}

	this->allocated_size *= 2;

	delete[] cp;
}

void Map::reduce()
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

