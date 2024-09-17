# Feed Dog
This project provides a solution to determine the number of dogs that can be fed based on their hunger levels and the sizes of available biscuits. The problem is solved using an iterative approach to match dogs with biscuits where each dog requires a biscuit of at least the same size as its hunger level.

## Problem Description
Given two lists:
- hunger_level: A list where each element represents the hunger level of a dog.
- biscuit_size: A list where each element represents the size of a biscuit.

The goal is to determine how many dogs can be fed. A dog can be fed if there is a biscuit whose size is at least as large as the dog's hunger level. Once a biscuit is used, it cannot be used again.

#### Example
For the input lists:
hunger_level = [2,1]
buiscit_size = [1,3,2]
the output will be: 2

Explanation: The dog with hunger level 2 can be fed by the biscuit of size 3, and the dog with hunger level 1 can be fed by the biscuit of size 2.

## How to Run
To run the script, simply execute the following into your terminal: FeedDog.py 

## License
This project is licensed under the MIT License.
