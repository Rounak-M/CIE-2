import sys

if len (sys.argv) == 5:
    p1 = sys.argv [1]
    p2 = sys.argv [2]
    p3 = sys.argv [3]
    p4 = sys.argv [4]

else:
    p1 = 0
    p2 = 0
    p3 = 0
    p4 = 0

avg = p1 + p2 + p3 + p4 / 4

if (avg > 0):
    print (f"Average Price: ", {avg})

else:
    print ("Please provide 4 prices please.")