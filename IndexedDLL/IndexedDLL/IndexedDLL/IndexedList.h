#pragma once
//DO NOT INCLUDE LISTITERATOR

//DO NOT CHANGE THIS PART
typedef int TElem;
#define NULL_TELEM -11111
class ListIterator;

class ListNode
{
public:
    TElem elem;
    ListNode* next;
    ListNode* prev;

    ListNode();

    ~ListNode();
};

class IndexedList {
private:
	//TODO - Representation
    ListNode* head;

    ListNode* tail;

    int length;
	
	//DO NOT CHANGE THIS PART
    friend class ListIterator;    
public:
    // constructor
    // Theta(1)
    IndexedList ();

    // returns the number of elements from the list
    // Theta(1)
    int size() const;

    // checks if the list is empty
    // Theta(1)
    bool isEmpty() const;

    // returns an element from a position
    //throws exception if the position is not valid
    // O(n)
    TElem getElement(int pos) const;

    // modifies an element from a given position
	//returns the old value from the position
    //throws an exception if the position is not valid
    // O(n)
    TElem setElement(int pos, TElem e);

    // adds an element to the end of the list
    // Theta(1)
    void addToEnd(TElem e);

    // adds an element to a given position
    //throws an exception if the position is not valid
    // BC=Theta(1) if the pos is the first one
    // WC=Theta(n) if the pos is the last one
    // O(n)
    void addToPosition(int pos, TElem e);

    // removes an element from a given position
	//returns the removed element
    //throws an exception if the position is not valid
    // BC=Theta(1) if the element is the first one
    // WC=Theta(n) if the element is the last one or the pos ins invalid
    // O(n)
    TElem remove(int pos);

    // searches for an element and returns the first position where the element appears or -1 if the element is not in the list
    // BC=Theta(1) if the element is the first one
    // WC=Theta(n) if the element is the last one or does not exist
    // O(n)
    int search(TElem e)  const;

    //returns the last index of a given element 
    //if the element is not in the list it returns -1 
    // BC=Theta(1) if the element is the last one in the list
    // WC=Theta(n) if the element is the first one in the list or if it does not exist
    // total=O(n)
    int lastIndexOf(TElem elem) const;

    // returns an iterator set to the first element of the list or invalid if the list is empty
    ListIterator iterator() const;

    //destructor
    ~IndexedList();

};
