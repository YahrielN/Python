import numpy
Names = ["Abby", "Raul", "Nick", "Jessica", "Winston"]
Age = numpy.array([14, 17, 32, 34, 40])
i=0

for f in Age:
    print('Name:', Names[i])
    print('Age:', Age[i])
    if Age[i] < 21:
        print('No Access Allowed')
        print('=================')
        i+=1
    else:
        print('Access granted')
        print('================')
        i+=1
