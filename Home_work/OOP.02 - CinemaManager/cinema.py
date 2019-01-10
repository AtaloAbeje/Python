class Cinema:
    def __init__(self):
        self.RoomArray = []
        self.MovieArray = []
        self.MaxMovie = 100
        self.MaxRoom = 6

    def add_room(self, room):
        if len(self.RoomArray) < self.MaxRoom:
            self.RoomArray.append(room)

    def add_movie(self, movie):
        if len(self.MovieArray) < self.MaxMovie:
            self.MovieArray.append(movie)

    def order_seats(self, amount, name):
        for i in range(0, len(self.RoomArray)):
            if self.RoomArray[i].movie.name == name:
                return self.RoomArray[i].order_seats(amount)
        return False

    def get_info(self):
        room_status = "\n"
        for i in range(0, self.RoomArray):
            room_status+=self.RoomArray[i].get_info()
            room_status += "\n__________________\n"
            
        return room_status