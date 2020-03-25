print("Paint store program \nSquare meters you gonna paint:")
meters = int(input())

tinL = 18
gallonL = 3.6
tinP = 80
gallonP = 25
finalP = 0
tinQt = 0
gallQt = 0

if meters != 0:
    finalP += 80
    tinQt += 1
    while meters > tinL*6:
        finalP += 80
        tinL += tinL
        tinQt += 1
print("final price only buying {} tins: {}".format(tinQt, finalP))
finalP = 0
tinL = 0
tinP = 0
tinQt = 0

if meters != 0:
    finalP += 25
    gallQt += 1
    while meters > gallonL*6:
        finalP += 25
        gallonL += gallonL
        gallQt += 1
print("final price only buying {} gallons: {}".format(gallQt, finalP))
finalP = 0
gallonL = 0
gallonP = 0
gallQt = 0

if meters != 0:
    while meters*1.1 > 64.8:
        finalP += 80
        gallonL += gallonL
        gallQt += 1
        meters -= 108

    while meters * 1.1 > 0:
        finalP += 25
        tinL += tinL
        tinQt += 1
        meters -= 21.6

print("final price  buying {} gallons and {} tins: {}".format(gallQt, tinQt, finalP))
