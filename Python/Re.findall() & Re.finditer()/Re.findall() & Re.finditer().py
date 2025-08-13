
import re

#pattern = re.compile(r"python")
#str = "PYTHON is a very strong programing language."

#match = re.search(pattern,str,re.IGNORECASE)

#if match:
  #  print("found",match.group())
#else:
  #  print("Not found")

#match = re.match(pattern,str)
#print(match)

#if match:
 #   print("Found",match.group())
#else:
 #   print("Not found.")

#pattern = re.compile(r"ab",re.IGNORECASE)
#str = "abcdefabghab"

#match_iter = re.finditer(pattern,str)
#count=0
#for match in match_iter:
 #   print(f"Start: {match.start()}, End: {match.end()}, Element: {match.group()}")
  #  count+=1
#print(count)

#match_list = re.findall(pattern,str)
#print(match_list)

#str = "Hello, my name is Sajir. my phone number is 01314546861"
#pattern = re.compile(r"\.")
#result = re.findall(pattern,str)
#result1 = re.finditer(pattern,str)
#print(result)

#for match in result1:
    #print(f"{match.start()}-{match.end()} = {match.group()}")

str = "sifaz20075@gmail.com and sajirwasee@gmail.com"
pattern = re.compile(r"\w+@\w+\.\w+")
match = re.findall(pattern,str)
print(match)



