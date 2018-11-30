import xlrd

f = open("outfile.txt",'w')
boon = xlrd.open_workbook('boonli.xls')
ps = xlrd.open_workbook('powerschool.xlsx')
for sheet2 in boon.sheets():
    for row2 in range(3,sheet2.nrows):
        for sheet1 in ps.sheets():  
            for row1 in range(1,sheet1.nrows):

                pfname = str(sheet1.cell(row1,1)).lower()
                plname = str(sheet1.cell(row1,2)).lower()
                bfname = str(sheet2.cell(row2,2)).lower()
                blname = str(sheet2.cell(row2,3)).lower()
                ID = sheet1.cell(row1,3)
                if (pfname == bfname and plname == blname):
                    #print "first name match and last name match"
                    #print ID
                    f.write(str(ID) + '\n')
##                    print "ps name",row1, str(pfname), plname 
##                    print "boonli name",row2 , str(bfname), blname
                    break
                elif(row1 == sheet1.nrows-1): f.write('\n')
f.close()
                

