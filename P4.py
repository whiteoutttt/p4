f = open("p4data.txt")
lines = f.read().split('\n')
for i in range(len(lines)):
    output = open("p4output.txt", "a")
    currentline = lines[i].split('\t')
    average = 0
    min = 9999
    max = 0
    sum = 0
    for x in range (len(currentline)):
        output.write(f"{currentline[x]}\t")
        sum = sum + int(currentline[x])
        if min > int(currentline[x]):
            min = int(currentline[x])
        if max < int(currentline[x]):
            max = int(currentline[x])
        average = sum / len(currentline)
    output.write(f"{sum}\t{average:.3f}\t{max}\t{min}\n")
    output.close()




#the sum, average, largest & smallest (all on one line) to the output file
#close both files
