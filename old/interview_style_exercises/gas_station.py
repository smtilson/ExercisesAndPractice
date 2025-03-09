'''
we want to traverse a cycle of gas stations.
gs is a list where there is gas[i] fuel available
cost is a list where cost[i] is how much fuel it takes to go from i to i+1
'''

class Car:
    def __init__(self,pos):
        self.pos=pos
        self.gas_tank = 0
    def fill_up(self, gas):
        print(f'current tank:{self.gas_tank}.')
        self.gas_tank+=gas[self.pos]
        print(f'tank filled up to {self.gas_tank}')
    def drive(self,cost):
        print(f'want to leave from {self.pos}.')
        print(f'this costs {cost[self.pos]}.')
        print(f'we have {self.gas_tank}')
        if cost[self.pos]<=self.gas_tank:
            self.gas_tank-=cost[self.pos]
            if self.pos == len(cost)-1:
                self.pos = 0
            else:
                self.pos += 1
            return True
        else:
            print('The journey has ended')
            self.gas_tank=0
            return False

def find_start(gas, cost):
    n=len(gas)
    test_car = Car(pos=0)
    for i in range(n):
        start=i
        print(f'start is {i}')
        test_car.pos = i
        test_car.fill_up(gas)
        while test_car.gas_tank>0:
            if not test_car.drive(cost):
                break
            if start == test_car.pos:
                print('we have come back to where we started.')
                return i
            test_car.fill_up(gas)
    return -1

gas=[1,5,3,3,5,3,1,3,4,5]
cost = [5,2,2,8,2,4,2,5,1,2]

print(find_start(gas,cost))


