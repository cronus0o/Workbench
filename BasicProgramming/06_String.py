# [Session 06]
# Character
# String

# Index (zero-based, negative)
# String Slicing
# [start, target+1, gap]
# [i:], [:i], [:-n], [-n:], [i:j:k]

str = 'start, target, gap'
print(str[0:19:2]) 

# len()
# Iterator in Sequence 
# min(), max() ... by Dictionary List

# .index(i) ... return Index
# .count(i) ... return frequency
# .lower()
# .upper()
# .swapcase() 
# .title()

# strip()
# rstrip()
# lstrip()

# replace('target', 'replace')
# .center(length, " ")
# .ljust(length, " ")
# .rjust(length, " ")
# .zfill(length, " ")

# .isdigit() ... Boolean
# .isalpha() ... Boolean
# .isalnum() ... Boolean
# .islower() ... Boolean
# .isupper() ... Boolean
# .isspace() ... Boolean

# .split() ... basic empty

# String cannot changed. Instead, we can make new string

str = 'Hello Eorld!'
fixed_str = str[:6] + "W" + str[7:]
print(fixed_str)
