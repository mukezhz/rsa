import math
from utils import (input_prime, 
        find_e, 
        find_fast_d,
        print_msg,
        encrypt_msg,
        decrypt_msg,
        mplain_text,
        plain_text,
        )

# STEP 1 select 2 prime numbers
print("I haven't check for the condition of prime number you entered")
print("=====================================================================")
print("You might encounter error please select two prime number properly")
print("=====================================================================")
print("Enter two prime numbers")

print("==========================================================")
p = input_prime('p')
print("==========================================================")
q = input_prime('q')
while True:
    if p == q:
        print("p and q are same enter different number")
    else:
        break
    q = input_prime('q')

n = p*q
z = (p-1)*(q-1)
print("==========================================================")
print(f"n = {n}")
print(f"z = (p-1)*(q-1) = {(p-1)}*{(q-1)} = {z}")
print("==========================================================")

# selection of e
e = find_e(n, z)

# selection of d
print("I am selecting the lowest possible value for d")
# e*d % z == 1
d = find_fast_d(e, z)
if d is None:
    print("================== :( ================")
    print("Cannot solve")
    print("================== :( ================")
    exit()
print()
print(f"Your d is: {d}")
print()

# encryption of text
print("Let's the encryption begins")
def encrypt():
    print()
    print("Enter o for entering numbers in one go")
    print("Enter m for entering numbers manually")
    print()
    if input("Enter letter? [o]/m: ") == "m":
        mlist = mplain_text()
    else:
        mlist = plain_text()
    print()
    print(f"p={p}    q={q}   n={n}   z={z}   e={e}   d={d}")
    clist = encrypt_msg(mlist, e, n)
    print_msg(mlist,clist, e, d, 'e')
    print()
    print("Wanna do decrption? of above message? [y]/n")
    if input()!="n":
        print("Let's the decryption begins")
        print(f"p={p}    q={q}   n={n}   z={z}   e={e}   d={d}")
        print()
        mlist = decrypt_msg(clist, d, n)
        print_msg(clist, mlist, e, d, 'd')


encrypt()

