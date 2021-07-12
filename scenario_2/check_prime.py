def is_prime(num):
  print(f"Checking number {num}...")
  if num == 1:
    return False
  if num == 2:
    return True
  if num % 2 == 0:
    return False
  for factor in range(2, math.floor(math.sqrt(num))):
    if not is_prime(factor): continue
    if num % factor == 0:
      return False
  return True
if any(map(is_prime, list_div)):
  print("There is a prime!")
else:
  print("No primes.")
