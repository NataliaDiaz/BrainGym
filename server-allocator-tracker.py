# # Problem 1:
# # https://gist.github.com/ChimeraCoder/1906326162eb88742952
#
# You're running a pool of servers where the servers are numbered sequentially starting from 1. Over time, any given server might explode, in which case its server number is made available for reuse. When a new server is launched, it should be given the lowest available number.
#
# Write a function which, given the list of currently allocated server numbers, returns the number of the next server to allocate. In addition, you should demonstrate your approach to testing that your function is correct. You may choose to use an existing testing library for your language if you choose, or you may write your own process if you prefer.
#
# For example, your function should behave something like the following:
#
#   >> next_server_number([5, 3, 1])
#   2
#   >> next_server_number([5, 4, 1, 2])
#   3
#   >> next_server_number([3, 2, 1])
#   4
#   >> next_server_number([2, 3])
#   1
#   >> next_server_number([])
#   1

def next_server_number(running):
    if running:
        s = 1
        while True:
            if not s in running:
                return s
            s +=1
    else:
        return 1


print next_server_number([5, 3, 1])
print next_server_number([5, 4, 1, 2])
print next_server_number([3, 2, 1])
print next_server_number([2, 3])
print next_server_number([])



"""
Part 2:
  https://gist.github.com/antifuchs/dd5344b60693dd1d073b

Server names consist of an alphabetic host type (e.g. "apibox") concatenated with the server number, with server numbers allocated as before (so "apibox1", "apibox2", etc. are valid hostnames).

Write a name tracking class with two operations, allocate(host_type) and deallocate(hostname). The former should reserve and return the next available hostname, while the latter should release that hostname back into the pool.

For example:

>> tracker = Tracker.new()
>> tracker.allocate("apibox")
"apibox1"
>> tracker.allocate("apibox")
"apibox2"
>> tracker.deallocate("apibox1")
nil
>> tracker.allocate("apibox")
"apibox1"
>> tracker.allocate("sitebox")
"sitebox1"
"""

class Tracker:
    name2number = {}

    def allocate(self, name):
        if name in self.name2number.keys():
            number = next_server_number(self.name2number[name])
            allocated = name+ str(number)
            self.name2number[name].append(number)
        else:
            number = next_server_number([])
            allocated = name+ str(number)
            self.name2number[name] = []
            self.name2number[name].append(number)
        return allocated

    def deallocate(self, name):
        keys = self.name2number.keys()
        for k in keys:
            if k in keys:
                host_type = k
                break
        if host_type in self.name2number.keys():#running:
            #self.running.remove(name)  ### ATTENTION: THIS RETURNS NONE !
            number = self.extract_nr(name)
            self.name2number[host_type].remove(number)
        return "nil"

    def extract_nr(self, name):
        i = len(name) -1
        while name[i]>='0' and name[i] <='9':
            i -=1
        number = name[i+1:]
        return int(str(number))



t = Tracker()
print t.extract_nr('apibox134')

print t.allocate("apibox")
print t.allocate("apibox")
print t.deallocate("apibox1")
print t.allocate("apibox")
print t.allocate("sitebox")
