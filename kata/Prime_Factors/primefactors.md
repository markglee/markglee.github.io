# Prime Factors

(Adopted from Uncle Bob)

This is a very short kata. You will write more test code than actual production code. 

There are two key things to learn:

* How if statements become while statements as the number of test cases increase.
* How algorithms become more simple as they become more general.

You will need to know:

How classes and objects work in Python
the difference between .append and .extend (try this in a terminal)

## Write a class named PrimeFactors that has one static method "of" 

The method takes a single integer input and returns a list of the prime factors in numerical sequence.

>> from primefactors import PrimeFactors
>> x = PrimeFactors()
>> x.of(2)
[2]
>> x.of(1)
[]
>> x.of(4)
[2,2]

Use PURE TDD. Don't write code until you have a failing test!