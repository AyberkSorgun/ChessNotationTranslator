

possible_startings = {'K':'King','Q':'Queen','B':'Bishop','N':'Knight','R':'Rook','O':'Castle',
                      'a':'a','b':'b','c':'c','d':'d','e':'e','f':'f','g':'g','h':'h',
                      '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8'}


def interp(str):
    result = ""


    return interpret(str,result)

def interpret(str,result):

   if len(str) == 2:

       if str[0] not in ("a","b","c","d","e","f","g","h") or str[1] not in ("1","2","3","4","5","6","7","8"):
           result = "Invalid move"

           return result
       else:
           return str
   if len(str) == 3:

        if str =="O-O":
            return "castles kingside"
        if str[0] in possible_startings.keys():

            result += possible_startings[str[0]]+" to " + interp(str[1:3])

            return result



        else:
            result = "Invalid move"

            return result

   if len(str) == 4:

       if str[0] not in ("a","b","c","d","e","f","g","h"):

           result= "Invalid move"

           return result

       else:


           if str[3] == "#" :
               result += interp(str[0:3]) + " checkmate"

               return result

           if str[3] == "+" :
               result += interp(str[0:3]) + " check"

           if str[2] == "=" and str[1] == "8":

               result="pawn is pushed and promoted to a " + possible_startings[str[3]]

               return result

           if str[1] == "x":

               return possible_startings[str[0]] + " takes on " + interp(str[2:4])

           if str[1] !="x" and str[3] !="+" and str[3] !="#" and str[2] != "=":

               return possible_startings[str[0]] + " from " +possible_startings[str[1]] + " to " + interp(str[2:4])

           else:
               result = "Invalid move"

               return result

   if len(str) == 5:

       if str[4] == "+":
           checkOrMate= " check"
       if str[4] == "#":
           checkOrMate= " checkmate"
       if str == "O-O-O":
           return "castles queenside"

       if str[1] == "x":

           return possible_startings[str[0]] + " takes on " + interp(str[2:4]) + checkOrMate

       else:

           result = "Invalid move"

           return result




while True:
    input= raw_input("Please write a chess notation: ")

    print(interp(input))




