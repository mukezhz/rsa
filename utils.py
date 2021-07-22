import math
# 1 and itself can only divide
def input_prime(n):
    num = None
    while True:
        num = int(input(f"Enter {n}: "))
        counter=0
        for i in range(2, num): # 2 3 4 5 6 7
            if num%i == 0:
                counter += 1
        if counter > 0:
            print("The number you have entered is not prime number")
        else:
            print("Viola got it :)")
            break
    return num

def find_e(n, z):
    while True:
        try:
            e = int(input(f"Enter e please select less than {n}: "))
            if e < n:
                if math.gcd(e,z) == 1:
                    print("Selection of e is completed")
                    break
                else:
                    print("==========================================================")
                    print(f"{z} and {e} common factor is not 1 it is {math.gcd(e,z)}") 
                    print("==========================================================")
                continue
            else:
                print(f"{e} is greater than {n}")
        except:
            print("Please enter the number")
            continue
    return e

def find_d(e, z):
    d = None
    for i in range(1,1111):
        if e*i%z == 1 and i!=e:
            d = i
            break
    return d

def print_msg(list1, list2, e , d, t=""):
    msg1="message"
    exp_msg="m^e"
    msg2="cyphers [c = m^e % n]"
    exp = e
    if t=="d":
        msg1="cyphers"
        exp_msg="c^d"
        msg2="message [m = c^d % z]"
        exp = d
    print(f"{msg1:>4}   {exp_msg:>46}           {msg2}:<8")
    for i,t in enumerate(list1):
        print(f"{t:>4}      {t**exp:>46}            {list2[i]:<8}")
        
def encrypt_msg(mlist, e, n):
    clist = [m**e % n for m in mlist]
    return clist[:]

def decrypt_msg(clist, d, n):
    mlist = [c**d % n for c in clist]
    return mlist[:]

def plain_text():
    print("Enter numbers separated by spaces")
    print("Eg. 1 20 1 2 4")
    t = input()
    t = map(lambda n: int(n), t.split())
    return list(t)[:]


def mplain_text():
    mlist = []
    while True:
        m = input("Enter the message(m) and 'k' to finish: ")
        if m == "k":
            break
        if type(m) == type(str):
            continue
        else:
            m = int(m)
            mlist.append(m)
    return mlist[:]

