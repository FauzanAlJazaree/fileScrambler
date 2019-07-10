import os, random

label = input( 'Enter file directory path : ')
dir_path = "./" + label
totalRenamedFile = 0
used_random = []

os.makedirs("rename_"+label)
os.chdir(dir_path)

totalFile = len(os.listdir())
print("total file:"+str(totalFile))

for filename in os.listdir():
	n = random.randint(0, totalFile)
	
	#menghindari perulangan n
	while n in used_random:
		n = random.randint(0, totalFile)
	used_random.append(n)

	newFilename = str(label)+"_"+"%03d"%n+".jpg"
	os.rename(filename, "../rename_"+label+"/"+newFilename)
	totalRenamedFile+=1
	print (filename, "==>", newFilename, "| total renamed file = ", totalRenamedFile)

#hapus folder asli dan rename folder rename+label
os.chdir("../")
os.rmdir(label)
os.rename("rename_"+label, label)