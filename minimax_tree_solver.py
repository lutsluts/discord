""" 
Input 8 integers, no spaces: 18574857

1   8   5   7   4   8   5   7
 \ /     \ /     \ /     \ /
  8       7       8       7  <--MAX
   \     /         \     /
      7               7      <--MIN
      \              /
              7              <--MAX
>>> 
"""

def sorter(lst):
  newlist = []
  for i in range(int(len(lst)/2)):
    newlist.append(lst[0:2])
    del lst[0:2]
  
  for i in range(len(newlist)):
    if isinstance(newlist[i],list)==False:
      del newlist[i]
  return [max(n) for n in newlist]


seq = list(input("Input 8 integers, no spaces: "))
if len(seq) != 8:
  print("I said 8 integers!")
  raise SystemExit(0)
  

print("")
print("   ".join(seq))
print(" \ /     \ /     \ /     \ /")
a,b,c,d = sorter(seq)
print("  {}       {}       {}       {}  <--MAX".format(a,b,c,d))
print("   \     /         \     /")
x,y = min(a,b), min(c,d)
print("      {}               {}      <--MIN".format(x,y))
print("      \              /")
print("              {}              <--MAX".format(max(x,y)))
