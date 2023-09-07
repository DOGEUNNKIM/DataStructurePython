import ctypes
#array
#값 변경만 가능 
#추가 및 삭제 불가능 --> C에서 동적할당을 하려먼 malloc과 free를 사용
#정적 할당


#list
#추가 및 삭제가 가능
#동적 할당임
#list는 연속적으로 되어있음 --> 값들은 각자의 공간에 개별적으로 존재


a = []
ab=[111,222,333,444]
ab.append(555)
ab.append(444)

ab.remove(444)

ab.count(111)

for i in range(len(ab)):
    print(ab[i])

#print(ab.capacity())

print( id(ab[0]))
print(id(ab[1]))
print(ab[0])