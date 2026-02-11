# EJERCICIO 19 - digital clock
# Complete the function to return how many hours and minutes are displayed on the 24h digital clock
def digital_clock(n):
  total_h = n // 60
  total_min = n % 60
  return (total_h, total_min)

# Invoke the function with any integer (minutes after midnight)
print(digital_clock(150))
