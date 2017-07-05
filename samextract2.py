import sys

with open(sys.argv[1]) as inputfile1:
    with open (sys.argv[2]) as inputfile2:
        with open(sys.argv[3],"w") as outputfile:
            ddict = {}
            for line in inputfile1: 
                columns= line.split("\t")
                ddict[columns[0]] = [columns[4], columns [5]]
            for line in inputfile2:
                columns= line.split("\t")
                if columns[1]=="n/a\n":
                    outputfile.write(line)
                    continue
                temps= ddict[columns[0]]
                mystring= line.strip()+"\t"+"\t".join(temps)
                outputfile.write(mystring)
                        
                        
    
