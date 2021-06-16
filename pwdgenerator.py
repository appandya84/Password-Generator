import random
from string import digits
from string import punctuation
from string import ascii_letters

print("Secure password generated: ", end="")

pwd = random.choices(ascii_letters + digits + punctuation, k=10)

for i in range(10):
    print(pwd[i], end="")

    
