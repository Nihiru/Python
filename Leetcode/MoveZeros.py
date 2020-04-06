def moveZeros(ListInput):
    # find the number of zeros in the list and remove them
    #  count = 0
    size = len(ListInput)
    nxt = 0
    for x in ListInput:
       if x != 0:
          ListInput[nxt] = x
          nxt += 1

    x = nxt
    for i in range(len(ListInput[nxt:])):
        ListInput[x] = 0
        x+=1

    print(ListInput)

moveZeros([0,1,0,22,0,2,3,0,4,5])