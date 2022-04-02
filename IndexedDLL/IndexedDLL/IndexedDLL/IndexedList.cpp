#include <exception>

#include "IndexedList.h"
#include "ListIterator.h"

IndexedList::IndexedList() {
	//TODO - Implementation
    this->head = nullptr;
    this->tail = nullptr;
    this->length = 0;
}

int IndexedList::size() const {
    //TODO - Implementation
	return this->length;
}


bool IndexedList::isEmpty() const {
    //TODO - Implementation
    return this->head == nullptr;
}

TElem IndexedList::getElement(int pos) const {
    //TODO - Implementation
    if (pos < 0 || pos >= this->length)
        throw std::exception();
    else if (pos == 0)
    {
        return this->head->elem;
    }
    else
    {
        ListNode* currentNode = this->head;
        int currentPos = 0;

        while (currentNode != nullptr && currentPos != pos)
        {
            currentNode = currentNode->next;
            currentPos++;
        }

        if (currentNode == nullptr)
            throw std::exception();
        else
        {
            return currentNode->elem;
        }
    }
}

TElem IndexedList::setElement(int pos, TElem e) {
    //TODO - Implementation
    if (pos < 0 || pos >= this->length)
        throw std::exception();
    else if (pos == 0)
    {
        TElem el = this->head->elem;
        this->head->elem = e;
        return el;
    }
    else
    {
        ListNode* currentNode = this->head;
        int currentPos = 0;

        while (currentNode != nullptr && currentPos != pos)
        {
            currentNode = currentNode->next;
            currentPos++;
        }

        if (currentNode == nullptr)
            throw std::exception();
        else
        {
            TElem el = currentNode->elem;
            currentNode->elem = e;
            return el;
        }
    }
}

void IndexedList::addToEnd(TElem e) {
    //TODO - Implementation
    ListNode* node = new ListNode();
    node->elem = e;
    node->prev = this->tail;

    if (this->head == nullptr)
    {
        this->head = node;
        this->tail = node;
    }
    else
    {
        this->tail->next = node;
        this->tail = node;
    }
    this->length++;
}

void IndexedList::addToPosition(int pos, TElem e) {
    //TODO - Implementation
    if (pos < 0 || pos >= this->length)
        throw std::exception();
    else if (pos == 0)
    {
        ListNode* node = new ListNode;
        node->elem = e;
        node->next = this->head;
        
        if (this->head == nullptr)
        {
            this->head = node;
            this->tail = node;
        }
        else
        {
            this->head->prev = node;
            this->head = node;
        }
        this->length++;
    }
    else
    {
        ListNode* currentNode = this->head;
        int currentPos = 0;

        while (currentNode != nullptr && currentPos < pos - 1)
        {
            currentNode = currentNode->next;
            currentPos++;
        }

        if (currentNode == nullptr)
        {
            throw std::exception();
        }
        else if (currentNode == this->tail)
        {
            this->addToEnd(e);
        }
        else
        {
            ListNode* node = new ListNode;
            node->elem = e;
            node->next = currentNode->next;
            node->prev = currentNode;

            currentNode->next->prev = node;
            currentNode->next = node;
            this->length++;
        }
    }
}

TElem IndexedList::remove(int pos) {
    //TODO - Implementation
    if (pos < 0 || pos >= this->length)
        throw std::exception();
    else if (pos == 0)
    {
        if (this->head == this->tail)
        {
            TElem e = this->head->elem;
            delete this->head;
            this->head = nullptr;
            this->tail = nullptr;
            this->length--;
            return e;
        }
        else
        {
            TElem e = this->head->elem;
            ListNode* headNode = this->head;
            this->head = this->head->next;
            this->head->prev = nullptr;
            delete headNode;
            this->length--;
            return e;
        }
    }
    else
    {
        ListNode* currentNode = this->head;
        int currentPos = 0;

        while (currentNode != nullptr && currentPos != pos)
        {
            currentNode = currentNode->next;
            currentPos++;
        }

        ListNode* deleteNode = currentNode;

        if (currentNode == nullptr)
            throw std::exception();
        else if (currentNode == this->tail)
        {
            this->tail = this->tail->prev;
            this->tail->next = nullptr;
        }
        else
        {
            currentNode->next->prev = currentNode->prev;
            currentNode->prev->next = currentNode->next;
        }

        TElem e = deleteNode->elem;
        delete deleteNode;
        this->length--;
        return e;
    }
}

int IndexedList::search(TElem e) const{
    //TODO - Implementation
    ListNode* currentNode = this->head;
    int currentPos = 0;

    while (currentNode != nullptr && currentNode->elem != e)
    {
        currentNode = currentNode->next;
        currentPos++;
    }

    if (currentNode == nullptr)
        return -1;
    else
        return currentPos;
}

int IndexedList::lastIndexOf(TElem elem) const
{
    ListNode* currentNode = this->tail;
    int currentPos = this->length - 1;

    while (currentNode != nullptr && currentNode->elem != elem)
    {
        currentNode = currentNode->prev;
        currentPos--;
    }

    if (currentNode == nullptr)
        return -1;
    else
        return currentPos;
}

ListIterator IndexedList::iterator() const {
    return ListIterator(*this);        
}

IndexedList::~IndexedList() {
	//TODO - Implementation
    while (!this->isEmpty())
    {
        this->remove(0);
    }
}

ListNode::ListNode()
{
    this->elem = NULL_TELEM;
    this->next = nullptr;
    this->prev = nullptr;
}

ListNode::~ListNode()
{
    this->next = nullptr;
    this->prev = nullptr;
}
