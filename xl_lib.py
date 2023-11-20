from xlrd import open_workbook

def read_locators(sheetname):
    objects={}
    wb=open_workbook("D:\\htmlfiles\\objects.xls")
    ws=wb.sheet_by_name(sheetname)
    rows=ws.nrows
    for i in range(1,rows):
        data=ws.row_values(i)
        objects[data[0]]=(data[1],data[2])
    return objects
    

def read_data(sheetname,testcasename):

    wb=open_workbook("D:\\htmlfiles\\testdata.xls")
    ws=wb.sheet_by_name(sheetname)
    rows=ws.nrows
    final_data=[]

    for i in range(0,rows):
        temp=ws.row_values(i)
        if temp[0]==testcasename:
            data=ws.row_values(i)
            data=[item for item in data if item]
            data=[item for item in data if data[1]=="Yes"]
            if data:
                final_data.append(tuple(data[2:]))
    return final_data

