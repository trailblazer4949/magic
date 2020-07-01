import datetime
import string
from string import Formatter
result = string.ascii_letters
print("\n", result, "\n")

result1 = string.ascii_lowercase
print(result1, "\n")

result2 = string.ascii_uppercase
print(result2, "\n")

result3 = string.digits
print(result3, "\n")

# print(string.digits[1])

print(string.hexdigits, "\n")

print(string.octdigits, "\n")

print(string.punctuation, "\n")

# include - characters space, tab, linefeed, return, formfeed, and vertical tab.
print(string.whitespace, "\n")

# Combination of all(digits, punctuation, whitespaces, ascii_letters)
print(string.printable)

# custom sting formatting
mystring = "My name is {}"
print(str.format("python"))

print("This is {} way of doing {}".format("other", "this"))
print()


# more in format()

Name = ["Bharat", "Vedant"]
Rollno = [1, 2]
Marks = [98, 89]
print("{:<30}{:^30}{:>30}".format("Name", "Rollno", "Marks"))
for i in range(len(Name)):
    print()
    print("{N:<30}  {R:^30} {M:>30}".format(
        R=(int(Rollno[i])), N=str(Name[i]), M=int(Marks[i])))
print()
print(
    "floating numbers {:+f} {:+f} {: f}{: f} {:-f}{:-f}".format(3.14, -3.14, 4.13, 4.13, 5.13, -5.13))
print()

'''
    {: f} -> shows space for positive
    {:+f} -> shows float numbers upto 6 places

'''

# converting values to different bases
print("int {0:d}  Oct  {0:o}  Hex  {0:x}  Bin  {0:b} ".format(15))
print()

# Seperator
print('{:,}'.format(34534642))
print()

# percentage
marksObtained = 87
totalMarks = 100
print("{:.2%}".format(marksObtained / totalMarks))
print()

# datetime
DMT = datetime.datetime.now()
print(DMT)

NDMT = datetime.datetime(2020, 10, 15, 12, 48, 2)
print("{:%Y-%M-%D %H:%M:%S}".format(NDMT))


