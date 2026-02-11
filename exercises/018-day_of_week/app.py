# EJERCICIO 18 - day of week
# Complete the function to return the number of day of the week for k'th day of year
def day_of_week(k):
  # 0 = Sunday (day 4)
  # 1 = Monday (day 5)
  # 2 = Tuesday (day 6)
  # 3 = Wednesday (day 7)
  # 4 = Thursday (day 1)
  # 5 = Friday (day 2)
  # 6 = Saturday (day 3)
  adjustment = (k + 3)
  result = adjustment % 7
  return result
# Invoke function day_of_week with an integer between 1 and 365
print(day_of_week(1))
