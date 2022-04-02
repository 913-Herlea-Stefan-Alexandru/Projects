#include <assert.h>

#include "SortedMultiMap.h"
#include "SMMIterator.h"
#include <exception>
#include <vector>

using namespace std;

bool relation1(TKey cheie1, TKey cheie2) {
	if (cheie1 <= cheie2) {
		return true;
	}
	else {
		return false;
	}
}

void testAll(){
	SortedMultiMap smm = SortedMultiMap(relation1);
	assert(smm.size() == 0);
	assert(smm.isEmpty());
    smm.add(1,2);
    smm.add(1,3);
    assert(smm.size() == 2);
    assert(!smm.isEmpty());
    vector<TValue> v= smm.search(1);
    assert(v.size()==2);
    v= smm.search(3);
    assert(v.size()==0);
    SMMIterator it = smm.iterator();
    it.first();
    while (it.valid()){
    	TElem e = it.getCurrent();
    	it.next();
    }
    smm.add(3, 4);
    smm.add(3, 8);
    smm.add(4, 2);
    SortedMultiMap smm2 = SortedMultiMap(relation1);
    smm2.add(3, 5);
    smm2.add(3, 9);
    smm2.add(3, 21);
    smm2.add(8, 3);
    smm2.add(4, 5);
    smm2.add(4, 2);
    assert(smm.updateValues(smm2) == 2);
    assert(smm.remove(1, 2) == true);
    assert(smm.remove(1, 3) == true);
    assert(smm.remove(2, 1) == false);
    //assert(smm.isEmpty());
}

