#include "movieIterator.h"
#include "movieRepo.h"

MViterator::MViterator(const MovieRepo& r) : repo{r}
{
	this->pos = 0;
}

MViterator::~MViterator()
{

}

void MViterator::first()
{
	this->pos = 0;
}

bool MViterator::next()
{
	if (this->pos < this->repo.length() - 1)
	{
		this->pos++;
		return true;
	}
	else
		return false;
}

bool MViterator::valid()
{
	if (this->pos >= this->repo.length())
		return false;
	return true;
}

int MViterator::getPos()
{
	if (!this->valid())
	{
		return -1;
	}
	return this->pos;
}
