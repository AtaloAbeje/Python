import room
import movie
import cinema

myCinme = cinema.Cinema()

movie1 = movie.Movie("Avatar", 100)
movie2 = movie.Movie("Toy Story", 110)
movie3 = movie.Movie("Black Panther", 130)
movie4 = movie.Movie("The Amazing Spider-Man", 140)


room1 = room.Room(movie1)
room2 = room.Room(movie2)
room3 = room.Room(movie3)
room4 = room.Room(movie4)

myCinme.add_movie(room1)
myCinme.add_movie(room2)
myCinme.add_movie(room3)
myCinme.add_movie(room4)

myCinme.order_seats(2, "Avatar")
myCinme.order_seats(3, "Toy Story")
myCinme.order_seats(4, "Black Panther")
myCinme.order_seats(5, "The Amazing Spider-Man")

print(myCinme.get_info())