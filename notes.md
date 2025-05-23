# LeetCode prep notes

## Basics
* 2 types- iterative ; recursive

### Arithmetic Operators:
- '**': Exponentiation
- '//': Floor Division
  - **Note:** Difference between '/' [Normal division - returns float value] and '//' [Floor Division- returns integer value]


## **Abstract Linear Data Types:** 

## Arrays[List]
* to compare max of 2 numbers: a = max(1,10) {Built-in function in Python}
* abs(x) - function in python that gives absolute of the number x
* Typecasting: q=['1','0','0']. Here all elements of q are strings. To access them as integers, typecast - int(q[0]) \
  Vice-versa: q=[1,0,0]. To stringify it - str(q[0])
* To declare a 2-d array, declare a 1d and append each row.\
  Eg: do- a=[] and add each row to it(row=[1,2,3]) instead of declaring it as a[][] (invalid syntax) or a[[]] (creates only one empty list of 1D)
* Pre assign same value for each row: row=[1]*(j) ==> say j=3, equivalent of saying  create 3 copies of [1]. 


## String
* ASCII Values for:
  * Small-case Alphabets: 97 to 122
  * Capital-cas Alphabets: 65 to 90 
* To convert a character to its ASCII value: built in python function -> ord()
* To convert an integer into character -> chr(i)
* Strings are immutable, i.e, cannot be edited/changed. \
  * To make it mutable, we have to convert it into a List and then make changes and join it.
    (Eg- LC:345)


* String Operations:
  * s.isdigit(): Confirms if it is a digit or not
  * s.isalpha(): Confirms if it is an alphabet
  * s.alnum(): Confirms if it is alphabet or numeric
  * s.isspace(): confirms if it is a space
  * s.isascii(), s.isdecimal(), s.isupper(), s.islower() are few other built in functions in Python
  * k=s.split("/") : Uses "/" as a delimiter and splits the string s into an list
  * s.replace("/",":")--> replaces all "/" with ":"


  * l=re.sub(r'[^a-zA-Z0-9]', '', text) : this regular expression method is used to add only alphanumeric chars and no special characters
  * The same can be done using isalnum() function as well through iteration


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
s
Applications of DEQ: Multi Porcessors ; Redo & Undo in systems


## **Abstract Non-Linear Data Types:**



# Interesting LC to solve:
>- **LC143** : <br>
   Interesting way of manipulating linked lists \
   1>2>3>4>5 ===> 1>5>2>4>3
>- **LC71** :<br>
   Tricky String Manipulation for file path \
   "/.../a/../b/c/../d/./"  ===>  "/.../b/d"
   Note: use built in functions for string manipulation: x.split("/"), x.join(""), x.replace("(","/")
>- **LC1700** : <br>
   Interesting simulation of matching students wanting circle and square food with sandwiches. 
>- **LC345**: <br>
   Interesting manipulation of strings ; while intuition was right, logic written was a bit different.\
   Note: If x==y doesn't work, translate the logic into what must be done if x!=y. 
>- **LC541** : <br>
   Very interesting way of string manipulation. \ 
   Every element in first k positions should be reversed in every 2k steps.\
   Intuition was partially correct but was not implemented in the code. Edge cases were missed.\
   Can use **reversed** function for a subset of string(List of sub-string as well) \ 
   Eg: s="abcdefg" k=2 ; expected output: "**ba**cd**fe**g" notice the first k characters are interchanged in every 2k steps.
>- **LC67**: <br>
   Although I solved it, it wasn't the efficient solution. 
   Eg; a=["111"], b=["111"]. output>> ["1000"]
>- **LC2563**: <br>
   Intuition was partially correct. Interesting way of calculating sum within range. Tried too hard to do everything in one loop.\
   If unable to solve everything in one loop, try to break it into 2 loops. 
   eg: Counting sum which is [>=lower] and [<=upper] can be broken down to 2 loops -> count of everything [<=upper]-count of everything[<lower].\
   Time complexity calculations: O(n)+O(n) = O(n)
>- **LC38**: <br>
   Took some time to understand the question. The iteration, though simple, was hard to understand. Had to simulate it few times.
>- **LC70**: <br>
   Interesting simulation. Easy but I complicated it by myself.\
   If intuition is not working, simulate more and compare results with previous results to find a trend.


## Patterns of solving DSA:
1. Two-Pointers : there are 2 pointers running in the same loop instead of having 2 different pointers. 
Notes: Sorting an array will help efficiently solve 2 pointer problems
> Types:
> * (One fast, one slow eg: LC141) ;
> * (different start positions eg: LC541) ; 
> * (Sorting of array is efficient use of 2 pointers eg: LC2563)

2. Sliding Window: 


3. Fibbonachi Series: 


4. Bit Manipulation: Using gates - And, Or, Nand, Nor, Xor 


## Methodology of solving:
- Understanding of the question
- Intuition construction
- Writing logic
- Testing with generic edge case scenarios
- Analysis of Complexity 


## Links
- https://www.w3schools.com/dsa/ : DSA Preperation
- https://systemdesignschool.io/primer#introduction : System Design Preperation


## NeetCode Notes
- In python, when using built in array sorting: nums.sort() -> time complexity is O(nlogn); \
space complexity is dependant on the sorting algorithm used [can be O(1) or O(n)].
- 