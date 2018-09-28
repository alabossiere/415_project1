# function for Euclid's Algorithm
def gcd(x, y):

    j = 0

    while y != 0:
        (x, y) = (y, x % y)
        j = j + 1
    # print "number of mods", j
    # print "gcd is", x
    return j

# function used to calculate average number of modulos for euclids
def avg(x):

    s = 0.0

    for i in range(1, x+1):
        s = s + gcd(x, i,)
        # print(s)
    # print(s/x)
    return s/x


def main():

    print(avg(5))


main()
