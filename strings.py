"Mountains".upper()
"Mountains".lower()

answer = "YES"
if answer.lower() == "yes":
  print("User said yes")

" yes ".strip()
" yes ".lstrip()
" yes ".rstrip()

"The number of times e occurs in this string is 4".count("e")

"Forest".endswith("rest")
"Forest".startswith("gre")

"Forest".isnumeric()
"12345".isnumeric()

int("12345") + int("54321")

" ".join(["This", "is", "a", "phrase", "joined", "by", "spaces"])
"...".join(["This", "is", "a", "phrase", "joined", "by", "triple", "dots"])

"This is another example".split()
"This,is,another,example".split(",")

name = "Manny"
number = len(name) * 3
print("Hello {}, your lucky number is {}".format(name, number))

name = "Manny"
print("Your lucky number is {number}, {name}.".format(name=name, number=len(name)*3))

price = 7.5
with_tax = price * 1.09
print(price, with_tax)
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))

def to_celsius(x):
  return (x-32)*5/9

for x in range(0,101,10):
  print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))

print(len("abcde")) # prints 5
for c in "abcde":  print(c) # prints a b c d e
print("abc" in "abcde") # prints True
print("def" in "abcde") # prints False
print("abcde"[2]) # prints c
print("abcde"[:2]) # prints ab
print("abcde"[2:]) # prints cde
print("AaBbCcDdEe".lower()) # prints aabbccdde
print("AaBbCcDdEe".upper()) # prints AABBCCDDEE
print("  Hello  ".lstrip()) # prints Hello  
print("  Hello  ".rstrip()) # prints   Hello
print("  Hello  ".strip()) # prints Hello
test = "How much wood would a woodchuck chuck"
print(test.count("wood")) # prints 2
print(test.endswith("chuck")) # prints True
print("12345".isnumeric()) # prints True
print("-123.45".isnumeric()) # prints False
print("xyzzy".isalpha()) # prints True
print(test.split()) # prints ['How', 'much', 'wood', 'would', 'a', 'woodchuck', 'chuck']
print(" ".join(test.split())) # prints How much wood would a woodchuck chuck
test = "How-much-wood-would-a-woodchuck-chuck"
print(test.split("-")) # prints ['How', 'much', 'wood', 'would', 'a', 'woodchuck', 'chuck']
print(test.replace("wood", "plastic")) # prints "How much plastic would a plasticchuck chuck"
print("-".join(test.split())) # prints How-much-wood-would-a-woodchuck-chuck