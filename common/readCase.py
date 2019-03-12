import os
import xlrd
import re
from common.login import login

pwd=os.getcwd()
testcase_file=os.path.join(pwd,"testcase.xlsx")



class ReadCase(object):

    def __init__(self,interfacename,casename,casefile):
        self.interfacename=interfacename
        # print(self.interfacename)
        self.casename=casename
        # print(self.casename)
        data=xlrd.open_workbook(casefile,formatting_info=True)
        self.sheet=data.sheet_by_name(self.interfacename)


    def read_case_info(self):
        caseinfo=self.get_case_info()
        # print (caseinfo)
        for i in caseinfo:
            data = {}
            if i[3]!="":
                h=i[3].strip()
                i[3]=h
            if "=" in i[4]:
                data1 = i[4].split(",")
                for t in data1:
                    data2 = t.split("=")
                    data[data2[0]] = data2[1].strip()
                i[4] = data
            else:
                data = i[4].strip()
                i[4] = data
        # print("YYYYYYYYYYYYYYYYY")
        # print (caseinfo)
        return caseinfo


    def get_case_info(self):
        merged_list = self.sheet.merged_cells
        print(merged_list)
        rows_num=self.sheet.nrows
        cols_num=self.sheet.ncols
        mergejson={}
        caseinfo=[]
        info = []
        t=0
        for r in range(rows_num):
            rowvalue=self.sheet.row_values(r)
            t=0
            for mer in merged_list:
                if mer[2]==0:
                    if r>=mer[0] and r<mer[1] :
                         t=t+1
                         if rowvalue[0]==self.casename:
                             caseinfo.append(rowvalue)
                             for i in range(r+1,mer[1]):
                                 # print(i)
                                 if self.sheet.row_values(i)[0] is None or self.sheet.row_values(i)[0] == '':
                                     caseinfo.append(self.sheet.row_values(i))
                                 else:
                                     break
                         else:
                             continue
                    else:
                        continue
                else:
                    continue
            if t==0:
                if rowvalue[0]==self.casename:
                    caseinfo.append(rowvalue)
                else:
                    continue
        return caseinfo
    # def add_token(self):
    #     t=[]
    #     if self.interfacename !="verification_code":
    #         token=login()
    #         print(token)
    #         colvalue = self.sheet.col_values(3)
    #         for i in colvalue:
    #             if i!='head':
    #                 print(i)
    #                 print("'Authorization': %s" %token)
    #                 i=i.replace("'Authorization':''","'Authorization': %s" %token)
    #                 t.append(i)
    #             else:
    #                 pass
    #     return t
def add_token():
    token=login()
    return token
t=ReadCase('userinfo','','C:\myprojects\interfacetest\common\\testcase.xlsx')
# R=t.get_case_info()
# print(R)









