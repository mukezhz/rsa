# RSA
We use RSA to encrypt the plain text ie. convert the plain text to cipher text. For example:
```
suppose,
'LOVE' is plain text then
it's equivalent cipher text will be
'QOVJ'

```
**Note:** A->1, B->2, C->3 ... and so on

As we know everything inside the computer works in numeric value for example ASCII, UTF-8 etc are some standards which are used by computer to convert a character to number

Since this is just a basic of RSA, I haven't used exact numeric value what say ASCII uses
Users are free to assign its own value for example:
```
A->1  B->2  C->3  D->4 ... Z->26
a->27 .. and so on
```
Its user preference to suppose where you have mapped your character

## Basic working of RSA algorithm
- RSA is an asymmetric cryptographic algorithm
- It used encryption key for the encryption and decryption key for decryption

# I have use the algorithm which I have studied in my college course **COMPUTER NETWORK**

### Algorithm are as follows:
- Generate two large prime numbers say 'p' & 'q'
- Compute modulus 'n': n = p * q
- Compute 'phy' we called 'z' here: z = (p-1) * (q-1)
- Choose an integer 'e' which follows the following conditions:
```
  e should be greater than 1 and less than n ie.
  (1 < e < n)
  &
  common factor between e and z should be 1 only ie.
  gcd(e, z) = 1

  Note: e is known as public exponent or encryption exponent or just exponent 
```
- Compute an integer 'd' which is obtained if we follow the following condition:
```
  d should be greater than 1 and less than z ie.
  (1 < d < z)
  &
  remainder we get after dividing the product of e and d by z should be equal to 1
  e*d mod z = 1

  Note: d is known as private exponent or decryption exponent
```
- Public key is <n, e> 
- Private key is <n, d>

#### Since we get the public key and private key
- Use public key to produce cipher text from plain text by:
```
  c = m^e % n
```
- Use private key to produce plain text from cipher text by:
```
  m = c^d % n
```

#
```
Note: m = Plain Text and c = Cipher Text
e is used to encrypt m
d is used to decrupt c
```

