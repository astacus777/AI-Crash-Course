# Exercise for Lists and Arrays: Homework Solution

import numpy as np                          # we import the Numpy library and give it abbreviation "np"

L4 = [[2, 9, -5], [-1, 0, 4], [3, 1, 2]]    # this is once again our L4 list

mean = np.mean(L4)                          # this method from Numpy class let's us easily calculate the mean of an array/list

print(mean)                                 # we display the mean calculated by function above

# moje przyklady

L4 = [[2, 9, -5],[-1, 0, 4], [3, 1, 2], [8, 10, 6]]
sum = L4[0][0] + L4[0][1] + L4[0][2] + L4[1][0] + L4[1][1] + L4[1][2] + L4[2][0] + L4[2][1] + L4[2][2]
sum1 = np.mean(L4)
sum2 = 0
lengh = 0
for row in L4:
  for el in row:
    sum2 = sum2 + el
    lengh = lengh + 1

print(sum/9)

print("2nd way: ", sum1)
print("3nd way: ", sum2/lengh)
print("lengh: ", lengh)