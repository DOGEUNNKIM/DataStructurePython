# hash table
#
# key 값들을 규칙(hash function)에 따라 table(list)의 slot에 저장함 
# collision이 발생하면 collision resolution method 를 사용하여 해결
#
# cluster사이즈를 줄여서 검색 삭제 삽입시간을 O(1)으로 가능함
# -->그러기 위해서 50%이상 채워지면 hash table크기를 증가시킴

# hash fucntion 
# perfect hash func(충돌 확률 0), c-universal hash func(충돌 확률 균알한것)
# 좋은 hash func: less collision, fast computation

#collision resolution method
#
# open addressing: 주변의 빈공간에 넣음 
# --> 빈공간 선택 방식에따라 또 나뉨
# --> linear probing, quadratic probing, double hashing
#
# chaining: 각 slot을 head로 하여 linked list 만듦
# --> hash function을 c-universal hash func을 사용하면 linked list 길이 상수 --> O(1)
