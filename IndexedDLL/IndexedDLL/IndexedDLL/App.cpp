#include <iostream>
#include "ShortTest.h"
#include "ExtendedTest.h"
#include "IndexedList.h"
#include <assert.h>

using namespace std;

void testOperation()
{
    IndexedList list = IndexedList();
    list.addToEnd(1);
    list.addToEnd(2);
    list.addToEnd(3);
    list.addToEnd(2);
    list.addToEnd(1);
    assert(list.lastIndexOf(1) == 4);
    assert(list.lastIndexOf(2) == 3);
    assert(list.lastIndexOf(3) == 2);
    assert(list.lastIndexOf(5) == -1);
}

int main(){
    testOperation();
    testAll();
    testAllExtended();
    cout<<"Finished LI Tests!"<<endl;
}