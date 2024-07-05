x = int(input(f"Please enter the secret number between 0 and 100: "))
max = 100
min = 0
R = 0

while R != x:
 R = (max + min)/2
 if R > x:
    max = R

 elif R < x:
    min = R

 elif R == x:
    print(f'I have guessed it! It is {R}!')

while x == 0:
    print("woofwoofwoof")
    break
