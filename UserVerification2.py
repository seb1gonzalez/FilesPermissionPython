#Sebastian Gonzalez
#imports
import sys
import os
#taking in multiple arguments
print("Searching for file 1: "+ sys.argv[1])
print("Searching for file 2: "+ sys.argv[2])
file1 = sys.argv[1]
file2 = sys.argv[2]
#Checking if file 1 exists in directory
if os.path.isfile(file1):
    print("File 1 found!\n")
else:
    print("File 1 was not found\n")
#Checking if file 2 exists in directory
if os.path.isfile(file2):
    print("File 2 found!\n")
else:
    print("File 2 was not found\n")
#Checking if file 2 is actually a directory
print("Checking if file 2 is a directory...")
if os.path.isdir(file2):
    print("File 2 is a directory\n")
else:
    print("File 2 is not a directory\n")

#Checking permissions for file 1
print("Checking if file 1 has RWX permissions...")
if os.access(file1, os.R_OK) and os.access(file1, os.W_OK) and os.access(file1, os.X_OK):
    print("File 1 has these permissions: READ, WRITE, EXECUTE\n")
else:
    if not os.access(file1, os.R_OK):
        print("File 1 is not readable\n")
        os.chmod(file1, 0o777)
        print("File 1 has now Read permission")
    if not os.access(file1, os.W_OK):
        print("File 1 is not writeable\n")
        os.chmod(file1, 0o777)
        print("File 1 has now Write permission")
    if not os.access(file1, os.X_OK):
        print("File 1 is not executable\n")
        os.chmod(file1, 0o777)
#Checking permissions for file 2
print("Checking if file 2 has RX permissions...")

if os.access(file2, os.R_OK) and os.access(file2, os.X_OK):
    print("File 2 has these permissions: READ, EXECUTE\n")
else:
    if not os.access(file2, os.R_OK):
        print("File 2 is not readable\n")
        os.chmod(file1, 0o555)
        print("File 1 has now Read permission")
    if not os.access(file2, os.X_OK):
        print("File 2 is not executable\n")
        os.chmod(file1, 0o555)
        print("File 2 has now Execute permission")
print("Operations complete")
exit(1)
