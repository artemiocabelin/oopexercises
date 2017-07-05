class Underscore(object):

    def map(self, func, seq):
        newSeq = []
        for i,item in enumerate(seq):
            newSeq.append(func(seq[i]))
        print newSeq
        return newSeq

    def reduce(self, func, seq):
        if len(seq) < 2:
            print func(seq[0])
            return func(seq[0])

        newEl = func(seq[0], seq[1])
        i = 2
        while i < len(seq):
            newEl = func(newEl,seq[i])
            i+=1
        print newEl
        return newEl

    def find(self, targetStr, sample, beg, end):
        i = beg
        length = end
        while i < length:
            if targetStr[i] == sample[0]:
                start = i
                j=0
                while j < len(sample):
                    if targetStr[start+j] != sample[j]:
                        break
                    elif targetStr[start+j] == sample[j] and j == len(sample)-1:
                        print start
                        return start
                    else:
                        j+=1
            i += 1
        print "Not found"
        return ""

    def filter(self, func, seq):
        newSeq = []
        for i,item in enumerate(seq):
            if not isinstance(func(item),bool):
                break
            elif func(item) == True:
                newSeq.append(seq[i])
        print newSeq
        return newSeq

    def reject(self,seq,func):
        newList = []
        for i,item in enumerate(seq):
            if not func(item):
                newList.append(seq[i])
        print newList
        return newList

_ = Underscore()
# evens = 

_.filter(lambda x: x % 2 == 0,[1,2,3,4,5,6])

_.map(lambda x: x + 2, [1,2,3,4,5,6])

_.reduce(lambda x,y: x+y, [47,11,42,13])

_.find("this is string example....wow!!!","exam",0,len("this is string example....wow!!!"))

_.reject([1, 2, 3, 4, 5, 6], lambda num: num % 2 == 0 )