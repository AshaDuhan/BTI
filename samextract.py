import sys

with open(sys.argv[1]) as inputfile:
    with open(sys.argv[2],"w") as outputfile:
        for line in inputfile:
            if line.startswith("@"):
                continue 
            columns = line.split("\t")
            unique = line.endswith("NH:i:1\n")
            maps = columns[5] in ["20M","21M","22M"]
            if unique and maps:
                mylist =[columns[0], columns[9], columns[2], columns[3], columns[7], columns[8]]
            else:
                mylist=[columns[0], "n/a"]
            mystring="\t".join(mylist)+"\n"
            outputfile.write(mystring)
