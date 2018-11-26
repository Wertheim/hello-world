#Sorting Algorithms in Python#
###Bubble Sort###
def bubble_sort(list):
    swap = False
    while not swap:
        #print('Bubble sort: ' + str(list))
        swap = True
        
        for j in range(0, len(list)-1):
            #check
            if list[j] > list[j+1]:
                swap = False
                #swap the elements
                temp = list[j+1]
                list[j+1] = list[j]
                list[j] = temp

testList = [11,23,35,7,23,6,2,1,13]

print('Before')
print(testList)
bubble_sort(testList)
print('After Bubble Sort')
print(testList)

###Selection Sort###
def selection_sort(list):
    #track two indices
    i = 0
    while i != len(list):
        #print('Selection sort: ' + str(list))
        #check if element is the smallest and move it to front
        #check again on smaller list
        for j in range(i, len(list)):
            if list[j] < list[i]:
                (list[i], list[j]) = (list[j], list[i])
        i += 1
 
testList = [11,23,35,7,23,6,2,1,13]
       
print('Before')
print(testList)
selection_sort(testList)
print('After Selection Sort')
print(testList)

###Merge Sort###
def merge(left, right):
    result = []
    i = 0
    j = 0
    #combine and sort both halves of a list
    #by finding the correct place for each element
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    #append leftover(sorted) elements
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    #test print
    print('merge: ' + str(left) + ' with ' + str(right) + ' gets ' +str(result))
    return result

def merge_sort(list):
    #print('merge sort: ' + str(L))
    #base case
    if len(list) < 2:
        return list[:]
    else:
        #find middle index
        m = len(list)//2
        #sort both halves recursivley
        left = merge_sort(list[:m])
        right = merge_sort(list[m:])
        #combine and sort again
        return merge(left, right)
        
testList = [11,23,35,7,23,6,2,1,13]
print('Before')
print(testList)

print('After Merge Sort')
print(merge_sort(testList))

