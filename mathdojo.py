class MathDojo(object):

    def __init__(self):
        self.final = 0

    def add(self, num, *nums):
        total = 0
        if isinstance(num,list) or isinstance(num,tuple):
            for i in num:
                total += i
            self.final = self.final + total
        else:
            self.final = self.final + num
            
        if nums:
            count = 0
            for item in nums:
                if isinstance(item,list) or isinstance(num,tuple):
                    for j in item:
                        count += j
                else:
                    count += item
            self.final = self.final + count
            return self
        return self


    def subtract(self, num, *nums):
        if isinstance(num,list) or isinstance(num,tuple):
            total = 0
            for i in num:
                total += i
            self.final = self.final - total
        else:
            self.final = self.final - num


        if nums:
            count = 0
            for item in nums:
                if isinstance(item,list) or isinstance(num,tuple):
                    for j in item:
                        count += j
                else:
                    count += item
            self.final = self.final - count
            return self
        return self
    
    def displayResult(self):
        print self.final



MathDojo().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).displayResult()


MathDojo().add(2).add(2, 5).subtract(3, 2).displayResult()
