import re
from fractions import Fraction

from Calculation import *


class Verification():

    def __init__(self):
        self.calcultation=Calculation()
        self.wrongsum=0
        self.correstsum=0
        self.wronglist=[]
        self.correstlist=[]

    def str_to_int(self,str):
        sum=0.0
        str=str.split('‘')
        #print(str)
        for i in str:
            sum=sum+float(Fraction(i))
        return sum

    def getanswer(self,answername):
        answerlist=[]
        with open(answername,'r')as f:
            for i in f.readlines():
                str = i.replace("\n", "")
                num=self.str_to_int(str)
                answerlist.append(num)
        return answerlist

    def gettopicanswer(self,topicname):
        topiclist=[]
        with open(topicname, 'r')as f:
            for i in f.readlines():
                str=i.replace("\n", "").replace("=", "")
                res=re.split(r'([()÷x+-])',str)
                while '' in res:
                    res.remove('')
                for i in range(len(res)):
                    if res[i] not in '()÷x+-':
                        str=res[i]
                        num=self.str_to_int(str)
                        res[i]=num
                temp=self.calcultation.calculation(res)
                topiclist.append(round(temp,3))
        return topiclist

    def verification(self,topicname,answername):
        standard_answers,answers=self.getanswer(answername),self.gettopicanswer(topicname)
        for i in range(len(standard_answers)):
            if abs(standard_answers[i]-answers[i])<=0.01:
                self.correstlist.append(i+1)
                self.correstsum+=1
            else:
                self.wronglist.append(i+1)
                self.wrongsum=+1




if __name__ == '__main__':
    a=Verification()
    a.verification('Exercises.txt','Answers.txt')

    print(a.wrongsum,a.wronglist)
    print(a.correstsum,a.correstlist)