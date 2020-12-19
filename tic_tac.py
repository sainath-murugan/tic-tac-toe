print("// play tic tac toe///")
name_of_player_1 = input("enter the name of player one\n")
name_of_player_2 = input("enter the name of player two\n")
b = ['-', '-', '-',
     '-', '-', '-',
     '-', '-', '-']

def tic_tac():
    
    print(b[0] + "|" + b[1] + "|" + b[2])
    print(b[3] + "|" + b[4] + "|" + b[5])
    print(b[6] + "|" + b[7] + "|" + b[8])

tic_tac()

one = True
while one == True:
    player_1 = int(input(" player 1's turn\nenter a value between 1 - 9\n"))
    if player_1 in [1, 2, 3, 4, 5, 6, 7, 8, 9]:

        if player_1 == 1:
          if b[0] == "o":
              print("the place was taken by player2")

          else:
             b[0] = "x"
             tic_tac()
             if b[0:3] == ["x", "x", "x"]:
                 print(f"{name_of_player_1} won the match")
                 break
             elif b[0] == b[3] == b[6]:
                print(f"{name_of_player_1} won the match")
                break
             elif b[0] == b[4] == b[8]:
                 print(f"{name_of_player_1} won the match")
                 break


        elif player_1 == 2:
            if b[1] == "o":
                print("the place was taken by player_2")

            else:
             b[1] = "x"
             tic_tac()
             if b[0:3] == ["x", "x", "x"]:
                 print(f"{name_of_player_1} won the match")
                 break
             elif b[1] == b[4] == b[7]:
                 print(f"{name_of_player_1} won the match")
                 break



        elif player_1 == 3:
            if b[2] == "o":
                print("the place was taken by player2")
            else:
             b[2] = "x"
             tic_tac()
             if b[0:3] == ["x", "x", "x"]:
                 print(f"{name_of_player_1} won the match")
                 break
             elif b[2] == b[5] == b[8] :
                 print(f"{name_of_player_1} won the match")
                 break
             elif b[2] == b[4] == b[6]:
                 print(f"{name_of_player_1} won the match")
                 break

        elif player_1 == 4:
            if b[3] == "o":
                print("the place was taken by player2")
            else:
             b[3] = "x"
             tic_tac()

             if b[3:6] == ["x", "x", "x"] :
                 print(f"{name_of_player_1} won the match")
                 break
             elif b[0] == b[3] == b[6]:
                 print(f"{name_of_player_1} won the match")
                 break

        elif player_1 == 5:
           if b[4] == "o":
               print("the place was taken by player2")
           else:
            b[4] = "x"
            tic_tac()
            if b[3:6] == ["x", "x", "x"]:
                print(f"{name_of_player_1} won the match")
                break
            elif b[1] == b[4] == b[7]:
                print(f"{name_of_player_1} won the match")
                break
            elif b[0] == b[4] == b[8] :
                print(f"{name_of_player_1} won the match")
                break
            elif b[2] == b[4] == b[6] :
                print(f"{name_of_player_1} won the match")
                break



        elif player_1 == 6:
            if b[5] == "o":
                print("the place was taken by player2")
            else:
             b[5] = "x"
             tic_tac()
             if b[3:6] == ["x", "x", "x"]:
                 print(f"{name_of_player_1} won the match")
                 break
             elif b[2] == b[5] == b[8] :
                 print(f"{name_of_player_1} won the match")
                 break


        elif player_1 == 7:
            if b[6] == "o":
                print("the place was taken by player2")
            else:
             b[6] = "x"
             tic_tac()
             if b[6] == b[7] == b[8]:
                 print(f"{name_of_player_1} won the match")
                 break

             elif b[6] == b[3] == b[0] :
                 print(f"{name_of_player_1} won the match")
                 break

             elif b[6] == b[4] == b[2] :
                 print(f"{name_of_player_1} won the match")
                 break

        elif player_1 == 8:
            if b[7] == "o":
                print("the place was taken by player2")
            else:
             b[7] = "x"
             tic_tac()
             if b[6:9] == ["x", "x", "x"]:
                 print(f"{name_of_player_1} won the match")
                 break
             elif b[1] == b[4] == b[7]:
                 print(f"{name_of_player_1} won the match")
                 break


        else:
            if b[8] == "o":
                print("the place was taken by player2")
            else:
             b[8] = "x"
             tic_tac()
             if b[6:9] == ["x", "x", "x"]:
                 print(f"{name_of_player_1} won the match")
                 break
             elif b[2] == b[5] == b[8] :
                 print(f"{name_of_player_1} won the match")
                 break
             elif b[0] == b[4] == b[8] :
                 print(f"{name_of_player_1} won the match")
                 break
        two = True
        while two == True:
          player_2 = int(input(" player 2's turn\nenter a value between 1-9\n"))
          if player_2 in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            if player_2 == 1:
              if b[0] == "x":
                  print("this place is taken")


              else :
                  b[0] = "o"
                  tic_tac()
                  if b[0:3] == ["o", "o", "o"]:
                      print(f"{name_of_player_2} won the match")
                      one = False
                  elif b[0] == b[3] == b[6]:
                      print(f"{name_of_player_2} won the match")
                      one = False
                  elif b[0] == b[4] == b[8]:
                      print(f"{name_of_player_2} won the match")
                      one = False
                  break

            elif player_2 == 2:
                if b[1] == "x":
                    print("the place is taken")
                else:
                 b[1] = "o"
                 tic_tac()
                 if b[0:3] == ["o", "o", "o"]:
                     print(f"{name_of_player_2} won the match")
                     one = False
                 elif b[1] == b[4] == b[7]:
                     print(f"{name_of_player_2} won the match")
                     one = False
                 break

            elif player_2 == 3:
                if b[2] == "x":
                    print("the place is taken")
                else:
                 b[2] = "o"
                 tic_tac()
                 if b[0:3] == ["o", "o", "o"]:
                     print(f"{name_of_player_2} won the match")
                     one = False
                 elif b[2] == b[5] == b[8] :
                     print(f"{name_of_player_2} won the match")
                     one = False
                 elif b[2] == b[4] == b[6] :
                     print(f"{name_of_player_2} won the match")
                     one = False
                 break

            elif player_2 == 4:
                if b[3] == "x":
                    print("the place is taken")
                else:
                 b[3] = "o"
                 tic_tac()
                 if b[3:6] == ["o", "o", "o"]:
                     print(f"{name_of_player_2} won the match")
                     one = False
                 elif b[0] == b[3] == b[6]:
                     print(f"{name_of_player_2} won the match")
                     one = False
                 break

            elif player_2 == 5:
                if b[4] == "x":
                    print("the place is taken")
                else:
                 b[4] = "o"
                 tic_tac()
                 if b[3:6] == ["o", "o", "o"]:
                     print(f"{name_of_player_2} won the match")
                     one = False
                 elif b[1] == b[4] == b[7]:
                     print(f"{name_of_player_2} won the match")
                     one = False
                 elif b[0] == b[4] == b[8]:
                     print(f"{name_of_player_2} won the match")
                     one = False
                 elif b[2] == b[4] == b[6]:
                     print(f"{name_of_player_2} won the match")
                     one = False
                 break

            elif player_2 == 6:
                if b[5] == "x":
                    print("the place is taken")
                else:
                 b[5] = "o"
                 tic_tac()
                 if b[3:6] == ["o", "o", "o"]:
                     print(f"{name_of_player_2} won the match")
                     one = False
                 elif b[2] == b[5] == b[8]:
                     print(f"{name_of_player_2} won the match")
                     one = False
                 break

            elif player_2 == 7:
                if b[6] == "x":
                    print("the place is taken")
                else:
                  b[6] = "o"
                  tic_tac()
                  if b[6:9] == ["o", "o", "o"]:
                      print(f"{name_of_player_2} won the match")
                      one = False
                  elif b[0] == b[3] == b[6]:
                      print(f"{name_of_player_2} won the match")
                      one = False
                  elif b[6] == b[4] == b[2] :
                      print(f"{name_of_player_2} won the match")
                      one = False
                  break

            elif player_2 == 8:
               if b[7] == "x":
                   print("the place is taken")
               else:
                   b[7] = "o"
                   tic_tac()
                   if b[6:9] == ["o", "o", "o"]:
                       print(f"{name_of_player_2} won the match")
                       one = False
                   elif b[1] == b[4] == b[7] :
                       print(f"{name_of_player_2} won the match")
                       one = False
                   break

            elif player_2 == 9:
                if b[8] == "x":
                    print("the place is taken")
                else:
                    b[8] = "o"
                    tic_tac()
                    if b[6:9] == ["o", "o", "o"]:
                        print(f"{name_of_player_2} won the match")
                        one = False
                    elif b[2] == b[5] == b[8] :
                        print(f"{name_of_player_2} won the match")
                        one = False
                    elif b[0] == b[4] == b[8]:
                        print(f"{name_of_player_2} won the match")
                        one = False
                    break

















