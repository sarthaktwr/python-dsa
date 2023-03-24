def selection_sort(a):
    for i in range(len(a)):
        min_index = i
        for j in range(i + 1, len(a)):
            if a[min_index] > a[j]:
                min_index = j
            
        a[min_index], a[i] = a[i], a[min_index]
    
    return a

if __name__ == '__main__':
    a = [1, 5, 9, 7, 4, 6, 3]
    print(selection_sort(a))