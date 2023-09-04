class MyInteger():
    logdata=[]
    algebralogdata=[]
    def __init__(self,input_1=0):
        if (type(input_1)!=int) and (type(input_1)!=float) and (type(input_1)!=str) and (not isinstance(input_1,MyInteger)):#마지막에 객체한번 넣어보기
            self.value=0
            self.init_value=0
        elif isinstance(input_1,MyInteger):
            self.value=input_1.value
            self.init_value=input_1.value
        else:
            self.value=int(input_1)
            self.init_value=int(input_1)

    def __eq__(self,other):
        if (type(other)==float) or (type(other)==int) or (type(other)==str):
            return self.value==int(other)

        elif isinstance(other,MyInteger):
            return self.value==other.value
        else:
            return False

    def pressAdd(self,input_1):
        if isinstance(input_1,MyInteger):
            self.Add_1=input_1.value
            self.logdata.append(input_1.value)
            self.value+=self.Add_1
            self.algebralogdata.append('Add')
        else:
            self.Add_1=int(input_1)
            self.logdata.append(self.Add_1)
            self.value+=self.Add_1
            self.algebralogdata.append('Add')
        return self.value


    def pressSub(self,input_1):
        if isinstance(input_1,MyInteger):
            self.Sub_1=input_1.value
            self.logdata.append(input_1.value)
            self.value-=self.Sub_1
            self.algebralogdata.append('Sub')
        else:
            self.Sub_1=int(input_1)
            self.logdata.append(self.Sub_1)
            self.value-=self.Sub_1
            self.algebralogdata.append('Sub')
        return self.value

    def getCurrentVariable(self,mode_name='deci'):
        if mode_name =='hex':
            self.new_name=hex(self.value)
        if mode_name =='oct':
            self.new_name=oct(self.value)
        if mode_name =='bin':
            self.new_name=bin(self.value)
        if mode_name =='deci':
            self.new_name=self.value
        return self.new_name
    def resetCurrentVariable(self):
        self.value=0
        self.logdata=[]
        self.algebralogdata=[]
        return 0

    def rollbackCurrentVariable(self):
        if self.algebralogdata!=[]:
            algebra_1=self.algebralogdata.pop()
            log_1=self.logdata.pop()
            if algebra_1=='Sub':
                self.value+=log_1
            else:
                self.value-=log_1
            return self.value
        else:
            self.value=self.init_value
            return self.value

