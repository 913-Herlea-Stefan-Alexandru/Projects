#include "ListIterator.h"
#include "IndexedList.h"
#include <exception>

ListIterator::ListIterator(const IndexedList& list) : list(list){
   //TODO - Implementation
    this->currentNode = this->list.head;
}

void ListIterator::first(){
    //TODO - Implementation
    this->currentNode = this->list.head;
}

void ListIterator::next(){
    //TODO - Implementation
    if (this->valid())
        this->currentNode = this->currentNode->next;
    else
        throw std::exception();
}

bool ListIterator::valid() const{
    //TODO - Implementation
    if (this->currentNode == nullptr)
        return false;
    return true;
}

TElem ListIterator::getCurrent() const{
   //TODO - Implementation
    if (this->valid())
        return this->currentNode->elem;
    else
        throw std::exception();
}