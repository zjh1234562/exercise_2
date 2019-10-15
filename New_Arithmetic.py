from Number_generation import *
from write import *
from Calculation import *

class New_Arithmetic():

    def __init__(self,nums_range,n):
        self.number_generation=Number_generation(nums_range)
        self.write=Write2file()
        self.calculation=Calculation()
        #self.strlist=[]
        #self.intlists=[]
        self.n=n   #指定生成题目的数目

    def operator(self):
        operator=['+','-','x','÷']
        return random.sample(operator,random.randint(1,3))

    def chufa(self,strlist,intlist):#被除数不能为0
        chulist= [i for i, v in enumerate(strlist) if v == '÷']
        #print(chulist)
        for i in chulist:
            if strlist[i+1]=='0.0':
                strlist[i+1]='1.0'
                intlist[i+1]=1.0
        #print(strlist,intlist)

    def change(self,strlist,intlist):  #避免出现负数及重复
        for j in 'x+-':
            chulist= [i for i, v in enumerate(strlist) if v == j]
            for i in chulist:
                if float(intlist[i-1])<intlist[i+1]:
                    strlist[i-1],strlist[i+1]=strlist[i+1],strlist[i-1]
                    intlist[i - 1], intlist[i + 1] = intlist[i + 1], intlist[i - 1]
        #print(strlist,intlist)

    def kuohaoiseffective(self,start,end,strlist):#检查加上括号的位置是否有效
        listA=[]
        listB=[]
        for i in range(len(strlist)):
            if strlist[i] in '+-x÷':
                if start<i<end:
                    temp={strlist[i]:i}
                    listA.append(temp)
                else:
                    temp={strlist[i]:i}
                    listB.append(temp)






    def kuohao(self,strlist,intlist,operator_length):#随机插入括号
        lefts = [0, 2, 4]
        rights = [3, 5, 7]

        flag=random.sample([0,1],1)
        if flag==[0]: #随机添加一对括号
            if operator_length == 2:
                rights.remove(7)
                lefts.remove(4)

            index1=random.sample(lefts,1)
            right=[v for i, v in enumerate(rights) if v >= index1[0]+3 ]

            if index1[0]==0:#处理将括号包括整个式子的情况
                if operator_length==2:
                    if 5 in right:
                        right.remove(5)
                else:
                    if 7 in right:
                        right.remove(7)

            index2=random.sample(right,1)

            strlist.insert(index1[0], '(')
            strlist.insert(index2[0]+1, ')')

            intlist.insert(index1[0], '(')
            intlist.insert(index2[0]+1, ')')

            if operator_length==3 and random.sample([0,1],1)==[1]:
                index3,index4=None,None
                if index2[0]+1-index1[0]>4:
                    if random.sample([0,1],1)==[1]:
                        index3=index1[0]+3
                        index4=index3+4
                    else:
                        index3=index1[0]+1
                        index4=index3+4
                # else:
                #     if random.sample([0,1],1)==[1]:
                #         index3=(index1[0]+6)%8
                #         if index3==6:
                #             index4=index3+4
                #         else:
                #             index4=index3+6
                #     else:
                #         index3=index1[0]%4
                #         if index3==

                if index3!=None and index4!=None:
                    strlist.insert(index3, '(')
                    strlist.insert(index4, ')')

                    intlist.insert(index3, '(')
                    intlist.insert(index4, ')')



    def isrepeat(self,answer,answers,strlists):#简单判断是否重复
        if answer in answers[:-1]:
            index=answers.index(answer)
            list1=strlists[index]
            list2=strlists[-1]
            if len(list1)==len(list2):
                return True
            else:
                return False
        else:
            return False




    def New_arithmetic(self):
        strlists,intlists,answers=[],[],[]
        sum=0
        while sum<self.n:
        #for j in range(self.n):
            operator=self.operator()
            operator_length=len(operator)
            num_length=operator_length+1
            strlist=[]
            intlist=[]

            for i in range(num_length+operator_length):
                num_str,num_int=self.number_generation.str_num()
                if i%2==0:#偶数位置放操作数
                    strlist.append(num_str)
                    intlist.append(num_int)
                else:
                    op=operator.pop()
                    strlist.append(op)
                    intlist.append(op)

            self.chufa(strlist,intlist)
            #self.change(strlist,intlist)
            if operator_length>1:
                self.kuohao(strlist,intlist,operator_length)

            #print(strlist)
            try:
                answer=self.calculation.calculation(intlist)
                if answer >= 0:
                    strlists.append(strlist)
                    # intlists.append(intlist)
                    answers.append(answer)

                    if self.isrepeat(answer, answers, strlists) != True:  # 如果不重复
                        sum = sum + 1
                    else:
                        strlists.pop()
                        # intlists.pop()
                        answers.pop()
                else:
                    pass
            except:
                pass



        self.write.write('Exercises.txt', strlists)
        self.write.writeanswer(answers)



if __name__ == '__main__':
    a=New_Arithmetic(50,50)
    a.New_arithmetic()
    # a.change(        ['6.0', '-', '3.0', 'x', '42.0'],
    #     [6.0, '-', 3.0, 'x', 42.0])
    #print(a.isrepeat(12,[12,2],[[1,'+',2],[2,'+',1]]))







