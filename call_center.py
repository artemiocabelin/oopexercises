from datetime import time

class Call(object):

    def __init__(self, caller_id, caller_name, caller_phone_num, hr, min , reason_of_call):
        self.caller_id = caller_id
        self.caller_name = caller_name
        self.caller_phone_num = caller_phone_num
        self.time_of_call = time(hr, min)
        self.reason_of_call = reason_of_call

    def displayCall(self):
        print "Id: " + str(self.caller_id)
        print "Name: " + self.caller_name
        print "Phone Number: " + str(self.caller_phone_num)
        print "Time of Call: " + self.time_of_call
        print "Reason: " + self.reason_of_call


class CallCenter(object):

    def __init__(self, call_list):
        self.call_list = call_list
        self.queue_size = len(call_list)

    def addCall(self,call):
        self.call_list.append(call)
        return self

    def removeCall(self):
        self.call_list.pop(0)
        return self

    def find_and_remove(self,phone_num):
        for i,call in enumerate(self.call_list):
            if call.caller_phone_num == phone_num:
                self.call_list.pop(i)
        return self

    def infoCall(self):
        for call in self.call_list:
            print call.caller_name
            print str(call.caller_phone_num)
            print str(call.time_of_call)
        print len(self.call_list)

    def sort_calls(self):
        for item in range(len(self.call_list)-1,0,-1):
            for i in range(item):
                if self.call_list[i].time_of_call > self.call_list[i+1].time_of_call:
                    temp = self.call_list[i].time_of_call
                    self.call_list[i].time_of_call = self.call_list[i+1].time_of_call
                    self.call_list[i+1].time_of_call = temp

        return self

daisy = Call(1,'Daisy',1231231212,2,30,'emergency')
bob = Call(2,'Bob',1231558812,9,30,'nothin')

someCollection = [daisy,bob]

wait_list = CallCenter(someCollection)

# daisy.displayCall()
# bob.displayCall()
# wait_list.infoCall()

duke = Call(3,'Duke',4532197567,8,30,'inquiry')
tupac = Call(4,'Tupac',3548905142,1,20,'request')

wait_list.addCall(duke).removeCall().addCall(tupac).infoCall()

# wait_list.find_and_remove(4532197567).infoCall()

wait_list.sort_calls().infoCall()
