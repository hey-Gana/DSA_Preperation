# LeetCode prep notes

## **Abstract Data Types:** 


## Arrays[List]
* to compare max of 2 numbers: a = max(1,10) {Built-in function in Python}

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
  * k=s.split("/") : Uses "/" as a delimiter and splits the string s into an list

## Linked Lists
* Different types: Singly Linked Lists, Doubly Linked Lists, Circular Linked Lists etc.
* Important functions:
  * add in beginning, end and at a given position
  * deleting the beginning, end , given position and given value
  * traversing and printing , size
  * **reverse a linked list**
  * **Fast traversing: node.next.next**



## Stacks (LIFO)
* To convert a list to string: use join() function. \
>Eg: stack = ['l','e','e','t'] \
     q = "".join(stack) \
This joins all the elements of stack into single string with "" (no space) delimiter. \
Hence output would be - leet.  

* stack elements can be accessed similar to arrays[List]. \
Eg: if you want to access the top element of stack: stack[-1] can be used.

* Applications: Tennis ball stored into a cylinder; bullets in a gun ; Expression Evaluation 

* **Infix, Prefix & Postfix Expressions:** An expression contains cariables, operators,brackets and values.\
Rules: 
Binary operator: requires 2 operands.
> Eg: A+B

**Associativity**
   1. (), [], {}  : Brackets are given highest priority to be calculated 
   2. ^ : (Right to Left)
   3.  *, / : (Left to right)
   4. +, - :(Left to right)

* Infix:  <operand><operator><operand>
> A+B
* Prefix:(Polish Notation)   <operator><operand><operand>
> +AB
* Postfix:(Reverse Polish Notation)  <operand><operand><operator>
> AB+

**Processing of postfix & prefix is better since it takes less memory and time to calculate.** 

Interesting LC to solve:
>- LC143 : Interesting way of manipulating linked lists \
1>2>3>4>5 ===> 1>5>2>4>3
>- LC71 : Tricky String Manipulation for file path \
   "/.../a/../b/c/../d/./"  ===>  "/.../b/d"

## Queues (FIFO)
{Linear, Abstract Data Type Data structure}\
Follows: FIFO; has array, circular array and linkedlist implementation. \
For linear array: the limitation is rear doesnt get updated properly; hence circular array. \
{ (i+1)%N } --> Inserts in the reminder of this. \
Functions involved: enqueue, dequeue, peek. \
3 types of Queues:
- Queue
- DEQ ( Double Ended Queue): Can enqueue and dequeue from both sides. 
- Priority Queue

Applications of DEQ: Multi Porcessors ; Redo & Undo in systems
