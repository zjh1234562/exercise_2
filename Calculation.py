

class Calculation():

    def __init__(self):
        self.operation_dict={  #优先级
            '+':1,
            '-':1,
            'x':2,
            '÷':2,
            '(':3
        }

    def bolan(self,intlist):
        stack=[]
        result=[]
        #intlist=['(',1.0,'+',2.0,')','x',3.0,'÷',4.0]
        #intlists=[1.0 ,'+', 2.0, 'x', 3.0 ,'+', '(',4.0, 'x', 5.0 ,'+', 6.0,')','x',7.0]
        for i in intlist:
            if type(i) is float:
                result.append(i)
            else:
                if stack==[]:
                    stack.append(i)
                else:
                    if i=='(':
                        stack.append(i)

                    elif i==')':
                        while len(stack)>0:
                            op=stack.pop()
                            if op=='(':
                                break
                            else:
                                result.append(op)
                    else:
                        if self.operation_dict.get(stack[-1]) < self.operation_dict.get(i):
                            stack.append(i)
                        else:
                            while len(stack)>0:

                                if self.operation_dict.get(stack[-1]) >=self.operation_dict.get(i) and stack[-1]!='(':
                                    op = stack.pop()
                                    result.append(op)
                                else:
                                    break
                            stack.append(i)
        #print(self.result,self.stack)
        res=result+stack[::-1]
        return res

    def calculation(self,intlist):
        stack=[]
        result=self.bolan(intlist)
        #print(result)
        for j in result:
            if type(j) is float:
                stack.append(j)
            else:
                if j=='+':
                    num1=stack.pop()
                    num2=stack.pop()
                    stack.append(num1+num2)
                elif j=='x':
                    num1=stack.pop()
                    num2=stack.pop()
                    stack.append(num1*num2)
                elif j == '-':
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(num2-num1)
                elif j == '÷':
                    num1 = stack.pop()
                    num2 = stack.pop()

                    stack.append( num2/num1)
        return stack[0]


        



if __name__ == '__main__':
    a=Calculation()
    #a.bolan(['(',1.0,'+',2.0,')','x',3.0,'÷',4.0])

    print(a.calculation([1.0 ,'+', 2.0, 'x', 3.0 ,'+', '(',4.0, 'x', 5.0 ,'+', 6.0,')','x',7.0]))


