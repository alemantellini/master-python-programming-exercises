# EJERCICIO 7 - hours and minutes
def hours_minutes(seconds):
  # Your code here
  hours = (seconds // 3600)
  remainder = (seconds % 3600)
  minutes = (remainder // 60)
  return hours, minutes
# Invoke the function and pass any integer as its argument
print(hours_minutes(3900))
