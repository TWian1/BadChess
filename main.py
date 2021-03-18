lets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
import os

def checkinput(msg, pos, tns, mov, test):

  location = pos.index(msg[0] + str(msg[1]))

  moves = [[8, 9, 7, 16]]
  reqpiece = [[-1, 1, 1, -1]]
  firstmove = [[False, False, False, True]]

  if msg[0].lower() == "p":

    multiplier = 1
    if msg[0] == "P":
      multiplier = -1
    
    return smallmoveset(moves, reqpiece, firstmove, test, multiplier, msg, mov, location)    

def smallmoveset(moves, reqpiece, firstmove, test, multiplier, msg, movecount, location):
  counter = -1
  for a in moves:
    counter += 1
    if a*multiplier == test:
      if firstmove[counter] == False:
        if reqpiece[counter] == 1:
          if msg[2] in getposnumbers():
            return True
        elif reqpiece[counter] == 0:
          return True
        elif reqpiece[counter] == -1:
          if not(msg[2] in getposnumbers()):
            return True
      else:
        if movecount[location] == '0':
          if reqpiece[counter] == 1:
            if msg[2] in getposnumbers():
              return True
          elif reqpiece[counter] == 0:
            return True
          elif reqpiece[counter] == -1:
            if not(msg[2] in getposnumbers()):
              return True
      

def resetboard():
  board = open('Data/posdat.txt', 'w')
  moves = open('Data/Movedat.txt', 'w')
  movetxt = []
  for a in range(32):
    movetxt.append('0\n')
  movetxt[31] = movetxt[31].rstrip('\n')
  moves.writelines(movetxt)
  board.writelines(["c0\n", "n1\n", "r2\n", "q3\n", "k4\n", "r5\n", "n6\n", "c7\n", "p8\n", "p9\n", "p10\n", "p11\n", "p12\n", "p13\n", "p14\n", "p15\n", "P48\n", "P49\n", "P50\n", "P51\n", "P52\n", "P53\n", "P54\n", "P55\n", "C56\n", "N57\n", "R58\n", "Q59\n", "K60\n", "R61\n", "N62\n", "C63"])
def printboard(board): #function to print the board better
  global lets
  line1 = "      "
  for c in range(8):
    line1 += str(c+1)
    line1 += "   "
  print(line1 + "\n\n")
  counter = -1
  for a in board:
    counter += 1
    line2 = lets[counter] + "     "
    for b in a:
      line2 += b
      line2 += "   "
    print(line2 + "\n")

def updateboard(pos): #takes the data and converts it for visuals
  boardtemp = open('Data/board.txt', 'r')
  boa = []
  counter = -1
  for a1 in boardtemp.readlines():
    counter += 1
    boa.append([])
    for a2 in a1:
      if a2 == "\n":
        continue
      boa[counter].append(a2)
  boardtemp.close()
  for a in pos:
    last = ""
    for b in a:
      if a.index(b) > 0:
        last += b
    last = int(last)
    yscale = 0
    xscale = 0
    while True:
      if last > 7:
        yscale += 1
        last -= 8
      else:
        xscale = last
        break
    boa[yscale][xscale] = a[0]

  return boa   

def get(txt):
  pos = open(txt, 'r')
  counter = -1
  lines = pos.readlines()
  for j in lines:
    counter += 1
    lines[counter] = j.rstrip('\n')
  return lines

def getposnumbers():
  lines = get('Data/posdat.txt')
  newlines = []
  for a in lines:
    newline = ""
    counter = 0
    for b in a:
      counter += 1
      if counter > 1:
        newline += b
    newlines.append(int(newline))
  return newlines


def completeboard():
  pos = get('Data/posdat.txt')
  board = updateboard(pos)
  printboard(board)
def getinpstuff(msg):
  global lets
  start = ""
  end = ""
  beforedash = True
  for a in msg:
    if a == "-":
      beforedash = False
      continue
    elif beforedash == True:
      start += a
    else:
      end += a
  addnums = lets.index(start[1])
  addnume = lets.index(end[0])
  totals = int(start[2]) + (addnums * 8) - 1
  totale = int(end[1]) + (addnume * 8) - 1
  return [start[0], totals, totale]
def updatepos(msg):
  lines = get('Data/posdat.txt')
  moves = get('Data/Movedat.txt')

  start = getinpstuff(msg)

  location = lines.index(start[0] + str(start[1]))
  editedlines = lines
  editedmoves = moves
  editedlines[location] = start[0] + str(start[2])
  editedmoves[location] = str(int(editedmoves[location]) + 1)


  counter = -1
  pos = open('Data/posdat.txt', 'r')


  
  lines = pos.readlines()
  for c in lines:
    counter = -1
    numberrrrr = ""
    for d in c:
      counter += 1
      if counter > 0:
        numberrrrr += d
    numberrrrr = int(numberrrrr)
    if start[2] == numberrrrr:
      del editedlines[editedlines.index(c.rstrip('\n'))]
    

  counter = -1
  for b in editedlines:
    counter += 1
    if counter > 0:
      editedlines[counter - 1] += "\n"
  counter = -1
  for b in editedmoves:
    counter += 1
    if counter > 0:
      editedmoves[counter - 1] += "\n"

  pos.close()

  pos = open('Data/posdat.txt', 'w')
  mov = open('Data/Movedat.txt', 'w')
  mov.writelines(editedmoves)
  pos.writelines(editedlines)

def main():
  resetboard()
  turns = 0
  while True:
    turns += 1
    moves = get('Data/Movedat.txt')
    posdata = get('Data/posdat.txt')
    completeboard()
    print("\nFormat: Pg5-e5")
    answer = input()
    inputclean = getinpstuff(answer)
    check = checkinput(inputclean, posdata, turns, moves, inputclean[2] - inputclean[1])
    if check == True:
      updatepos(answer)
    os.system('clear')


main()