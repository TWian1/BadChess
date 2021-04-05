lets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
names = ["p", "n", "k", "q", "c", "r"]
import os

def checkinput(msg, pos, tns, movecount, movediff):
  global lets
  global names

  location = pos.index(msg[0] + str(msg[1]))

  valpiece = False
  

  moveset = [[8, 9, 7, 16], [15, 17, 10, 6, -15, -17, -10, -6], [1, 8, 9, 7, -1, -8, -9, -7], [7, 9, 8, 1, -7, -9, -8, -1]]

  requirepiece = [[-1, 1, 1, -1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]

  firstmove = [[False, False, False, True], [False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False]]

  onemove = True
  color = 1
  if msg[0] == "P": color = -1

  place = names.index(msg[0].lower())
  if place > 2: onemove = False

  if onemove:
    return smallmoveset(moveset, requirepiece, firstmove, movediff, color, msg, movecount, location, place) 
  else:
    return longmoveset(moveset, firstmove, movediff,movecount, place)

def smallmoveset(moveset, requirepiece, firstmove, movediff, color, msg, movecount, location, place):
  if movediff*color in moveset[place]:
    movindex = moveset[place].index(movediff*color)
    if requirepiece[place][movindex] == 1:
      if firstmove[place][movindex] == True:# valid requires piece and can only move on first turn


        Detected = False
        for a in getposnumbers():
          if int(a) == msg[2]: Detected = True
        if Detected == True:
          if movecount[location] == "0": return True


      else:# valid requires piece

        Detected = False
        for a in getposnumbers():
          if int(a) == msg[2]: Detected = True
        if Detected == True: return True


    elif requirepiece[place][movindex] == 0:
      if firstmove[place][movindex] == True: # valid can move whenever as long as first move

        if movecount[location] == "0": return True 


      else:# can move wherever whenever

        return True 


    elif requirepiece[place][movindex] == -1:
      if firstmove[place][movindex] == True:# valid requires there to be no piece and it to be the first move

        Detected = False
        for a in getposnumbers():
          if int(a) == msg[2]: Detected = True
        if Detected == False:
          if movecount[location] == "0": return True 


      else:# valid requires there to be no piece


        Detected = False
        for a in getposnumbers():
          if int(a) == msg[2]: Detected = True
        if Detected == False: return True 
    
def longmoveset(moveset, firstmove, movediff, movecount, place):
  pass
  
  

def resetboard():
  board = open('Data/posdat.txt', 'w')
  moves = open('Data/Movecount.txt', 'w')
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
      if a2 == "\n": continue
      boa[counter].append(a2)
  boardtemp.close()
  for a in pos:
    last = ""
    for b in a:
      if a.index(b) > 0: last += b
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
      if counter > 1: newline += b
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
    elif beforedash == True: start += a
    else: end += a
  addnums = lets.index(start[1])
  addnume = lets.index(end[0])
  totals = int(start[2]) + (addnums * 8) - 1
  totale = int(end[1]) + (addnume * 8) - 1
  return [start[0], totals, totale]
def updatepos(msg):
  lines = get('Data/posdat.txt')
  moves = get('Data/Movecount.txt')

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
      if counter > 0: numberrrrr += d
    numberrrrr = int(numberrrrr)
    if start[2] == numberrrrr: del editedlines[editedlines.index(c.rstrip('\n'))]
    

  counter = -1
  for b in editedlines:
    counter += 1
    if counter > 0: editedlines[counter - 1] += "\n"
  counter = -1
  for b in editedmoves:
    counter += 1
    if counter > 0: editedmoves[counter - 1] += "\n"

  pos.close()

  pos = open('Data/posdat.txt', 'w')
  mov = open('Data/Movecount.txt', 'w')
  mov.writelines(editedmoves)
  pos.writelines(editedlines)

def formated(mes):
  global names
  global lets
  if not(len(mes) == 6): return False
  if not(mes[3] == "-"): return False
  if not(mes[0].lower() in names): return False
  if not(mes[1] in lets and mes[4] in lets): return False
  mesclean = getinpstuff(mes)
  if not(mesclean[1] in getposnumbers()): return False
  if mesclean[1] > 63 or mesclean[2] > 63: return False
  return True

def main():
  resetboard()
  turns = 0
  while True:
    turns += 1
    moves = get('Data/Movecount.txt')
    posdata = get('Data/posdat.txt')
    completeboard()
    print("\nFormat: Pg5-e5")
    answer = input()
    if formated(answer):
      inputclean = getinpstuff(answer)
      if checkinput(inputclean, posdata, turns, moves, inputclean[2] - inputclean[1]):  updatepos(answer)
      os.system('clear')


main()
