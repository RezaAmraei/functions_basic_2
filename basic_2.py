def countdown(num):
    listAnswer = []
    for i in range(num,-1, -1):
        listAnswer.append(i)
    return listAnswer
print(countdown(5))

def print_and_return(arr):
    print(arr[0])
    return arr[1]
answer = print_and_return([1,2])
print(answer)

def first_plus_length(arr):
    return arr[0] + len(arr)
answer2 = first_plus_length([1,2,3,4,5])
print(answer2)

def values_greater_than_second(arr):
    newList = []
    if len(arr) <= 2:
        return False
    for x in arr:
        if x > arr[1]:
            newList.append(x)
    return newList
answer3 = values_greater_than_second([5,2,3,2,1,4])
print(answer3)

def this_length_that_value(size, val):
    newList = []
    for i in range(size):
        newList.append(val)
    return newList
final_answer = this_length_that_value(4,7)
print(final_answer)