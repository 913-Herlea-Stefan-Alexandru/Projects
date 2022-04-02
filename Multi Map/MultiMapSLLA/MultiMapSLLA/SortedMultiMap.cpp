#include "SMMIterator.h"
#include "SortedMultiMap.h"
#include <iostream>
#include <vector>
#include <exception>
using namespace std;

void SortedMultiMap::expand()
{
	//vector
	//TE* e2 = new TE[this->cap * 2];
	//for (int i = 0; i < this->cap; i++)
	//{
	//	e2[i] = this->elems[i];
	//}
	//delete[] this->elems;
	//this->elems = e2;
	//this->cap *= 2;

	//SLLA
	TE* e2 = new TE[this->cap * 2];
	int* n2 = new int[this->cap * 2];
	for (int i = 0; i < this->cap; i++)
	{
		e2[i] = this->elems[i];
		n2[i] = this->next[i];
	}
	for (int i = this->cap; i < this->cap * 2 - 1; i++)
	{
		n2[i] = i + 1;
	}
	n2[this->cap * 2 - 1] = -1;
	delete[] this->elems;
	delete[] this->next;
	this->elems = e2;
	this->next = n2;
	this->firstEmpty = this->cap;
	this->cap *= 2;
}

SortedMultiMap::SortedMultiMap(Relation r) : r{r} {
	//TODO - Implementation
	this->cap = 5;
	this->length = 0;

	//vector
	//this->elems = new TE[this->cap];

	//SLLA
	this->elems = new TE[this->cap];
	this->next = new int[this->cap];
	this->head = -1;
	for (int i = 0; i < this->cap - 1; i++)
	{
		this->next[i] = i + 1;
	}
	this->next[this->cap - 1] = -1;
	this->firstEmpty = 0;
}

void SortedMultiMap::add(TKey c, TValue v) {
	//TODO - Implementation
	//vector
	//for (int i = 0; i < this->length; i++)
	//{
	//	if (this->elems[i].first == c)
	//	{
	//		this->elems[i].second->insertFirst(v);
	//		return;
	//	}
	//	else if (!this->r(this->elems[i].first, c))
	//	{
	//		if (this->length == this->cap)
	//		{
	//			this->expand();
	//		}
	//		for (int j = this->length; j > i; j--)
	//		{
	//			this->elems[j].first = this->elems[j - 1].first;
	//			this->elems[j].second = this->elems[j - 1].second;
	//		}
	//		this->elems[i].second = new SLLA;
	//		this->elems[i].first = c;
	//		this->elems[i].second->insertFirst(v);
	//		this->length++;
	//		return;
	//	}
	//}
	//if (this->length == this->cap)
	//{
	//	this->expand();
	//}
	//this->elems[this->length].second = new SLLA;
	//this->elems[this->length].first = c;
	//this->elems[this->length].second->insertFirst(v);
	//this->length++;

	//SLLA
	if (this->head == -1)
	{
		int newPos = this->firstEmpty;
		this->elems[newPos].first = c;
		this->elems[newPos].second = new SLLA;
		this->elems[newPos].second->insertFirst(v);
		this->firstEmpty = this->next[this->firstEmpty];
		this->next[newPos] = this->head;
		this->head = newPos;
		this->length++;
		return;
	}
	else if (this->elems[this->head].first == c)
	{
		this->elems[this->head].second->insertFirst(v);
		return;
	}
	else if (!this->r(this->elems[this->head].first, c))
	{
		if (this->firstEmpty == -1)
		{
			this->expand();
		}
		int newPos = this->firstEmpty;
		this->elems[newPos].first = c;
		this->elems[newPos].second = new SLLA;
		this->elems[newPos].second->insertFirst(v);
		this->firstEmpty = this->next[this->firstEmpty];
		this->next[newPos] = this->head;
		this->head = newPos;
		this->length++;
		return;
	}
	else
	{
		int current = this->head;
		while (this->next[current] != -1 && this->r(this->elems[this->next[current]].first, c))
		{
			current = this->next[current];
			if (this->elems[current].first == c)
			{
				this->elems[current].second->insertFirst(v);
				return;
			}
		}
		if (this->next[current] != -1 && this->elems[this->next[current]].first == c)
		{
			this->elems[current].second->insertFirst(v);
			return;
		}
		if (this->firstEmpty == -1)
		{
			this->expand();
		}
		int newPos = this->firstEmpty;
		this->elems[newPos].first = c;
		this->elems[newPos].second = new SLLA;
		this->elems[newPos].second->insertFirst(v);
		this->firstEmpty = this->next[this->firstEmpty];
		this->next[newPos] = this->next[current];
		this->next[current] = newPos;
		this->length++;
		return;
	}
}

vector<TValue> SortedMultiMap::search(TKey c) const {
	//TODO - Implementation
	//vector
	//int left = 0, right = this->length - 1;
	//while (left <= right)
	//{
	//	int m = left + (right - left) / 2;
	//	if (this->elems[m].first == c)
	//	{
	//		return this->elems[m].second->toVect();
	//	}
	//	if (this->r(this->elems[m].first, c))
	//	{
	//		left = m + 1;
	//	}
	//	else
	//	{
	//		right = m - 1;
	//	}
	//}
	//return vector<TValue>();

	//SLLA
	int current = this->head;
	while (current != -1 && this->elems[current].first != c)
	{
		current = this->next[current];
	}
	if (current != -1)
	{
		return this->elems[current].second->toVect();
	}
	else
	{
		return vector<TValue>();
	}
}

bool SortedMultiMap::remove(TKey c, TValue v) {
	//TODO - Implementation
	//vector
	//for (int i = 0; i < this->length; i++)
	//{
	//	if (this->elems[i].first == c)
	//	{
	//		bool res = this->elems[i].second->deleteElem(v);
	//		if (!res)
	//		{
	//			return false;
	//		}
	//		if (this->elems[i].second->size() == 0)
	//		{
	//			this->elems[i].first = -111111;
	//			delete this->elems[i].second;
	//			this->elems[i].second = NULL;
	//			for (int j = i; j < this->length - 1; j++)
	//			{
	//				this->elems[j].first = this->elems[j + 1].first;
	//				this->elems[j].second = this->elems[j + 1].second;
	//			}
	//			this->elems[this->length - 1].first = -111111;
	//			this->elems[this->length - 1].second = NULL;
	//			this->length--;
	//		}
	//		return res;
	//	}
	//}
	//return false;

	//SLLA
	int currentNode = this->head;
	int prevNode = -1;
	while (currentNode != -1 and this->elems[currentNode].first != c)
	{
		prevNode = currentNode;
		currentNode = this->next[currentNode];
	}
	if (currentNode != -1)
	{
		bool res = this->elems[currentNode].second->deleteElem(v);
		if (!res)
		{
			return false;
		}
		if (this->elems[currentNode].second->size() == 0)
		{
			delete this->elems[currentNode].second;
			if (currentNode == this->head)
			{
				this->head = this->next[this->head];
			}
			else
			{
				this->next[prevNode] = this->next[currentNode];
			}
			this->next[currentNode] = this->firstEmpty;
			this->firstEmpty = currentNode;
			this->length--;
			return true;
		}
	}
	else
	{
		return false;
	}
}


int SortedMultiMap::size() const {
	//TODO - Implementation
	int size = 0;

	//vector
	//for (int i = 0; i < this->length; i++)
	//{
	//	size += this->elems[i].second->size();
	//}

	//SLLA
	int current = this->head;
	while (current != -1)
	{
		size += this->elems[current].second->size();
		current = this->next[current];
	}

	return size;
}

bool SortedMultiMap::isEmpty() const {
	//TODO - Implementation
	if (this->size() == 0)
		return true;
	return false;
}

SMMIterator SortedMultiMap::iterator() const {
	return SMMIterator(*this);
}

int SortedMultiMap::updateValues(SortedMultiMap& sm)
{
	int k = 0;
	int current = this->head;
	while (current != -1)
	{
		vector<TValue> v = sm.search(this->elems[current].first);
		if (v.size() != 0)
		{
			SLLA* slla = new SLLA;
			for (TValue& val : v)
			{
				slla->insertFirst(val);
			}
			delete this->elems[current].second;
			this->elems[current].second = slla;
			k++;
		}
		current = this->next[current];
	}
	return k;
}

SortedMultiMap::~SortedMultiMap() {
	//TODO - Implementation
	//vector
	//for (int i = 0; i < this->length; i++)
	//{
	//	delete this->elems[i].second;
	//}
	//delete[] this->elems;

	//SLLA
	int current = this->head;
	while (current != -1)
	{
		delete this->elems[current].second;
		current = this->next[current];
	}
	delete[] this->elems;
	delete[] this->next;
}

void SLLA::expand()
{
	TValue* e2 = new TValue[this->cap * 2];
	int* n2 = new int[this->cap * 2];
	for (int i = 0; i < this->cap; i++)
	{
		e2[i] = this->elems[i];
		n2[i] = this->next[i];
	}
	for (int i = this->cap; i < this->cap * 2 - 1; i++)
	{
		n2[i] = i + 1;
	}
	n2[this->cap * 2 - 1] = -1;
	delete[] this->elems;
	delete[] this->next;
	this->elems = e2;
	this->next = n2;
	this->firstEmpty = this->cap;
	this->cap *= 2;
}

SLLA::SLLA()
{
	this->cap = 5;
	this->elems = new TValue[this->cap];
	this->next = new int[this->cap];
	this->head = -1;
	for (int i = 0; i < this->cap - 1; i++)
	{
		this->next[i] = i + 1;
	}
	this->next[this->cap - 1] = -1;
	this->firstEmpty = 0;
	this->length = 0;
}

SLLA::~SLLA()
{
	delete[] this->elems;
	delete[] this->next;
}

void SLLA::insertFirst(TValue val)
{
	if (this->firstEmpty == -1)
	{
		this->expand();
	}
	int newPos = this->firstEmpty;
	this->elems[newPos] = val;
	this->firstEmpty = this->next[this->firstEmpty];
	this->next[newPos] = this->head;
	this->head = newPos;
	this->length++;
}

bool SLLA::deleteElem(TValue val)
{
	int currentNode = this->head;
	int prevNode = -1;
	while (currentNode != -1 and this->elems[currentNode] != val)
	{
		prevNode = currentNode;
		currentNode = this->next[currentNode];
	}
	if (currentNode != -1)
	{
		if (currentNode == this->head)
		{
			this->head = this->next[this->head];
		}
		else
		{
			this->next[prevNode] = this->next[currentNode];
		}
		this->next[currentNode] = this->firstEmpty;
		this->firstEmpty = currentNode;
		this->length--;
		return true;
	}
	else
	{
		return false;
	}
}

TValue SLLA::getByIndex(int index)
{
	return this->elems[index];
}

vector<TValue> SLLA::toVect()
{
	return vector<TValue>(this->elems, this->elems + this->length);
}

int SLLA::size()
{
	return this->length;
}
