class Sort:
    def Bubble_Sort(self,a:list[int])->list:
        #i is for iteration
        swap = True
        for i in range(len(a)):
            #j is for comparison
            for j in range(0,len(a)-i-1):
                if a[j]>a[j+1]:
                    a[j],a[j+1] = a[j+1],a[j]
                    swap = True
            if swap == False:
                break
        return a
    def Selection_Sort(self,a:list[int])->list:
        for i in range(len(a)):
            min = i
            for j in range(i+1,len(a)):
                if a[j]<a[min]:
                    min = j
            a[i] , a[min] = a[min] , a[i]
        return a
    def Insertion_Sort(self,a:list[int])->list:
        for i in range(1,len(a)):
            min = a[i]
            j = i - 1
            while j >= 0 and min < a[j] :
                a[j + 1] = a[j]
                j -= 1
            a[j + 1] = min
        return a
    def Merge_Sort(self,a:list[int])->list:
        if len(a) > 1:
            r = len(a)//2
            low = a[:r]
            high = a[r:]
            self.Merge_Sort(low)
            self.Merge_Sort(high)
            i = j = k = 0
            while i < len(low) and j < len(high):
                if low[i] < high[j]:
                    a[k] = low[i]
                    i += 1
                else:
                    a[k] = high[j]
                    j += 1
                k += 1
            while i < len(low):
                a[k] = low[i]
                i += 1
                k += 1

            while j < len(high):
                a[k] = high[j]
                j += 1
                k += 1
        return a
    #The Most Efficient Sorting Algorithm
    def Quick_Sort(self, a:list[int]) -> list:
        def partition(a, low, high) -> int:
            pivot = a[low]
            start = low + 1
            end = high
            while True:
                while start <= end and a[start] <= pivot:
                    start += 1
                while start <= end and a[end] >= pivot:
                    end -= 1
                if start <= end:
                    a[start], a[end] = a[end], a[start]
                else:
                    break
            a[low], a[end] = a[end], a[low]
            return end

        def Quick(a, low, high):
            if low < high:
                x = partition(a, low, high)
                Quick(a, low, x - 1)
                Quick(a, x + 1, high)

        low = 0
        high = len(a) - 1
        Quick(a, low, high)
        return a
    def Radix_Sort(self,a:list[int]) -> list:
        def count(a,place):
            size = len(a)
            output = [0] * size
            count = [0] * 10
            for i in range(0, size):
                index = a[i] // place
                count[index % 10] += 1

            for i in range(1, 10):
                count[i] += count[i - 1]
            i = size - 1
            while i >= 0:
                index = a[i] // place
                output[count[index % 10] - 1] = a[i]
                count[index % 10] -= 1
                i -= 1

            for i in range(0, size):
                a[i] = output[i]
        max_element = max(a)
        place = 1
        while max_element // place > 0:
            count(a, place)
            place *= 10
        return a
    def  Heap_Sort(self,a:list[int]) -> list:
        N = len(A)  #using N because when i'm removing all the elements in heap sort after heapify it will be used so length will be -1
        def heapify(a,i,N):
            largest = i
            l = 2*i+1
            r = 2*i+2
            if l < N and a[largest] < a[l]:
                largest = l
            if r < N and a[largest] < a[r]:
                largest = r
            if largest != i:
                a[i], a[largest] = a[largest], a[i]
                heapify(a,largest,N)
        for i in range((N-1 // 2) ,-1, -1):
            heapify(a, i,N)
        for i in range(N-1,0,-1):
            a[i] ,a[0] = a[0],a[i]
            heapify(a,0,i)
        return a
if __name__ == '__main__':
    sort = Sort()
    A = [int(i) for i in input("Enter the array :-\t").split()]
    print(f"Array is A = {A} ")
    R = sort.Radix_Sort(A)
    Q = sort.Quick_Sort(A)
    I = sort.Insertion_Sort(A)
    M = sort.Merge_Sort(A)
    S = sort.Selection_Sort(A)
    B = sort.Bubble_Sort(A)
    H = sort.Heap_Sort(A)

    print(f"Bubble Sort is :- {B} \nInsertion Sort is :- {I} \nSelection Sort is :-{S} \nRadix Sort is :- {R} \nMerge Sort is :- {M} \nQuick Sort :- {Q} \nHeap Sort :- {H} \n")
