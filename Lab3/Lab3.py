
def element(lst, n):
    for i in range(n):
        maxvalue= float('-inf')
        for num in lst:
            if num > maxvalue:
                maxvalue = num
    
        lst=[num for num in lst if num != maxvalue]
    return maxvalue

my_list=[2, 3, 5, 6, 7, 8, 9, 10]
n = int(input())
print(element(my_list, n))
