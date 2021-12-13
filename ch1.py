# r-1.1
def is_multiple(n, m):
    return(m % n == 0)

# print(is_multiple(5, 10))
# print(is_multiple(3, 10))

# r-1.2
def is_even(k):
    return (k & 1 == 0)

# print(is_even(10))
# print(is_even(2))
# print(is_even(1000))
# print(is_even(5))
# print(is_even(100001))
# print(is_even(1))

# r-1.3
def minmax(data):
    if not data:
        raise ValueError("Data list is empty")
    else:
        min = max = data[0]
    for i in data:
        if i < min:
            min = i
        elif i > max:
            max = i
    return min, max

# print(minmax([1,4,78,9,-8]))
# print(minmax([1]))
# print(minmax([-99999, 1,4,78,9,-8, 0]))
# print(minmax([1,4,78,9,-8, 999999, 7, -9786, 765]))
# print(minmax([]))

# r-1.4
def square_sum(n):
    if n < 1 or not isinstance(n, int):
        raise ValueError("n must be a positive integer")
    sum = 0
    for i in range(1,n):
        sum += i ** 2
    return sum

# print(square_sum(1))
# print(square_sum(2))
# print(square_sum(3))
# print(square_sum(4))
# print(square_sum(5))
# print(square_sum(6))

# r-1.5
def square_sum2(n):
    return sum(i ** 2 for i in range(1,n))

# print(square_sum2(1))
# print(square_sum2(2))
# print(square_sum2(3))
# print(square_sum2(4))
# print(square_sum2(5))
# print(square_sum2(6))

# r-1.6 & r-1.7
def square_sum3(n):
    return sum(i ** 2 for i in range(1,n) if i % 2 == 1)
# print(square_sum3(1))
# print(square_sum3(2))
# print(square_sum3(3))
# print(square_sum3(4))
# print(square_sum3(5))
# print(square_sum3(6))

# r-1.8
# j = n + k

# r-1.9
# print([i for i in range(50,90,10)])

# r-1.10
# print([i for i in range(8,-10,-2)])

# r-1.11
# print([2 ** i for i in range(0,9)])

# r-1.12
from random import randrange
def choice(data):
    return data[randrange(0, len(data))]

# list = [1,4,78,9,-8, 999999, 7, -9786, 765]
# print(choice(list))
# print(choice(list))
# print(choice(list))
# print(choice(list))

# c-1.13
def reverse(data):
    templist = []
    for i in range(len(data)-1, -1, -1):
        templist.append(data[i])
    return templist

# list = [1,4,78,9,-8, 999999, 7, -9786, 765]
# print(reverse(list))

# c-1.14
def find_neg_pair(data):
    for i in range(0,len(data)):
        for j in range(0,len(data)):
            if data[i] != data[j] and data[i] * data[j] < 0:
                return True
    return False

# print(find_neg_pair([1,4,78,9,-8, 999999, 7, -9786, 765]))
# print(find_neg_pair([1,4,78,9, 999999, 7, 765]))
# print(find_neg_pair([1]))
# print(find_neg_pair([-1, -2]))
# print(find_neg_pair([-1, -2, 3]))

# c-1.15
def distinct(data):
    for i in range(0,len(data)):
        for j in range(0,len(data)):
            if i != j and data[i] == data[j]:
                return False
    return True

# print(distinct([1,4,78,9,-8, 999999, 7, -9786, 765]))
# print(distinct([1,4,78,9,-8, 999999, 7, -9786, 765,1]))
# print(distinct([1]))

def distinct2(data):
    # faster but uses more memory to store the temp set
    tempset = set()
    for i in range(0,len(data)):
        if data[i] in tempset:
            return False
        else:
            tempset.add(data[i])
    return True

# print(distinct2([1,4,78,9,-8, 999999, 7, -9786, 765]))
# print(distinct2([1,4,78,9,-8, 999999, 7, -9786, 765,1]))
# print(distinct2([1]))

# c-1.16
# data[j] *= factor is shorthand for data[j] = data[j] * factor
# So the immutable integer in data[j] is being scaled then the alias that is data[j] is then set to reference the new immutable integer.
# The original list isn't being given to the *= operator directly

# c-1.17
# No because val is being assigned to a new value but never assigned back into the original data list.

# c-1.18
# print([ i * (i + 1) for i in range(0,10)])

# c-1.19
# print([chr(i) for i in range(97,123)])

# c-1.20
from random import randint
def shuffle(data):
    templist = []
    for i in range(0, len(data)):
        templist.append(data.pop(randint(0,len(data)-1)))
    return templist

# print(shuffle([1,4,78,9,-8, 999999, 7, -9786, 765]))
# print(shuffle([1,4,78,9,-8, 999999, 7, -9786, 765]))
# print(shuffle([1,4,78,9,-8, 999999, 7, -9786, 765]))
# print(shuffle([1]))

# c-1.21
# print("Enter strings one line at a time. Enter ctrl-D to quit and display strings reversed")
# str_list = []
# try:
#     while True:
#         str_list.append(input())
# except(EOFError):
#     print()
#     for i in range(len(str_list)-1, -1, -1):
#         print(str_list[i])

# c-1.22
# Might be confused on what the question is asking. From what I recall the dot product would
# return only a single value and not another array like that
def dot_prod(a, b):
    c = []
    for i in range(0,len(a)):
        c.append(a[i] * b[i])
    return c

# a = [1,2,3]
# b = [3,2,1]
# print(dot_prod(a,b))

# c-1.23
def buffer_overflow(list):

    for i in range(0,len(list)+3,2):
        try:
            list[i] += 3
        except (IndexError):
            print("Don't try buffer overflow attacks in Python!")
    return list

# a = [1,2,3]
# buffer_overflow(a)

# c-1.24
def vowel_cnt(str):
    count = 0
    vowels = {'a','e','i','o','u','y'}
    for i in (range(len(str))):
        if str[i] in vowels:
            count += 1
    return count

# str1 = "ddddddddd"
# str2 = "asoyudopeqwrbkqwabsikvsa7yud"
# str3 = "aaauiopkoafsdobho"
# str4 = ""
# str5 = "a"
# print(vowel_cnt(str1))
# print(vowel_cnt(str2))
# print(vowel_cnt(str3))
# print(vowel_cnt(str4))
# print(vowel_cnt(str5))

# c-1.25
def remove_punc(str):
    new_str = ""
    for i in range(len(str)):
        if 97 <= ord(str[i]) <= 177 \
        or 65 <= ord(str[i]) <= 90 \
        or ord(str[i]) == 32:
            new_str += str[i]
    return new_str

# str1 = "Let's try, Mike."
# str2 = "!!!!!!"
# str3 = "no punctuation"
# print(remove_punc(str1))
# print(remove_punc(str2))
# print(remove_punc(str3))

# c-1.26
def check_formula(a,b,c)
