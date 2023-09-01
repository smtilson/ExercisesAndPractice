test='''
3,4,3,1,2
'''

input='''
3,1,4,2,1,1,1,1,1,1,1,4,1,4,1,2,1,1,2,1,3,4,5,1,1,4,1,3,3,1,1,1,1,3,3,1,3,3,1,5,5,1,1,3,1,1,2,1,1,1,3,1,4,3,2,1,4,3,3,1,1,1,1,5,1,4,1,1,1,4,1,4,4,1,5,1,1,4,5,1,1,2,1,1,1,4,1,2,1,1,1,1,1,1,5,1,3,1,1,4,4,1,1,5,1,2,1,1,1,1,5,1,3,1,1,1,2,2,1,4,1,3,1,4,1,2,1,1,1,1,1,3,2,5,4,4,1,3,2,1,4,1,3,1,1,1,2,1,1,5,1,2,1,1,1,2,1,4,3,1,1,1,4,1,1,1,1,1,2,2,1,1,5,1,1,3,1,2,5,5,1,4,1,1,1,1,1,2,1,1,1,1,4,5,1,1,1,1,1,1,1,1,1,3,4,4,1,1,4,1,3,4,1,5,4,2,5,1,2,1,1,1,1,1,1,4,3,2,1,1,3,2,5,2,5,5,1,3,1,2,1,1,1,1,1,1,1,1,1,3,1,1,1,3,1,4,1,4,2,1,3,4,1,1,1,2,3,1,1,1,4,1,2,5,1,2,1,5,1,1,2,1,2,1,1,1,1,4,3,4,1,5,5,4,1,1,5,2,1,3
'''

class LFish:
    def __init__(self, timer):
        self.timer = timer
    def __str__(self):
        return f'LFish with {self.timer} days left in cycle.'
    def __repr__(self):
        return f'LFish(timer={self.timer})'
    def cycle(self):
        self.timer-=1
        if self.timer==-1:
            self.timer=6

class LSchool:
    def __init__(self,d0,d1,d2,d3,d4,d5,d6,d7,d8):
        self.d0 = d0
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
        self.d4 = d4
        self.d5 = d5
        self.d6 = d6
        self.d7 = d7
        self.d8 = d8
    def cycle(self):
        new_d0 = self.d1
        new_d1 = self.d2
        new_d2 = self.d3
        new_d3 = self.d4
        new_d4 = self.d5
        new_d5 = self.d6
        new_d6 = self.d7+self.d0
        new_d7 = self.d8
        new_d8 = self.d0
        self.d0 = new_d0
        self.d1 = new_d1
        self.d2 = new_d2
        self.d3 = new_d3
        self.d4 = new_d4
        self.d5 = new_d5
        self.d6 = new_d6
        self.d7 = new_d7
        self.d8 = new_d8
    def total(self):
        return self.d0+self.d1+self.d2+self.d3+self.d4+self.d5+self.d6+self.d7+self.d8
    def __repr__(self):
        return f'{self.d0,self.d1,self.d2, self.d3, self.d4,self.d5,self.d6,self.d7,self.d8}'

def convert(data):
    clean=data.splitlines()
    while '' in clean:
        clean.remove('')
    clean=clean[0].split(',')
    d0=clean.count('0')
    d1=clean.count('1')
    d2=clean.count('2')
    d3=clean.count('3')
    d4=clean.count('4')
    d5=clean.count('5')
    d6=clean.count('6')
    d7=clean.count('7')
    d8=clean.count('8')
    School=LSchool(d0,d1,d2,d3,d4,d5,d6,d7,d8)
    return School

def progress_1_day(Fishes):
    new_fishes=[]
    for fish in Fishes:
        if fish.timer==0:
            new_fishes.append(LFish(timer=8))
        fish.cycle()
    return Fishes.extend(new_fishes)

def everything(data):
    school = convert(data)
    #Fishes=[LFish(timer=x) for x in data]
    run_experiment(18, school)
    school = convert(data)
    run_experiment(80, school)
    school = convert(data)
    run_experiment(256, school)

def run_experiment(days, school):
    for day in range(days):
        school.cycle()
        #print(school.total(), school)

        #if day%25==0:
            #print(f'at day {day} there are {school.total()}')
        #print(f'there are currently {len(Fishes)} fishes.')
    print(f"After {days} days, there are {school.total()} fishes.")

#everything(test)
everything(input)
