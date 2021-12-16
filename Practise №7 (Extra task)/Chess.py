import numpy

#def knight_route(X,Y):
 #   if 

M = 10
N = 10
X = 1
Y = 1

chess_board = numpy.zeros((M, N))
chess_board[X-1][Y-1] = 1
print(int(chess_board[X-1,Y-1]))
# print(chess_board)
