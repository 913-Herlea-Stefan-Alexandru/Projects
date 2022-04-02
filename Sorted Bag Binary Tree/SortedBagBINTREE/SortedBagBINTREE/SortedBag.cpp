#include "SortedBag.h"
#include "SortedBagIterator.h"

void SortedBag::resize()
{
	int* newInfo = new int[this->cap * 2];
	int* newLeft = new int[this->cap * 2];
	int* newRight = new int[this->cap * 2];
	int* newParent = new int[this->cap * 2];
	int* newEmptyList = new int[this->cap * 2];

	for (int i = 0; i < this->cap; i++)
	{
		newInfo[i] = this->info[i];
		newLeft[i] = this->left[i];
		newRight[i] = this->right[i];
		newParent[i] = this->parent[i];
	}

	for (int i = this->cap; i < this->cap * 2; i++)
	{
		newInfo[i] = NULL_TCOMP;
		newLeft[i] = -1;
		newRight[i] = -1;
		newParent[i] = -1;
		newEmptyList[i - this->cap] = this->cap * 2 - i + this->cap - 1;
	}

	delete[] this->info;
	delete[] this->left;
	delete[] this->right;
	delete[] this->parent;
	delete[] this->emptyList;

	this->info = newInfo;
	this->left = newLeft;
	this->right = newRight;
	this->parent = newParent;
	this->emptyList = newEmptyList;

	this->nrEmpty = this->cap;

	this->cap *= 2;
}

int SortedBag::getMinimum() const
{
	if (this->root == -1)
	{
		return -1;
	}
	int currentNode = this->root;
	while (this->left[currentNode] != -1)
	{
		currentNode = this->left[currentNode];
	}
	return currentNode;
}

int SortedBag::successor(int node) const
{
	if (this->right[node] != -1)
	{
		int c = this->right[node];
		while (this->left[c] != -1)
		{
			c = this->left[c];
		}
		return c;
	}
	else
	{
		int c = node;
		int p = this->parent[node];
		while (p != -1 && this->left[p] != c)
		{
			c = p;
			p = this->parent[p];
		}
		return p;
	}
}

int SortedBag::predecessor(int node) const
{
	if (this->left[node] != -1)
	{
		int c = this->left[node];
		while (this->right[c] != -1)
		{
			c = this->right[c];
		}
		return c;
	}
	else
	{
		int c = node;
		int p = this->parent[node];
		while (p != -1 && this->right[p] != c)
		{
			c = p;
			p = this->parent[p];
		}
		return p;
	}
	return 0;
}

SortedBag::SortedBag(Relation r) : r{ r } {
	//TODO - Implementation
	this->cap = 10;
	this->dim = 0;

	this->firstEmpty = 0;
	this->root = -1;

	this->info = new int[10];
	this->left = new int[10];
	this->right = new int[10];
	this->parent = new int[10];

	this->nrEmpty = 9;
	this->emptyList = new int[10];

	for (int i = 0; i < 10; i++)
	{
		this->info[i] = NULL_TCOMP;
		this->left[i] = -1;
		this->right[i] = -1;
		this->parent[i] = -1;

		this->emptyList[i] = 10 - i - 1;
	}
}

void SortedBag::add(TComp e) {
	//TODO - Implementation
	if (this->root == -1)
	{
		this->root = this->firstEmpty;
		this->info[this->root] = e;
		this->left[this->root] = -1;
		this->right[this->root] = -1;
		this->parent[this->root] = -1;
		this->firstEmpty = this->emptyList[this->nrEmpty - 1];
		this->nrEmpty--;
		this->dim++;
		return;
	}
	int currentNode = this->root;
	if (this->nrEmpty == 0)
	{
		this->resize();
	}
	int newNode = this->firstEmpty;
	this->info[newNode] = e;
	this->left[newNode] = -1;
	this->right[newNode] = -1;
	this->parent[newNode] = -1;
	this->firstEmpty = this->emptyList[this->nrEmpty - 1];
	this->nrEmpty--;
	while (this->info[currentNode] != NULL_TCOMP)
	{
		if (this->r(e, this->info[currentNode]) || e == this->info[currentNode])
		{
			if (this->left[currentNode] == -1)
			{
				this->parent[newNode] = currentNode;
				this->left[currentNode] = newNode;
				break;
			}
			currentNode = this->left[currentNode];
		}
		else
		{
			if (this->right[currentNode] == -1)
			{
				this->parent[newNode] = currentNode;
				this->right[currentNode] = newNode;
				break;
			}
			currentNode = this->right[currentNode];
		}
	}
	this->dim++;
}


bool SortedBag::remove(TComp e) {
	//TODO - Implementation
	int currentNode = this->root;
	while (currentNode != -1)
	{
		if (this->info[currentNode] == e)
		{
			if (this->left[currentNode] == -1 && this->right[currentNode] == -1)
			{
				this->info[currentNode] = NULL_TCOMP;
				if (this->root == currentNode)
				{
					this->root = -1;
				}
				else if (currentNode == this->left[this->parent[currentNode]])
				{
					this->left[this->parent[currentNode]] = -1;
				}
				else
				{
					this->right[this->parent[currentNode]] = -1;
				}
				this->parent[currentNode] = -1;
				this->nrEmpty++;
				this->emptyList[this->nrEmpty - 1] = currentNode;
			}
			else if (this->left[currentNode] == -1)
			{
				this->info[currentNode] = NULL_TCOMP;
				if (this->root == currentNode)
				{
					this->root = this->right[currentNode];
				}
				else if (currentNode == this->left[this->parent[currentNode]])
				{
					this->left[this->parent[currentNode]] = this->right[currentNode];
				}
				else
				{
					this->right[this->parent[currentNode]] = this->right[currentNode];
				}
				this->parent[this->right[currentNode]] = this->parent[currentNode];
				this->parent[currentNode] = -1;
				this->right[currentNode] = -1;
				this->nrEmpty++;
				this->emptyList[this->nrEmpty - 1] = currentNode;
			}
			else if (this->right[currentNode] == -1)
			{
				this->info[currentNode] = NULL_TCOMP;
				if (this->root == currentNode)
				{
					this->root = this->left[currentNode];
				}
				else if (currentNode == this->left[this->parent[currentNode]])
				{
					this->left[this->parent[currentNode]] = this->left[currentNode];
				}
				else
				{
					this->right[this->parent[currentNode]] = this->left[currentNode];
				}
				this->parent[this->left[currentNode]] = this->parent[currentNode];
				this->parent[currentNode] = -1;
				this->left[currentNode] = -1;
				this->nrEmpty++;
				this->emptyList[this->nrEmpty - 1] = currentNode;
			}
			else
			{
				int movedNode = this->left[currentNode];
				while (this->right[movedNode] != -1)
				{
					movedNode = this->right[movedNode];
				}
				if (this->root == currentNode)
				{
					this->root = movedNode;
				}
				else if (currentNode == this->left[this->parent[currentNode]])
				{
					this->left[this->parent[currentNode]] = movedNode;
				}
				else
				{
					this->right[this->parent[currentNode]] = movedNode;
				}
				if (this->parent[movedNode] != currentNode)
				{
					this->right[this->parent[movedNode]] = this->left[movedNode];
					if (this->left[movedNode] != -1)
					{
						this->parent[this->left[movedNode]] = this->parent[movedNode];
					}
					this->parent[this->left[currentNode]] = movedNode;
					this->left[movedNode] = this->left[currentNode];
				}
				if (this->right[currentNode] != -1)
				{
					this->parent[this->right[currentNode]] = movedNode;
				}
				this->right[movedNode] = this->right[currentNode];
				this->parent[movedNode] = this->parent[currentNode];
				this->info[currentNode] = NULL_TCOMP;
				this->parent[currentNode] = -1;
				this->left[currentNode] = -1;
				this->right[currentNode] = -1;
				this->nrEmpty++;
				this->emptyList[this->nrEmpty - 1] = currentNode;
			}
			this->dim--;
			return true;
		}
		if (this->r(e, this->info[currentNode]))
		{
			currentNode = this->left[currentNode];
		}
		else
		{
			currentNode = this->right[currentNode];
		}
	}
	return false;
}


bool SortedBag::search(TComp elem) const {
	//TODO - Implementation
	int currentNode = this->root;
	while (currentNode != -1)
	{
		if (this->info[currentNode] == elem)
		{
			return true;
		}
		if (this->r(elem, this->info[currentNode]))
		{
			currentNode = this->left[currentNode];
		}
		else
		{
			currentNode = this->right[currentNode];
		}
	}
	return false;
}


int SortedBag::nrOccurrences(TComp elem) const {
	//TODO - Implementation
	int currentNode = this->root;
	int n = 0;
	while (currentNode != -1)
	{
		if (this->info[currentNode] == elem)
		{
			n++;
		}
		if (this->r(elem, this->info[currentNode]))
		{
			currentNode = this->left[currentNode];
		}
		else
		{
			currentNode = this->right[currentNode];
		}
	}
	return n;
}



int SortedBag::size() const {
	//TODO - Implementation
	return this->dim;
}


bool SortedBag::isEmpty() const {
	//TODO - Implementation
	return this->root == -1;
}


SortedBagIterator SortedBag::iterator() const {
	return SortedBagIterator(*this);
}


SortedBag::~SortedBag() {
	//TODO - Implementation
	delete[] this->info;
	delete[] this->left;
	delete[] this->right;
	delete[] this->parent;
	delete[] this->emptyList;
}
