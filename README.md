## Python Crash Course

### 1. Introduction

Hi everyone, my name's Parth and I'm doing a Bachelor of Advanced Computing with a major in Computer Science and Computational Data Science. I'll be in my third year next sem.

<br>

### 2. Classes and Objects

Python is an object oriented programming language. Almost everything in python is an object, with its own attributes and methods, for eg. `str.split()`.

A class is like a blueprint for an object, which means you can define your own type of object, with custom attributes and methods as you see fit.

- self keyword (_not actually a keyword_)
- del keyword

`__init__()` constructor, is a dunder method. They are a level of abstraction below a general user's interaction with the language. They allow instances of a class to interact with the built-in functions and operators of the language. All operators like `+` and `-` rely on dunder methods under the hood, such as `__add__`.

__Q. Create a class to represent a restaurant and make a program that simulates dining out in that restaurant.__

<br>

### 3. File I/O

Interacting with files in python can be done using the open() method. This takes two parameters, the filename and the mode to open the file in.

Along with these modes, we will also go over how to read and write to a file.

__Q. Read 'data.csv' and print the sum of all numbers in each row one by one, along with the numbers in the row themselves.__

<br>

### 4. Short Break + Questions
<br>

### 5. Testing

Testing is a very important step in the development process. In fact, there's a development practice called test-driven development (TDD) where you write unit tests for your code before writing the actual code. Now I know a lot of you will be thinking, "who cares about testing man just write code". Honestly, I'd agree with you cuz I hate testing. But it's important to be aware of how important it is and there's no way around it, so you might as well try to like it.

Also, don't be scared of testing. It's not as foreign as it might seem, you guys have probably been testing your code one way or another. Even having print statements everywhere and seeing if the output's correct is a form of testing, just not a very good one. We can test using assert statements and write functions to test our code.

`assert sum([1, 2, 3]) == 6, "Should be 6"`

We can automate testing in a better way by using something like the __unittest__ library. Actually, let's create a mini testing suite and we'll see how to write some basic tests for the upcoming questions.

<br>

### 6. Recursion

_You can't understand recursion without first understanding recursion._ It's just another way of solving problems, where we break a problem down into smaller versions of itself and bring them together at the end. A bit tricky to understand because it's hard to imagine what's happening under the hood. Important concepts: base case, recursive case. 

- Recursion isn't necessary, there's always an iterative way of doing a problem.
- In some cases, makes the code way simpler and easier to implement.
- It's easy to accidentally do infinite recursion, that's why we need to carefully choose a base case.
- It can also be inefficient due to stack memory.

__Q. Write a recursive algorithm to generate numbers from the fibonacci sequence.__

The fibonacci sequence goes like this: `0, 1, 1, 2, 3, 5, 8, 13, 21, ...`<br>
$Fib_n = Fib_{n-1} + Fib_{n-2}$

- _Testing_

__Q. Write a recursive algorithm to calculate the sum of all natural numbers until the given number.__

- _Testing_

<br>

### 7. Multi-dimensional arrays

Just means there's a list inside a list. So after accessing the list using an index, we access an element in the nested list using another index.

```
a = [[1, 2], [3, 4]]    # a 2x2 matrix
a[0][1]  # gives us 2
a[1][0]  # gives us 3
```

__Q. Write a function that takes two 2-dimensional arrays and outputs the sum.__

<br>

### 8. Iterators

An object that can be iterated over. We need the `__iter__()` and `__next__()` to implement an iterator. The `__iter__()` method returns an iterator instance of the object, can be used in a for loop. The `__next__()` method returns the value for every iteration. Other than for loops, can also manually use `iter()` and `next()` to interact with iterators. To stop the iteration, we need to `raise` a `StopIteration()` exception.

<br>

### 9. Questions




