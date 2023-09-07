# bubble sort
# 두 숫자를 비교해가며 큰수를 뒤로 보냄
# 내부 loof가 수행되면 가장 큰 수는 제일 뒤로 감
# loof를 반복할 때마다 총 횟수는 출어들음

from operator import le
import time

sort_example = [9,10,245,4,5,62,745,8,3,2,1]

def bubble_sort(list_):
    for i in range(len(list_)-1):
        for j in range(len(list_)-1-i):
            if list_[j]>list_[j+1]:
                temp = list_[j+1]
                list_[j+1] = list_[j]
                list_[j] = temp
    for i in range(len(list_)):
        print (list_[i])
start = time.time()
bubble_sort(sort_example)
end = time.time()
print("bubble_sort 걸린 시간: ", end - start)

# selection sort
# 가장 작은 숫자를 선택해서 앞의 값과 변경해줌
# 1개씩 지나가며 최소값 구하기
def selection_sort(list_):
    for i in range(len(list_)-1):
        min_idx = i
        for j in range(i+1, len(list_)):
            if  list_[min_idx] > list_[j]:
                min_idx = j
        temp = list_[i]
        list_[i] = list_[min_idx]
        list_[min_idx] = temp

    for i in range(len(list_)):
        print (list_[i])
start = time.time()
selection_sort(sort_example)
end = time.time()
print("selection_sort 걸린 시간: ", end - start)

# insertion sort
# 점점 배열의 갯수를 증가시키며 올바른 위치에 삽입하기
def insertion_sort(list_):
    for i in range(1,len(list_)):
        insert_idx = i-1
        key = list_[i]
        while (list_[insert_idx] > key ) & (insert_idx>-1):
            list_[insert_idx + 1] = list_[insert_idx]
            list_[insert_idx] = key
            insert_idx = insert_idx - 1

    for i in range(len(list_)):
        print (list_[i])      

start = time.time()
insertion_sort(sort_example)
end = time.time()
print("insertion_sort 걸린 시간: ", end - start)

# merge sort
def merge_sort(list_):
    if len(list_) > 1:
        r = len(list_)//2
        L = list_[:r]
        M = list_[r:]

        merge_sort(L)
        merge_sort(M)

        i = j = k = 0
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                list_[k] = L[i]
                i += 1
            else:
                list_[k] = M[j]
                j += 1
            k += 1
        while i < len(L):
            list_[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            list_[k] = M[j]
            j += 1
            k += 1
 
start = time.time() 
merge_sort(sort_example)
end = time.time()
for i in range(len(sort_example)):
        print (sort_example[i])
print("merge_sort 걸린 시간: ", end - start)


# quick sort
# pivot을 결정해서 pivot보다 작은건 왼쪽, 큰건 오른쪽으로 옮긴 다음 pivot위치 결정
# 재귀적으로 반복함
# pivot을 결정하는건 랜덤일 수도 있고 제일 오른쪽 값일 수도 있음

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

start = time.time()
sort_example = quick_sort(sort_example)
end = time.time()
for i in range(len(sort_example)):
        print (sort_example[i])
print("quick_sort 걸린 시간: ", end - start)