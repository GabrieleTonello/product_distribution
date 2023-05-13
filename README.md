# Product Distribution Challenge
***

The Challenge is about developing a function that gives as output the gratest Product Allocation, calculated as descripted 
on its website [Challenge] (https://www.vgen.it/it/product-distribution-challenge/)

## Function
To maximize the Product Allocation, first the function orders the list of number to be set in the segments using quick sort algorithm, so as to have the gratest numbers in the last segments (as a consecuence, the gratest the number, the gratest its segment index). Then, calculates the first segment and if there is any rest ( if so, it will mean that the last segment will have more than m elements). Finally, multiplies the segment index with the current number contained in the list, and adds it, changing the index segmentation every m steps.


## Technologies used to implement the function

The function has been written in Python 3.9 and tests have been run using unittest.
Testing has demonstrated the correctness of the solution, testing the possibles types of input that can be passed to the function:
1 ≤ n ≤ 10^6
1 ≤ m ≤ n
1 ≤ ai ≤ 10^9  (note that integers in python have no maximum lenght, so it can be represented with an int)

### Gabriele Tonello
