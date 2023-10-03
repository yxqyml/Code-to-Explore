# How to calcuate the value of PI (π) 
This folder include two python files:
* est_pi.py -- Python file to show the estimation of PI by using animations (Plotly)  
* est_pi_explain.py -- Python file (manim) to explain the principle of calculation of PI by using Monte Carlo.
## 1. History, Efforts, and Fun Facts of PI (π) 

Pi (π) is a magical mathematical constant representing the ratio of a circle's circumference to its diameter. Although it may seem simple, the precise value of pi has always been one of the pursuits of mathematicians and scientists. Let's take a look at the history of pi, the relentless efforts of people to calculate it, and some interesting facts.

## 1.1 History:

The history of pi dates back to ancient civilizations. Ancient cultures like Egypt, Greece, and India all have records related to pi. The ancient Greek mathematician Archimedes was one of the early mathematicians who attempted to calculate pi. He used a method known as the "Method of Archimedes" to approximate the value of pi by progressively dividing a circle into polygons.

## 1.2 Relentless Efforts:

As time went on, more and more mathematicians delved into the calculation of pi. In the 17th century, mathematician John Wallis proposed an infinite series known as Wallis's formula, which could be used to approximate the value of pi. Leibniz and Newton independently discovered similar series, propelling research on pi.

However, pi is an infinitely non-repeating decimal, requiring an infinite number of decimal places to represent it more accurately. This prompted mathematicians to use various methods and computational tools, including computers, to calculate more digits of pi. By the end of the 20th century, pi had been computed to billions of decimal places, finding extensive applications in science and engineering.

## 1.3 Fun Facts:

In addition to mathematical research, pi holds a special place in culture. Pi Day is celebrated on March 14th each year because 3.14 approximates pi. People commemorate this day with various fun mathematical activities and contests and even make pi-themed pies to celebrate.

Another interesting fact is that some individuals have memorized and recited pi to an impressive number of decimal places. Math enthusiasts have competed to see who can memorize more digits of pi. Currently, some have successfully memorized thousands of digits of pi.

In summary, pi is not just a mathematical constant; it is a symbol of history, efforts, and fun facts. The tireless efforts of mathematicians have allowed us to better understand this constant, while Pi Day and pi memorization contests bring some enjoyable mathematical entertainment. Regardless, pi will continue to inspire curiosity and passion in people.

# 2. Estimation of PI by using Monte Carlo method
## 2.1 Understanding the Principle
The principle behind the Monte Carlo method for estimating π is based on the idea of randomly sampling points within a square and determining the ratio of points that fall inside a quarter-circle to those that fall outside it. The quarter-circle is inscribed within the square.

## 2.2 Sampling Points 
Imagine you have a square with a quarter-circle inside it. To estimate π, you randomly generate a large number of points (often done using a computer) within the square. These points are uniformly distributed, meaning they are scattered randomly and evenly throughout the square.

## 2.3 Counting Points
You then count the number of points that fall inside the quarter-circle. To determine if a point is inside the quarter-circle, you check if its distance from the origin (the center of the square) is less than the radius of the quarter-circle. Points within the quarter-circle are considered "hits," while those outside are "misses."

## 2.4 Calculating the Ratio
The ratio of the number of hits (points inside the quarter-circle) to the total number of points generated within the square is an approximation of the ratio of the areas of the quarter-circle to the square.

## 2.5 Estimating π
By multiplying this ratio by 4 (since the quarter-circle represents one-fourth of the full circle), you get an estimation of π. The more points you generate and the larger your sample size, the closer your estimate will be to the actual value of π.

The beauty of the Monte Carlo method lies in its simplicity and scalability. By increasing the number of randomly generated points, you can achieve increasingly accurate estimates of π. This method is particularly useful in situations where analytical solutions are difficult to obtain or when dealing with high-dimensional problems.

In summary, the Monte Carlo method is a powerful computational technique used to estimate π by randomly sampling points within a square and determining the ratio of points inside a quarter-circle. It provides a practical and flexible approach to approximating the value of this fundamental mathematical constant.
