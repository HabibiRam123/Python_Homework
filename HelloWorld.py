print("Hello World")
print("We are currently using github")

import random
def cd_gen(times = 1):
    for x in range(times):
        a =(random.random())
        b = (random.randint(40,100))

        c = (round(a + b, 2))

        cd_list = ["N", "E", "S", "W", "SE", "SW", "NW", "NE"]

        cd = random.choice(cd_list)
        return(str(c) + "°" + cd)
cd_gen(5)
print("Food is currently being sent to",cd_gen(1))