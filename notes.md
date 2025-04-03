# LeetCode prep notes

## Arrays
* to compare max of 2 numbers: a = max(1,10) {Built in function in Python}

## String
* ASCII Values for:
  * Small-case Alphabets: 97 to 122
  * Capital-cas Alphabets: 65 to 90 
* To convert a character to its ASCII value: built in python function - ord()
* String Operations:
  * s.isdigit(): Confirms if it is a digit or not
  * s.isalpha(): Confirms if it is an alphabet
  * s.alnum(): Confirms if it is alphabet or numeric
  * s.isspace(): confirms if it is a space
  * s.isascii(), s.isdecimal(), s.isupper(), s.islower() are few other built in functions in Python

## Linked Lists
* Different types: Singly Linked Lists, Doubly Linked Lists, Circular Linked Lists etc.
* Important functions:
  * add in beginning, end and at a given position
  * deleting the beginning, end , given position and given value
  * traversing and printing , size
  * **reverse a linked list**
  * **Fast traversing: node.next.next**



## Stacks
* To convert a list to string: use join() function. <br>
>Eg: stack = ['l','e','e','t'] \
     q = "".join(stack) \
This joins all the elements of stack into single string with "" (no space) delimiter. \
Hence output would be - leet.  
