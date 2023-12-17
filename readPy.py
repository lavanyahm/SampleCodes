with open('file3.txt', 'w') as file3:
    with open('Ue_1Positionstream.dat', 'r') as file1:
        with open('RxPacketTrace.txt', 'r') as file2:
            for line1, line2 in zip(file1, file2):
                 columns = line1.split( )
                 print (columns[1])
                 columns_SINR = line2.split( )
                 print (columns_SINR[13])
                 print( columns_SINR[13],columns[1],file=file3)
