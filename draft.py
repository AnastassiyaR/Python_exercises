letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

alphabet = "abcdefghijklmnopqrstuvwxyz"

def second_letter(word):
    return word[1]  # here we should check that the string is long enough

names = ["aye", "xai", "mxo"]
print(sorted(names, key=second_letter))



a = {'a': 'aaaaaaaaaaa'}

for i in a['a']:
    print(i)
