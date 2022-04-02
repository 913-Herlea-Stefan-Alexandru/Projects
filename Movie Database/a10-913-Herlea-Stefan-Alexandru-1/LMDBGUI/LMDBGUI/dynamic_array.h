#pragma once
#include <string>
#include "movie.h"
#include <vector>
#include <algorithm>
#include <functional>

using namespace std;

template <class T>

class DynamicArray
{
private:

	vector<T> arr2;

public:

	//the constructor for the dynamic array
	//allocates memory or 5 entries, setting the size to 0
	DynamicArray()
	{
		
	}

	//the destructor for the dynamic array
	~DynamicArray()
	{
		
	}

	//adds the object of type T given
	int add(T obj)
	{
		this->arr2.push_back(obj);
		
		return 0;
	}

	//removes the object from pos index(int) given
	//if the index is invalid, returns 1, else returns 0
	int remove(int index)
	{
		if (index < 0 || index >= this->arr2.size())
		{
			return 1;
		}

		this->arr2.erase(this->arr2.begin() + index);

		return 0;
	}

	vector<T> filter(function<bool(T)> f)
	{
		vector<T> filtered(this->arr2.size());

		auto it = copy_if(this->arr2.begin(), this->arr2.end(), filtered.begin(), f);
		filtered.resize(distance(filtered.begin(), it));

		return filtered;
	}

	T* getAddress(int index)
	{
		return &this->arr2[index];
	}

	//returns a pointer to the object of type T if found on position index(int), otherwise returns null
	T operator[](int index)
	{
		return this->arr2[index];
	}

	auto begin()
	{
		return this->arr2.begin();
	}

	auto end()
	{
		return this->arr2.end();
	}

	void clear()
	{
		this->arr2.clear();
	}

	int length() const
	{
		return this->arr2.size();
	}
};
