import time
def credit():
    print("                                 -------------------------")
    print("                                 | Created and coded by: |")
    print("                                 |    DRENI MUHAXHERI    |")
    print("                                 |   dreni.mu@gmail.com  |")
    print("                                 -------------------------")
    pause=input("press ENTER to continue...")
    print("")
def HowToPlay():
    print("\n\n\n                ------ HOW TO PLAY ------")
    print("         The game requires two players. Each player")
    print("         takes a turn slotting a tile into the column")
    print("         of their choice. If a player gets four of ")
    print("         their own tiles in a row before the other,")
    print("         they win. The four in a row may be positioned")
    print("         horizontally, vertically or diagonally.")
    print("         Player 1 is 'X' and Player 2 is 'O'.")
    print("                --------------------------\n")
    pause=input("press ENTER to continue...")
    print("")
reset=0
while reset == 0:
    title=0
    while title == 0:
        print("    -- 4 IN A ROW! --\n")
        print("Type 'h' to view how to play...")
        print("Type 'c' to view the credits...")
        print("or Press 'ENTER' to play!")
        play=input("")
        if play == 'h':
            HowToPlay()
        elif play == 'c':
            credit()
        else:
            title=1
    print("\n")
    k=0
    num=0
    total=0
    total1=0
    total2=0
    total3=0
    total4=0
    total5=0
    a=' '
    b=' '
    c=' '
    d=' '
    e=' '
    f=' '
    g=' '
    h=' '
    i=' '
    j=' '
    l=' '
    m=' '
    n=' '
    o=' '
    p=' '
    q=' '
    r=' '
    s=' '
    t=' '
    u=' '
    v=' '
    w=' '
    x=' '
    y=' '
    z=' '
    while k == 0:
        if (num % 2) == 0:
            player='1'
        else:
            player='2'
        num=num+1
        print("\n\nPLAYER:",player,"\n")
        print("  1   2   3   4   5")
        print("|",u,"|",p,"|",z,"|",f,"|",a,"|")
        print("|",v,"|",q,"|",l,"|",g,"|",b,"|")
        print("|",w,"|",r,"|",m,"|",h,"|",c,"|")
        print("|",x,"|",s,"|",n,"|",i,"|",d,"|")
        print("|",y,"|",t,"|",o,"|",j,"|",e,"|")
        k=0
        while k == 0:
            numberloop=0
            while numberloop == 0:
                try:
                    choice=int(input("Pick a number"))
                    numberloop=1
                except ValueError:
                    print("This is NOT a number!")
            numberloop=0
            loop=0
            while loop == 0:
                if 1 > choice or choice > 5:
                    while numberloop == 0:
                        try:
                            choice=int(input("Please pick a number from 1 to 5"))
                            numberloop=1
                        except ValueError:
                            print("This is NOT a number!")
                    numberloop=0
                else:
                    loop=1
            loop=0
            if choice == 1:
                if y == 'X' or y == 'O':                                          #make sure the player's choice works physically
                    if x == 'X' or x == 'O':
                        if w == 'X' or w == 'O':
                            if v == 'X' or v == 'O':
                                if u == 'X' or u == 'O':
                                    print("This column is full...")#                       1
                                else:
                                    if player == '1':
                                        u = 'X'
                                    else:
                                        u = 'O'
                                    k=1
                                    total1=1
                            else:
                                if player == '1':
                                    v = 'X'
                                else:
                                    v = 'O'
                                k=1
                        else:
                            if player == '1':
                                w = 'X'
                            else:
                                w = 'O'
                            k=1
                    else:
                        if player == '1':
                            x = 'X'
                        else:
                            x = 'O'
                        k=1
                else:
                    if player == '1':
                        y = 'X'
                    else:
                        y = 'O'
                    k=1
            if choice == 2:
                if t == 'X' or t == 'O':
                    if s == 'X' or s == 'O':
                        if r == 'X' or r == 'O':
                            if q == 'X' or q == 'O':
                                if p == 'X' or p == 'O':
                                    print("This column is full...")#                      2
                                else:
                                    if player == '1':
                                        p = 'X'
                                    else:
                                        p = 'O'
                                    k=1
                                    total2=1
                            else:
                                if player == '1':
                                    q = 'X'
                                else:
                                    q = 'O'
                                k=1
                        else:
                            if player == '1':
                                r = 'X'
                            else:
                                r = 'O'
                            k=1
                    else:
                        if player == '1':
                            s = 'X'
                        else:
                            s = 'O'
                        k=1
                else:
                    if player == '1':
                        t = 'X'
                    else:
                        t = 'O'
                    k=1
            if choice == 3:
                if o == 'X' or o == 'O':
                    if n == 'X' or n == 'O':
                        if m == 'X' or m == 'O':
                            if l == 'X' or l == 'O':
                                if z == 'X' or z == 'O':
                                    print("This column is full...")#                       3
                                else:
                                    if player == '1':
                                        z = 'X'
                                    else:
                                        z = 'O'
                                    k=1
                                    total3=1
                            else:
                                if player == '1':
                                    l = 'X'
                                else:
                                    l = 'O'
                                k=1
                        else:
                            if player == '1':
                                m = 'X'
                            else:
                                m = 'O'
                            k=1
                    else:
                        if player == '1':
                            n = 'X'
                        else:
                            n = 'O'
                        k=1
                else:
                    if player == '1':
                        o = 'X'
                    else:
                        o = 'O'
                    k=1
            if choice == 4:
                if j == 'X' or j == 'O':
                    if i == 'X' or i == 'O':
                        if h == 'X' or h == 'O':
                            if g == 'X' or g == 'O':
                                if f == 'X' or f == 'O':
                                    print("This column is full...")#                     4
                                else:
                                    if player == '1':
                                        f = 'X'
                                    else:
                                        f = 'O'
                                    k=1
                                    total4=1
                            else:
                                if player == '1':
                                    g = 'X'
                                else:
                                    g = 'O'
                                k=1
                        else:
                            if player == '1':
                                h = 'X'
                            else:
                                h = 'O'
                            k=1
                    else:
                        if player == '1':
                            i = 'X'
                        else:
                            i = 'O'
                        k=1
                else:
                    if player == '1':
                        j = 'X'
                    else:
                        j = 'O'
                    k=1
            if choice == 5:
                if e == 'X' or e == 'O':
                    if d == 'X' or d == 'O':
                        if c == 'X' or c == 'O':
                            if b == 'X' or b == 'O':
                                if a == 'X' or a == 'O':
                                    print("This column is full...")#                      5
                                else:
                                    if player == '1':
                                        a = 'X'
                                    else:
                                        a = 'O'
                                    k=1
                                    total5=1
                            else:
                                if player == '1':
                                    b = 'X'
                                else:
                                    b = 'O'
                                k=1
                        else:
                            if player == '1':
                                c = 'X'
                            else:
                                c = 'O'
                            k=1
                    else:
                        if player == '1':
                            d = 'X'
                        else:
                            d = 'O'
                        k=1
                else:
                    if player == '1':
                        e = 'X'
                    else:
                        e = 'O'
                    k=1
        k=0
        if u == 'X' and v == 'X' and w == 'X' and x == 'X':                 #all vertical possible wins
            k=1
        if u == 'O' and v == 'O' and w == 'O' and x == 'O':
            k=1
        if v == 'X' and w == 'X' and x == 'X' and y == 'X':
            k=1
        if v == 'O' and w == 'O' and x == 'O' and y == 'O':
            k=1
        if p == 'X' and q == 'X' and r == 'X' and s == 'X':
            k=1
        if p == 'O' and q == 'O' and r == 'O' and s == 'O':
            k=1
        if t == 'X' and q == 'X' and r == 'X' and s == 'X':
            k=1
        if t == 'O' and q == 'O' and r == 'O' and s == 'O':
            k=1
        if z == 'X' and l == 'X' and m == 'X' and n == 'X':
            k=1
        if z == 'O' and l == 'O' and m == 'O' and n == 'O':
            k=1
        if o == 'X' and l == 'X' and m == 'X' and n == 'X':
            k=1
        if o == 'O' and l == 'O' and m == 'O' and n == 'O':
            k=1
        if f == 'X' and g == 'X' and h == 'X' and i == 'X':
            k=1
        if f == 'O' and g == 'O' and h == 'O' and i == 'O':
            k=1
        if j == 'X' and g == 'X' and h == 'X' and i == 'X':
            k=1
        if j == 'O' and g == 'O' and h == 'O' and i == 'O':
            k=1
        if a == 'X' and b == 'X' and c == 'X' and d == 'X':
            k=1
        if a == 'O' and b == 'O' and c == 'O' and d == 'O':
            k=1
        if e == 'X' and b == 'X' and c == 'X' and d == 'X':
            k=1
        if e == 'O' and b == 'O' and c == 'O' and d == 'O':
            k=1
        if u == 'X' and p == 'X' and z == 'X' and f == 'X':                  #all horizontal possible wins
            k=1
        if u == 'O' and p == 'O' and z == 'O' and f == 'O':
            k=1
        if a == 'X' and p == 'X' and z == 'X' and f == 'X':
            k=1
        if a == 'O' and p == 'O' and z == 'O' and f == 'O':
            k=1
        if v == 'X' and q == 'X' and l == 'X' and g == 'X':
            k=1
        if v == 'O' and q == 'O' and l == 'O' and g == 'O':
            k=1
        if b == 'X' and q == 'X' and l == 'X' and g == 'X':
            k=1
        if b == 'O' and q == 'O' and l == 'O' and g == 'O':
            k=1
        if w == 'X' and r == 'X' and m == 'X' and h == 'X':
            k=1
        if w == 'O' and r == 'O' and m == 'O' and h == 'O':
            k=1
        if c == 'X' and r == 'X' and m == 'X' and h == 'X':
            k=1
        if c == 'O' and r == 'O' and m == 'O' and h == 'O':
            k=1
        if x == 'X' and s == 'X' and n == 'X' and i == 'X':
            k=1
        if x == 'O' and s == 'O' and n == 'O' and i == 'O':
            k=1
        if d == 'X' and s == 'X' and n == 'X' and i == 'X':
            k=1
        if d == 'O' and s == 'O' and n == 'O' and i == 'O':
            k=1
        if y == 'X' and t == 'X' and o == 'X' and j == 'X':
            k=1
        if y == 'O' and t == 'O' and o == 'O' and j == 'O':
            k=1
        if e == 'X' and t == 'X' and o == 'X' and j == 'X':
            k=1
        if e == 'O' and t == 'O' and o == 'O' and j == 'O':
            k=1
        if x == 'X' and r == 'X' and l == 'X' and f == 'X':                   #all diagonal possible wins
            k=1
        if x == 'O' and r == 'O' and l == 'O' and f == 'O':
            k=1
        if y == 'X' and s == 'X' and m == 'X' and g == 'X':
            k=1
        if y == 'O' and s == 'O' and m == 'O' and g == 'O':
            k=1
        if a == 'X' and s == 'X' and m == 'X' and g == 'X':
            k=1
        if a == 'O' and s == 'O' and m == 'O' and g == 'O':
            k=1
        if t == 'X' and n == 'X' and h == 'X' and b == 'X':
            k=1
        if t == 'O' and n == 'O' and h == 'O' and b == 'O':
            k=1
        if j == 'X' and n == 'X' and r == 'X' and v == 'X':
            k=1
        if j == 'O' and n == 'O' and r == 'O' and v == 'O':
            k=1
        if e == 'X' and i == 'X' and m == 'X' and q == 'X':
            k=1
        if e == 'O' and i == 'O' and m == 'O' and q == 'O':
            k=1
        if u == 'X' and i == 'X' and m == 'X' and q == 'X':
            k=1
        if u == 'O' and i == 'O' and m == 'O' and q == 'O':
            k=1
        if d == 'X' and h == 'X' and l == 'X' and p == 'X':
            k=1
        if d == 'O' and h == 'O' and l == 'O' and p == 'O':
            k=1
        total=total1+total2+total3+total4+total5
        if total == 5:
            k=1
    print("\n\n\n\n\n\n\n\n\n\n\n\n  1   2   3   4   5")
    print("|",u,"|",p,"|",z,"|",f,"|",a,"|")
    print("|",v,"|",q,"|",l,"|",g,"|",b,"|")
    print("|",w,"|",r,"|",m,"|",h,"|",c,"|")
    print("|",x,"|",s,"|",n,"|",i,"|",d,"|")
    print("|",y,"|",t,"|",o,"|",j,"|",e,"|")
    if total == 5:
        print("\n\nIt's a tie. You filled up the table.")
    else:
        print("\n\nPLAYER",player,"WINS!")
    print("\n\nWould you like to play again?")
    replay=input("Please type 'y' for yes or just press 'ENTER' to continue.")
    if replay == 'y':
        print("Replaying in 2 seconds...")
        time.sleep(2)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    else:
        exit()
