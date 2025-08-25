import csv

#  filedata = open('filename','mode')
'''
Operations
read    - r - filedata= open(filename, 'r')
write   - w - filedata= open(filename, 'w')
append  - a - filedata= open(filename, 'a')
create  - x - filedata= open(filename, 'x') ?if file exists, throws error

'''
# reading 
d = open('Sample.csv')
print(d.read())
# print(d.readline())
# list1 = d.readlines()
# print(list1[4])
d.close()


# f = open('Data2.csv','x')   # creating the file, only if it does not exist
f = open('Data2.csv', 'w')  # writing to the file
f.write('Name, Age, City\n')
f.write('Giri, 25, New York\n')
f.close()

# auto close
with open('Data2.csv', 'w') as f:
    f.write('Name, Age, City\n')
    f.write('Jenilia, 40, New York\n')
    f.write('Raj, 35, New York\n')

with open('Data2.csv', 'a') as f:
    f.write('John, 25, New York\n')
    f.write('Giri, 25, New York\n')

try:
    with open('Data2.csv','r') as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")
