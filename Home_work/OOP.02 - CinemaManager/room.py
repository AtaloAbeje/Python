class Room:
    def __init__(self, movie):
        self.MatrixSeat = [[False for i in range(8)] for j in range(10)] # 
        self.movie = movie

    def OrderSeat(self, amount):
        for i in range(0, len(self.MatrixSeat)):
            for j in range(0, len(self.MatrixSeat[i])):
                if not self.MatrixSeat[i][j]:
                    self.MatrixSeat[i][j] = True
                    amount -= 1
                    if samount == 0:
                        return  True
        return False

    def get_info(self): # return only string
        SeatStatus = "\n"
        for i in range(0, len(self.MatrixSeat)):
            for j in range(0, len(self.MatrixSeat[i])):
                if self.MatrixSeat[i][j]:
                    SeatStatus += " V |"
                else:
                    SeatStatus += " X |"
            SeatStatus += "\n---------------------------------\n"
        
        return self.movie.get_info() + SeatStatus
