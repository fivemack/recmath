#!/usr/bin/python3

def unhex(u):
    v=0
    for k in range(len(u)):
        v=v+(16**k)*int(u[len(u)-k-1])
    return v

def scan(start, digs):
    left=start+"0"*digs
    right=start+"9"*digs
    ld=unhex(left)/int(left)
    rd=unhex(right)/int(right)
    if (digs==1):
#        print([start, left, right, ld, rd])
        multiplier=int(ld+0.5)
        left_disc=unhex(left)-multiplier*int(left)
        right_disc=unhex(right)-multiplier*int(right)
#        print(left_disc, right_disc, left_disc%(multiplier-1))
        if(left_disc>=0 and right_disc<=0 and left_disc%(multiplier-1)==0):
            print(["SUCCESS!",start+str(left_disc//(multiplier-1)),multiplier])

    if (int(ld)!=int(rd)):
        # print([start, digs, ld, rd])
        for nd in range(10):
            scan(start+str(nd), digs-1)

for dogs in range(20):
    for u in range(1,10):
        scan(str(u),dogs)