#pragma once

#include "movieRepo.h"

class MViterator
{
	friend class MovieRepo;

private:

	const MovieRepo& repo;

	MViterator(const MovieRepo& repo);

	int pos;

public:

	~MViterator();

	void first();

	bool next();

	bool valid();

	int getPos();
};