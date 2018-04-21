import json
import unittest

class Test(unittest.TestCase):
    def test_pos(self):
        self.assertEqual(run('input2.json'), True)
    def test_neg(self):
        self.assertEqual(run('input3.json'), False)
     
     
def isAttack(board, r, c):
    for i in range(r):
        if(board[i][c] == 1):
            return True;
        
    i = r - 1
    j = c - 1
    while(i >= 0 and j >= 0):
        if(board[i][j] == 1):
            return True;
        i -= 1
        j -= 1
    
    i = r - 1
    j = c + 1
    while(i >= 0 and j < 8):
        if(board[i][j] == 1):
            return True
        i -= 1
        j -= 1
       
def solve(board, row):
    i = 0
    while(i < 8):
        if(not isAttack(board, row, i)):
            board[row][i] = 1;
            if(row == 7):
                return True;
            else:
                if(solve(board, row + 1)):
                    return True;
                else:
                    board[row][i] = 0
        i += 1
    return False;
        
def run(filename):
    board = [[0 for i in range(8)] for i in range(8)]
    
    data = []
    with open(filename, "r") as f:
        data = json.load(f)
        
    if(data["start"] < 0 or data["start"] > 7):
        print "Invalid input"
        return False
    
    board[0][data["start"]] = 1
    if(solve(board, 1)):
        print "Board configuration: "
        for i in range(8):
            for j in range(8):
                print str(board[i][j]),
            print ""
        return True
    else:
        print "8 queens not solved"
        return False

run('input1.json')
print "Unit testing"
unittest.main()