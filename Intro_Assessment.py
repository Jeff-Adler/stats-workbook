# 1. Find the variance of B
# B = { -5,3,12,190,-10 }

list_of_values = [-5, 3, 12, 190, -10]
list_of_values_copy = list_of_values

def calculate_avg(list_of_values):
  return sum(list_of_values) / len(list_of_values)

avg_of_values = calculate_avg(list_of_values)

def subtract_from_mean(n):
  return n - avg_of_values

def square_value(n):
  return n * n

differences_from_mean = [subtract_from_mean(n) for n in list_of_values]

squared_differences = [square_value(n) for n in differences_from_mean]

sum_of_squared_differences = sum(squared_differences)

variance = sum_of_squared_differences / len(list_of_values)

print("Variance from script: ", variance) 

def variance(data):
  # Number of observations
  n = len(data)
  # Mean of the data
  mean = sum(data) / n
  # Square deviations
  deviations = [(x - mean) ** 2 for x in data]
  # Variance
  variance = sum(deviations) / n
  return variance

print("Variance from function: ", variance(list_of_values_copy))