import chess
import numpy as np
from lexwolf.weights import WEIGHTS
import lexwolf.structEl

class bitBoard:

    def __init__(self,board=None):
        self.COLOR_OFFSET = {chess.WHITE: 0, chess.BLACK: 1}
        self.BOOL_BIN = {True: 1, False: 0}
        self.__list = np.asarray([None]*(768+5)) # private 772-bits bit array: 64*6*2 + 5 ~ 64 cases for each piece of each color plus side to move & castling rights
        self.__pieceswght = np.asarray([None]*(768+5))
        self.setWeights()

        if(board==None): # no board provided, initial board is supposed
            temp = chess.Board()
            self.setList(temp)
        elif(board!=None):
            self.setList(board)

    def getList(self):
        return self.__list
    
    def getWeighted(self):
        return self.__list*self.__pieceswght

    def getEval(self):
        return np.sum(self.getWeighted())

    def setList(self,board):
            # Dictionary to map piece colors to their index for bitboard representation
            self.__list = np.asarray([0b0]*(768+5))
            for square in chess.SQUARES:
                piece = board.piece_at(square)
                if(piece!=None):
                    index = square + (piece.piece_type-1)*64 + self.COLOR_OFFSET[piece.color]*64*6
                    self.__list[index] = 0b1

            self.__list[-5] = self.BOOL_BIN[board.turn]
            self.__list[-4] = self.BOOL_BIN[board.has_kingside_castling_rights(chess.WHITE)]
            self.__list[-3] = self.BOOL_BIN[board.has_queenside_castling_rights(chess.WHITE)]
            self.__list[-2] = self.BOOL_BIN[board.has_kingside_castling_rights(chess.BLACK)]
            self.__list[-1] = self.BOOL_BIN[board.has_queenside_castling_rights(chess.BLACK)]

    def setWeights(self):        
        self.__pieceswght[0:64] = np.asarray([WEIGHTS['PAWN_VALUE']]*64)
        self.__pieceswght[64:128] = np.asarray([WEIGHTS['KNIGHT_VALUE']]*64)
        self.__pieceswght[128:192] = np.asarray([WEIGHTS['BISHOP_VALUE']]*64)
        self.__pieceswght[192:256] = np.asarray([WEIGHTS['ROOK_VALUE']]*64)
        self.__pieceswght[256:320] = np.asarray([WEIGHTS['QUEEN_VALUE']]*64)
        self.__pieceswght[320:384] = np.asarray([0]*64)
        self.__pieceswght[384:448] = np.asarray([-WEIGHTS['PAWN_VALUE']]*64)
        self.__pieceswght[448:512] = np.asarray([-WEIGHTS['KNIGHT_VALUE']]*64)
        self.__pieceswght[512:576] = np.asarray([-WEIGHTS['BISHOP_VALUE']]*64)
        self.__pieceswght[576:640] = np.asarray([-WEIGHTS['ROOK_VALUE']]*64)
        self.__pieceswght[640:704] = np.asarray([-WEIGHTS['QUEEN_VALUE']]*64)
        self.__pieceswght[704:773] = np.asarray([0]*69)

