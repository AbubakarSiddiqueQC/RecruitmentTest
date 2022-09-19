## Add code below with answer clearly stated
def sum_of_factorial_digit(n: int)->int:
  """ This function will take an argument that is number it will find its factorial and treat that as string to find the sum of the digits in the factorial """
  fact = 1
  sum = 0
  for i in range(1,n+1):
    fact = fact*i
  for d in str(fact):
    sum = sum + int(d)
  return sum

# Driver line.
sum_of_factorial_digit(100)
