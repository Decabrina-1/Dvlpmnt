def move(n,start,finish):
    if n>0:
        tmp=6-start-finish
        if (finish-start)%3 ==1:
            move(n-1,start,tmp)
            print(n,start,finish)
        else:
            move(n-1,start,finish)
            print(n,start,tmp)
            move(n-1,finish,start)
            print(n,tmp,finish)
            move(n-1,start,finish)
move(int(input()),1,3)