import time
import random
import itertools
import sys

def traffic_lights():
    thing = itertools.cycle(['green', 'yellow', 'red'])

    while True:
        state = next(thing)
        resp = traffic_light_message(state)
        sys.stdout.write('\r' + resp)
        sys.stdout.flush()
        r = random.randint(0,3)
        time.sleep(2+r)

def traffic_light_message(state):
    if state == 'red':
        return 'The light is red. STOP!'
    if state == 'yellow':
        return 'Caution! The light is yellow. Slow down.'
    if state == 'green':
        return 'The light is green. Go for it!'

traffic_lights()