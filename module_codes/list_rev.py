# Code
multiples = []
for x in range(1,11):
  multiples.append(x*7)

print(multiples)
# Code
multiples = [x*7 for x in range(1,11)]
print(multiples)

# Code
languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
lengths = [len(language) for language in languages]
print(lengths)

# Code
z = [x for x in range(0,101) if x%3==0]
print(z)