#value = int(input("enter a number between [0,10]"))
#if value > 10 or value < 0:
#    exit(1)
myfile = open("file.txt","r") #to open a file  open(file,mode)
for lines in myfile:
    print(lines.strip())

outfile = open("outfile.txt","w")
for line in range(1,11):
    outfile.write(str(line))
outfile.close()
