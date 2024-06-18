import random

upper = ['A','B','C','D','E','F','G']
lower = ['a','b','c','d','e','f','g']
nums = ['1','2','3','4','5','6','7','8','9']
special_char = ['$','@','^','!','#']

wordlist = []

def readfile(wordfile):
    with open(wordfile, 'r') as file:
        data = file.readlines()
        for word in data:
            words = word.split()
            for item in words:
                wordlist.append(item.capitalize())


def genpass(wordlist, upper, lower, nums, special_char):
    random_word = random.choice(wordlist)
    num = str(random.randint(10, 99))
    password = (random.choice(upper) + random_word + random.choice(lower) +
             random.choice(nums) + random.choice(special_char) + num)
    return password

# Text file
wordfile = "wiki-word.txt"

# Function call
readfile(wordfile)

for i in range(10):
    print(f" Password {i} is : ", genpass(wordlist,upper, lower, nums, special_char))
