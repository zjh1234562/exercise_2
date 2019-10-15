import sys
from New_Arithmetic import *
from verification import Verification
from write import Write2file

def main():
    parameters=sys.argv[1:]
    #print(parameters)
    if parameters[0]=='-h' and len(parameters)==1:
        print("四则运算生成程序文档：\n")
        print("参数：-r,指定数值范围\n")
        print("     -n,指定生成题目的数量,默认为10\n")
        print("     -h,查看帮助\n")
        print("     -e,指定读取题目文件\n")
        print("     -a,指定读取答案文件\n")
    else:
        if '-e' in parameters and '-a' in parameters:
            vis=Verification()
            exercisesfile,answersfile=parameters[parameters.index('-e')+1],parameters[parameters.index('-a')+1]
            vis.verification(exercisesfile,answersfile)
            wr=Write2file()
            wr.writeGrade(vis.wrongsum,vis.correstsum,vis.wronglist,vis.correstlist)
        else:

            if '-r' not in parameters:
                print("请输入-r，指定数值范围！运行python xxx.py -h查看帮助")
            else:
                try:
                    if '-n' in parameters:
                        n=int(parameters[parameters.index('-n')+1])
                    else:
                        n=10
                    r=int(parameters[parameters.index('-r')+1])

                    generations=New_Arithmetic(r, n)
                    generations.New_arithmetic()
                except Exception as e:
                    print(e)


if __name__ == '__main__':
    main()