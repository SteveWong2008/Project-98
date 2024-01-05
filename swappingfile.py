def swapFileData():
    data1 = input('Enter file 1')
    data2 = input('Enter file 2')
    
    file1 = open(data1, 'r')
    file2 = open(data2, 'r')

    read1 = file1.read()
    read2 = file2.read()

    temp1 = open(data1,'w')
    temp2 = open(data2,'w')

    temp1.write(read2)
    temp2.write(read1)

    print('File successfully switched')

swapFileData()