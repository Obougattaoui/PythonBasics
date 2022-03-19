# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 18:18:07 2022

@author: oussama

        Data Types
"""


#           String
# Python Program for
# Creation of String
 
# Creating a String
# with single Quotes
String1 = 'Welcome to the Geeks World'
print("String with the use of Single Quotes: ")
print(String1)
 
# Creating a String
# with double Quotes
String1 = "I'm a Geek"
print("\nString with the use of Double Quotes: ")
print(String1)
 
# Creating a String
# with triple Quotes
String1 = '''I'm a Geek and I live in a world of "Geeks"'''
print("\nString with the use of Triple Quotes: ")
print(String1)
 
# Creating String with triple
# Quotes allows multiple lines
String1 = '''Geeks
            For
            Life'''
print("\nCreating a multiline String: ")
print(String1)


String1 = "GeeksForGeeks"
print("Initial String: ")
print(String1)
 
# Printing First character
print("\nFirst character of String is: ")
print(String1[0])
 
# Printing Last character
print("\nLast character of String is: ")
print(String1[-1])

#String slicing: Access a range of characters
string2 = "oussama"
print("slicing string from 1-6:(5 character) ")
print(string2[1:6])

print ("characters beween 3rd en 2nd last character")
print(string2[3:-2])


# This is because Strings are immutable, hence elements of a String cannot be changed once it has been assigned.
String3 = "Hello, I'm a Geek"
print("Initial String: ")
print(String3)
 
# Updating a character
# of the String
String3[2] = 'p'
print("\nUpdating character at 2nd Index: ")
print(String3)
#updating the entire string is allowed

#deletion of a character
String1 = "Hello, I'm a Geek"
print("Initial String: ")
print(String1)
 
# Deleting a character
# of the String
del String1[2]
print("\nDeleting character at 2nd Index: ")
print(String1)
# ===> will cause an error
#deleting the entire string is allowed 
del String1


#Escape sequencing in python
"""
While printing Strings with single and double quotes 
in it causes SyntaxError because String already 
contains Single and Double Quotes and hence cannot be printed with the use of either of these.
to print such a String either Triple Quotes are used or Escape sequences are used to print such Strings. 
Escape sequences start with a backslash
"""
# Initial String
String1 = '''I'm a "Geek"'''
print("Initial String with use of Triple Quotes: ")
print(String1)
# Printing Paths with the
# use of Escape Sequences
String1 = "C:\\Python\\Geeks\\"

#r or R to escape sequences
String1 = r"This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"

#Formatting of strings : format()

String1 = "{} {} {}".format('geeks', 'For', 'Life')
print("print in default order : ")
print(String1)

String1 = "{1} {0} {2}".format('geeks', 'For', 'Life')
print("print in Positional order : ")
print(String1)

#keyword formatting
String1 = "{l} {f} {g}".format(g='geeks', f='For', l='Life')
print("print using keyword formatting : ")
print(String1)


# Formatting of Integers
String1 = "{0:b}".format(16)
print("\nBinary representation of 16 is ")
print(String1)

# Formatting of Floats
String1 = "{0:e}".format(165.6458)
print("\nExponent representation of 165.6458 is ")
print(String1)

#Built in functions



"""
***************************LISTs
Lists are just like dynamically sized arrays
are mutable
"""
#Creating a list
List = []
print("Blank List: ")
print(List) 

List = [10, 20, 14]
print("List of numbers: ")
print(List)

List =  ["oussama", "bougattaoui", "ensa"]
print("List Items: ")
print(List[0])
print(List[1])


#nesting list
List = [['Geeks', 'For'], ['Geeks']]
print("Multidimensional List")
print(List)

# a list can contain  duplicates elements
List = [1, 2, 4, 4, 3, 3, 3, 6, 5]
print("List of integers ", List)

#a list with mixed type
List = [1, "oussama", 10.3]
print("List of mixed types ", List)

#size of list
print(len(List))

#adding elements to the list: at the end
List.append(2)
List.append(3)#just one element in time
print(List)
List = []
for i in range(1, 4):
    List.append(i)
print(List)

#we can add a list to an exesting list

#insert() ==> add element at the desired position
List.insert(2, 4)
List.insert(0, "oussama")
print(List)

#extend method: extend() ==> for adding elements
#adding mutiple elements at the same time at the end of the list
List = [1, 2, 3, 4]
print("Initial List: ")
print(List)
List.extend([5, 6, "oussama"])
print(List)

#Accessing elements from list
List = ["Geeks", "For", "Geeks"]
print("Accessing a element from the list")
print(List[0])
print(List[2])
List = [['Geeks', 'For'], ['Geeks']]
 
# accessing an element from the
# Multi-Dimensional List using
# index number
print("Accessing a element from a Multi-Dimensional list")
print(List[0][1])
print(List[1][0])



#negative indexing: represent positions from the end of the array
List = [1, 2, "Geeks", "For", "Geeks"]
print(List[-3])


#Removing elements from the list
#Remove method in List will only remove the first occurrence of the searched element.
#to remove a range of elements, the iterator is used.
# Creating a List
List = [1, 2, 3, 4, 5, 6,
        7, 8, 9, 5, 11, 12]
print("Initial List: ")
print(List)

List.remove(1)
print(List)
List.remove(5)
print(List)


#pop() remove and return the last element of a list or from a specific position of the list
List = [1, 2, 3, 4, 5]
List.pop()
print("List after popping an element", List)
#removing at a specific location
element = List.pop(2)
print("List after popping an element", List)
print("the element", element)

#slicing of a list
#print a specific range of elements from the list
#[:index]: from beginning to a range
#[:-index] : from the end to a range
#[index:]: from a specific index to the end
#[Start Index:End Index]
#to print the whole List in reverse order, use [::-1].

# Creating a List
List = ['G', 'E', 'E', 'K', 'S', 'F',
        'O', 'R', 'G', 'E', 'E', 'K', 'S']
print("Initial List: ")
print(List)

sliced_List = List[3:8]
print(sliced_List)

sliced_List = List[5:]
print(sliced_List)

sliced_List = List[:-6]
print(sliced_List)

sliced_List = List[-6:-1]

sliced_List = List[::-1]
print(sliced_List)

"""
    List Comprehension
    creating new Listts from other iterables like tuples, String, arrays, lists
    newList = [expression(element) for element in oldList if condition]
"""
old_square = [x ** 2 for x in range(1, 11) if x % 2 == 1]
print(old_square)





"""
    TUPLE
"""
Tuple1 = ()
print("empty tuple", Tuple1)

Tuple1 = ('Geeks', 'For')
print(Tuple1)

#creating a tuple with the use of list
list1 = [1, 2, 3, 4, 5]
print(tuple(list1))
#creatinga tuple using tuple() method
Tuple1 = tuple('Geeks')
print(Tuple1)#('G', 'e', 'e', 'k', 's')

Tuple1 = (1, "oussama", 3, 4.5)
Tuple2 = (1, 10)
#nested tuple
Tuple3 = (Tuple1, Tuple1)
print(Tuple3)

Tuple1 = ("Geeks",) * 3
print("Tuple with repetition ", Tuple1)

#Accessing of tuples
#Tuples ae immutable
#contain heterogeneous elements that are accessed via unpacking or indexing
Tuple1 = tuple("Geeks")
print("first element is ", Tuple1[0])
#Tuple unpacking
Tuple1 = ("Geeks", "For", "Geeks")
a, b, c = Tuple1
print("Values after unpacking: ")
print(a)
print(b)
print(c)

"""Concatenation of tuples
joining two or more tuples
"""
Tuple1 = (0, 1, 2, 3, 4)
Tuple2 = ("Geeks", 1, "Geeks")

Tuple3 = Tuple1 + Tuple2

print("Tuple 1: ", Tuple1)
print("Tuple 2: ", Tuple2)
print("Tuple 3: ", Tuple3)

"""
Slicing
Slicing of a Tuple is done to fetch a specific range or slice of sub-elements from a Tuple
"""
 
# Slicing of a Tuple
# with Numbers
Tuple1 = tuple('GEEKSFORGEEKS')
 
# Removing First element
print("Removal of First Element: ")
print(Tuple1[1:])
 
# Reversing the Tuple
print("\nTuple after sequence of Element is reversed: ")
print(Tuple1[::-1])
 
# Printing elements of a Range
print("\nPrinting elements between Range 4-9: ")
print(Tuple1[4:9])






"""
Deleting a tuple
are immutable do not allow deletion of part of it
using del() method
"""
Tuple1 = (0, 1, 2)
del Tuple1


"""
Difference between List and Tuple
The list is dynamic
the tuple has static characteristics
https://www.geeksforgeeks.org/python-difference-between-list-and-tuple/
"""



"""
Sets is unordered collection of data Type is iterable and mutable
The major advantage of using a set, as opposed to a list, is that 
it has a highly optimized method for checking whether a specific element is contained in the set.
has no duplicate element
mutable
"""

#Creating a set
set1 = set()
print("blank set," ,set1)

set1 = set("GeeksForGeeks")
print(set1)

String = "GeeksForGeeks"
set1 = set(String)
print(set1)
set1 = set(["Geeks", "For", "Geeks"])
print("\nSet with the use of List: ")
print(set1)

#Adding elements to a Set
#List cannot be added to a set as elements
#Tuples can be added
#Only immutable objects can be added to sets
set1 = set()
set1.add(1)
set1.add(2)
set1.add((3, 4))
print(set1)

#updating items
#update() accept String tuples, lists
set1 = set([4, 5, (6, 7)])
print(set1)
set1.update([10, 11])
print("after updating ", set1)

#Accessing a set
#are unordered ==> no index
set1 = set(["Geeks", "For", "Geeks"])
print("initial set: ", set1)
print("elements in the set: ")
for i in set1:
    print(i, end = " ")

print("Geeks" in set1)

#Removing elements from the list
#remove() ==> a keyError arises if element dosent exist
#discard() ==> no KeyError
set1 = set([1, 2, 3, 4, 5, 6, 
            7, 8, 9, 10, 11, 12])
print("Initial Set: ")
print(set1)

set1.remove(5)
set1.remove(6)
print("\nSet after Removal of two elements: ")
print(set1)
set1.remove(5)
set1.discard(12)
print(set1)

"""
pop() remove and return an element from the set
removes only the last element on the set
"""
set1 = set([1, 2, 3, 4, 5, 6, 
            7, 8, 9, 10, 11, 12])
print("Initial Set: ")
print(set1)

x = set1.pop()
print("the element moved is {} and the set {}".format(x, set1))

"""
Using clear method
remove all elements
"""
set1.clear()
print(set1)

"""
Frozen sets
are immutable objects
only support methods and operators that produce a result without affecting the frozen set or sets
"""
#creating a set
String = ('G', 'e', 'e', 'k', 's', 'F', 'o', 'r')
fset1 = frozenset(String)
print(fset1)

"""
Dictionary
ordered(since version 3.7) collection of data values
key value pair
duplicated data
any data type
keys cant be repted and must be immutable
"""
#Creating a dictionary
#can be created also by dict()
Dict = {1: 'oussama', 2: 'bougattaoui'}
print(Dict)
#a dictionary with mixed values
Dict = {1: 'oussama', 'oussama': 'bougattaoui', 2: ['oussama', 1, 2]}
print(Dict)

Dict = {}
print("empty dictionary ", Dict)

Dict = {1: 'oussama', 2: 'Bougattaoui',
        3: {'A': 10, 'B': 5}}
print(Dict)

"""
Adding elements to dictionary
one value at time
Dict[key] = 'value'
"""
Dict = {}
print("Empty dictionary: ")
print(Dict)

Dict[0] = 'oussama'
Dict[1] = 10
print(Dict)
#Adding a set of values
Dict['value_set'] = 2, 3, 4
print(Dict)

#Adding nested key value
Dict[2] = {'nested': {'1': 'yes', '2': 'no'}}
print(Dict)
#Accessing elements
print(Dict['value_set'])
#can also use method: get()
print(Dict.get(0))
#Accessing elements of a nested dictionary
Dict = {'Dict1': {1: 'oussama'},
        'Dict2': {'ous': 'bougattaoui'}}
print(Dict['Dict1'])
print(Dict['Dict2'])
print(Dict['Dict1'].get(1))
print(Dict['Dict1'][1])
print(Dict.get('Dict2').get('ous'))

"""
Removing elements from dictionary

"""
Dict = { 5 : 'Welcome', 6 : 'To', 7 : 'Geeks',
        'A' : {1 : 'Geeks', 2 : 'For', 3 : 'Geeks'},
        'B' : {1 : 'Geeks', 2 : 'Life'}}
print("Initial Dictionary: ")
print(Dict)
del Dict[6]
print(Dict)

del Dict['A'][1]
print(Dict)

"""
pop() delete and return the value of the key specified
"""
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}

pop_ele = Dict.pop(1)
print(Dict)
print(pop_ele)

"""
popitem() returns and removes an arbitrary element
"""
# Creating Dictionary
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
 
# Deleting an arbitrary key
# using popitem() function
pop_ele = Dict.popitem()
print("\nDictionary after deletion: " + str(Dict))
print("The arbitrary pair returned is: " + str(pop_ele))
"""
clear ==> deleting all elements
"""
Dict.clear()
print(Dict)

"""
*******************Arrays *************
store multiple items of the same type together
"""
#Creating an array
import array as arr
#an array with intger type
a = arr.array('i', [1, 2, 3])
for i in range(0, 3):
    print(a[i], end=" ")

#Adding elements to a array
"""
insert() ==> add elements any given index of array
append() ==>add at the end of array
"""
a.insert(1, 4)
print(a)
a.append(5)
print(a)

#Accessing elements from the array
print(a[2])

"""
Removing elements from array
remove() ==> remove one element
pop() ==> removes and return an element(by default the last element)
"""
x = a.pop()
print(x)
#remove the first occurence of 2
a.remove(2)
print(a)

"""
Slicing an array
print a specific range in array
[: index]
[: -index] ==> from the begining to -index
[index:] ==> from index to the end
[start: end]
[::-1] ==> reverse order
"""
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = arr.array('i', l)
sliced_array = a[3:8]
print(sliced_array)
sliced_array = a[:-2]

"""
Searching element in a array
index() ==> returns the index of the first occurence
"""
print(a.index(5))


"""
Updating element in array
"""
a[1] = 20
print(a)











