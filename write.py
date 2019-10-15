from fractions import Fraction

class Write2file():


    def write(self,filename,strlists):
        with open(filename,'a')as f:
            for i in strlists:
                for j in i:
                    f.write(j)
                f.write('=\n')

    def writeanswer(self,answers):
        with open('Answers.txt', 'a')as f:
            for answer in answers:
                theint=int(answer)
                thefraction=round(answer-theint,3)

                if theint!=0:
                    if thefraction!=0:
                        answer=str(theint)+'‘'+str(Fraction(str(thefraction)))
                    else:
                        answer=str(theint)
                else:
                    answer=str(Fraction(str(thefraction)))

                f.write(answer)
                f.write('\n')

    def writeGrade(self,wrongsum,correstsum,wronglist,correstlist):
        with open('Grade.txt','w')as f:
            f.write('Wrong:'+str(wrongsum)+"  "+str(wronglist)+'\n')
            f.write('Correct:'+str(correstsum)+'  '+str(correstlist))







if __name__ == '__main__':
    a=Write2file()
    #a.writeanswer(0.3)

