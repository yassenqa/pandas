import pandas as p 

data=['peter','Yassin','BILAL','15',' ']
print(p.Series(data))
print('.'*25)

print(p.Series(data).str.len())
print('.'*25)

print(p.Series(data).str.startswith('p'))
print('.'*25)

print(p.Series(data).str.endswith('n'))
print('.'*25)

print(p.Series(data).str.find('B'))#number of index
print('.'*25)

print(p.Series(data).str.rfind('L'))
print('.'*25)

print(p.Series(data).str.rjust(20))
print('.'*25)

print(p.Series(data).str.ljust(55))
print('.'*25)

print(p.Series(data).str.center(10))
print('.'*25)

print(p.Series(data).str.zfill(6))
print('.'*25)

print(p.Series(data).str.isupper())
print('.'*25)

print(p.Series(data).str.islower())
print('.'*25)

print(p.Series(data).str.istitle())
print('.'*25)

print(p.Series(data).str.isspace())
print('.'*25)

print(p.Series(data).str.isdigit())
print('.'*25)

print(p.Series(data).str.isalpha())
print('.'*25)

print(p.Series(data).str.isalnum())##no space
print('.'*25)

print(p.Series(data).str.isdecimal())
print('.'*25)

print(p.Series(data).str.isnumeric())

print('.'*25)

print(p.Series(data).str.swapcase())
print('.'*25)

print(p.Series(data).str.lower())


print('.'*25)
















