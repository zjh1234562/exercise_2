import random
from fractions import Fraction

class Number_generation():

    def __init__(self,nums_range):
        self.nums_range=nums_range


    def new_num(self):
        nums_types=['int','improper_fraction','proper_fraction']
        nums_type=random.sample(nums_types,1)
        if nums_type[0]=='int':
            return random.randint(0,self.nums_range),1
        elif nums_type[0]=='proper_fraction':
            molecule = random.randint(1, self.nums_range)
            denominator = random.randint(1, self.nums_range)
            if molecule>denominator:
                molecule,denominator=denominator,molecule
            return molecule,denominator
        else:
            molecule = random.randint(1, self.nums_range)
            denominator = random.randint(1, self.nums_range)
            if molecule<denominator:
                molecule,denominator=denominator,molecule
            return molecule,denominator

    def str_num(self):
        molecule, denominator=self.new_num()
        theint = molecule // denominator  # 整数部分
        thefraction = molecule % denominator
        if thefraction==0:
            res=str(molecule/denominator)
        else:
            if theint==0:
                res=str(molecule)+'/'+str(denominator)
            else:
                res=str(theint)+'‘' +str(thefraction)+'/'+str(denominator)

        return res,molecule/denominator






if __name__ == '__main__':
    pass

