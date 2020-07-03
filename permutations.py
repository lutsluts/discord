#input your word, character, number combination etc, then on the same line,
#leave a space and input how long your maximum combinations will be
#NB! it works better if you dont reuse same characters in your combination
#correct form: abcd 4
#also correct: 1A2B 2
from itertools import permutations
sisend = input().split()
for a in range(int(sisend[1]), -1, -1):
    listed = sorted(list(permutations(sisend[0], int(sisend[1])-a)))
    for i in range(len(listed)):
        print("".join(listed[i]).ljust(int(sisend[1]), "-"))
