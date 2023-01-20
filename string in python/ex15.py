import string

str = "/*Jon is @developer & musician"
print("original string is: ",str)

new_str=str.translate(str.maketrans('', '', string.punctuation))
print("new string: ",new_str)