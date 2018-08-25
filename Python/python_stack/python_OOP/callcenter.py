from datetime import datetime


class Calls(object):
    def __init__(self, id, caller_name, caller_number, time_call, reason_call):
        self.id = id
        self.caller_name = caller_name
        self.caller_number = caller_number
        self.time_call = time_call
        self.reason_call = reason_call
        self.create_at = datetime.now()

    def display(self):
        print "id is {}, caller name is {}, caller number is {}, time" \
              " call is {}, reason for calling is {}".format(self.id, self.caller_name, self.caller_number, self.time_call, self.reason_call)
        return self


class CallCenter(object):
    def __init__(self, *calls):
        self.calls = []
        for call in calls:
            self.calls.append(call)
        self.queue = len(self.calls)

    def add_calls(self, *new_call):
        self.calls += new_call
        self.queue = len(self.calls)
        return self

    def remove_calls(self):
        self.calls = self.calls[1:]
        self.queue = len(self.calls)
        return self

    def find_remove(self, number):
        for num in range(len(self.calls)-1):
            if self.calls[num].caller_number == number:
                self.calls.pop(num)
        self.queue = len(self.calls)
        return self

    def info(self):
        for call in self.calls:
            print "name: {} , phone number: {}, create at {}".format(call.caller_name, call.caller_number, call.create_at)
        print "queue length is {} \n".format(self.queue)


amy = Calls(1, "amy", 2015551234, "4 min", "complain about the self-serve manual")
jason = Calls(2, "jason", 5296354159,"20 min", "register a new payment account")
jimmy = Calls(3, "jimmy", 2153654789, "16 min", "purchase 10k worth of e-harmony poster")
"""
amy.display()
jason.display()
jimmy.display()

NYC_Center.info()
NYC_Center.add_calls(jimmy)

NYC_Center.info()
NYC_Center.remove_calls()
NYC_Center.info()
NYC_Center.add_calls(amy, jimmy)
NYC_Center.info()
"""
NYC_Center = CallCenter(amy, jason)
NYC_Center.find_remove(2015551234)
NYC_Center.info()
