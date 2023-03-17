import numpy as np
#Creating a vector of length 5 filled with arbitrary integers from 0 to 10
vector = np.random.randint(0, 11, size=5)
print(vector)

#Creating a vector with values ​​ranging from 15 to 55 
vector1 = np.arange(15, 56)
print(vector1[1:-1])

#Creating a random array with 1000 elements
array1= np.random.rand(1000)
average=np.mean(array1)
variance=np.var(array1)
standard_deviation=np.std(array1)
print("The Average is: ", average)
print("The Variance is: ", variance)
print("The Standard Deviation is: ", standard_deviation)

#
array2 = np.array([[2, 4, 6], [8, 10, 12], [14, 16, 18]])
print(array2)

# Cumulative sum along columns
cumulative_sum_columns = np.cumsum(array2, axis=0)

# Cumulative sum along rows
cumulative_sum_rows = np.cumsum(array2, axis=1)

# Sum over rows for each column
sum_over_rows = np.sum(array2, axis=0)

# Sum over columns for each row
sum_over_columns = np.sum(array2, axis=1)

print("Cumulative sum along columns: \n", cumulative_sum_columns)
print("Cumulative sum along rows: \n", cumulative_sum_rows)
print("Sum over rows for each column: ", sum_over_rows)
print("Sum over columns for each row: ", sum_over_columns)


#Creating a program to multiply two matrices
matrix_1 = np.array([[1, 0], [0, 1]])
matrix_2 = np.array([[1, 2], [3, 4]])
outcome = matrix_1 @ matrix_2
print(outcome)