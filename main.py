lets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
def resetboard():
  board = open('Data/posdat.txt', 'w')
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

def getpos():
  pos = open('Data/posdat.txt', 'r')
  counter = -1
  lines = pos.readlines()
  for j in lines:
    counter += 1
    lines[counter] = j.rstrip('\n')
  return lines

def completeboard():
  pos = getpos()
  board = updateboard(pos)
  printboard(board)

def updatepos(msg):
  global lets
  lines = getpos()
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
  location = lines.index(start[0] + str(totals))
  editedlines = lines
  editedlines[location] = start[0] + str(totale)
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
    if totale == numberrrrr:
      del editedlines[editedlines.index(c.rstrip('\n'))]
    

  counter = -1
  for b in editedlines:
    counter += 1
    if counter > 0:
      editedlines[counter - 1] += "\n"

  pos.close()

  pos = open('Data/posdat.txt', 'w')
  pos.writelines(editedlines)

def main():
  resetboard()
  while True:
    completeboard()
    print("\nFormat: Pg5-e5")
    updatepos(input())

main()