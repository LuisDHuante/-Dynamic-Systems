def sequence(n):
  sequence = ["\\,frac{1}{10^"+f"{i}"+"}" for i in range(1,n+1)]
  return sequence

print(sequence(int(input("Choose a number: "))))