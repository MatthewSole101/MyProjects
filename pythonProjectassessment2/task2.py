readfile = open('cn4game.txt', 'r')
writefile = open('cn4game.txt', 'a')
writefile.write('P')
writefile.close()
readfile1 = readfile.read()

print(readfile1)