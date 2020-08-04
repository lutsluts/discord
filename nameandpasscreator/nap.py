from random import choice

def get_random(l, char_bool, uplow):
  if char_bool == "y":
    characters = "abcdefghjiklmnopqrstuvwxy123456789"
  else: characters = "abcdefghijklmnopqrstuvwxy"
  if uplow == "u":
    characters = characters.upper()
  elif uplow == "l":
    pass
  else:
    characters += characters.upper()
  return ''.join(choice(characters) for _ in range(l))

def append_info(txt):
  appendFile = open('C:\\Users\\Anon\\Desktop\\gmail\\exampleFile.txt', 'a')
  appendFile.write("\n" + str(txt))
  appendFile.close()
  
times = int(input("How many accs and passes will I create?: "))
length = int(input("What should the length be?: "))
char = input("Do you want to include numbers(y/n): ")
uplow = input("Gibberish uppercase/lowercase or both?(u/l/b): ")


for _ in range(times):
  for _ in range(2):
    append_info(get_random(length, char.lower(), uplow.lower()))
  append_info("\n")
  
print("Done!")
  
