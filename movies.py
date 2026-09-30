# -------------------------------------------------------------
# Movie Ticket Booking App 
# TODO: need to add a proper database later instead of dicts, 
# but for now this works fine for testing.
# -------------------------------------------------------------

movies = {
    1:{
        "name": "Drishyam 3",
        "genre": "Crime / Thriller / Drama",
        "rating": 7.8,
        "price" : 200
     },
    2:{  
        "name": "Spider-Man: Brand New Day",
        "genre": "Action / Superhero / Sci-Fi",
        "rating": 8.0,
        "price": 250
     },
    3:{
        "name": "The Odyssey",
        "genre": "Action / Adventure / Epic",
        "rating": 8.5,
        "price": 300
     }
}

# keeping seats hardcoded, prob should make rows/cols dynamic later 
seats = [
    "A1", "A2", "A3", "A4", "A5",
    "B1", "B2", "B3", "B4", "B5",
    "C1", "C2", "C3", "C4", "C5"]

booked = {
    1: [],
    2: [],
    3: [] 
}

def present_movies():
        print("\n========== MOOOOOOVIES ==========") # Lol kept the extra o's from the debug phase
        # let's just loop through dict keys the old school way
        for number in movies:
                print(number, ".", movies[number]["name"])
                print("Genre :", movies[number]["genre"])
                print("Rating:", movies[number]["rating"], "/10")
                print("Price :", movies[number]["price"])
                print() # empty line spacing

def display_seats(movie_number):
        print("\n========== SEATS ==========" ) 
        
        # quick check to see if movie exists even though we usually validate before calling
        if movie_number not in movies:
            print("Wait, what movie is this?")
            return

        for seat in seats:
                if seat in booked[movie_number]:
                        print("[X]", end=" ")
                else:
                        print("[" + seat + "]", end=" ")
                
                # messy newline logic just like I wrote it at 2 AM
                if seat == "A5" or seat == "B5":
                        print()
                        
        print("\nX = Booked") 

def book_ticket():
       present_movies()
       try:
                movie_number = int(input("Enter movie number: "))
                if movie_number not in movies:
                        print("Invalid movie number. Try again.")
                        return
                
                display_seats(movie_number)
                seat = input("Enter seat number: ").upper()
                
                if seat not in seats:
                        print("Bro, that seat doesn't even exist.")
                        return
                        
                if seat in booked[movie_number]:
                        print("Ah, seat is already booked man!")
                        return
                        
                booked[movie_number].append(seat)
                
                # grab the price 
                price = movies[movie_number]["price"]
                
                print("\n========== BOOKING CONFIRMED ==========")
                print("Movie :", movies[movie_number]["name"])
                print("Seat  :", seat)
                print("Amount: ₹", price)
                print("Enjoy the show!! 🍿")
                
       except ValueError:
                print("Please enter a valid number, come on.")

def cancel_ticket():
       present_movies()
       try: 
                movie_number = int(input("Enter movie number: ")) 
                if movie_number not in movies:
                      print("Invalid movie number.")
                      return
                      
                display_seats(movie_number) 
                seat = input("Enter seat number to cancel: ").upper()
                
                # checking if it's actually booked before removing
                if seat in booked[movie_number]:
                      booked[movie_number].remove(seat)
                      print("Booking cancelled successfully.") 
                else:
                      print("Hmm... This seat is not even booked yet.")    
       except ValueError:
                print("Please enter a valid number.")

def main():
    # Main app loop
    while True:
            print("\n-------------------------------")
            print("   MOVIE TICKET BOOKING SYSTEM")
            print("---------------------------------")
            print("1. Display Movies")
            print("2. Display Seats")
            print("3. Book Ticket")
            print("4. Cancel Ticket")
            print("5. Exit")

            choice = input("Enter your choice: ")  
            
            if choice == "1":
                        present_movies() 
            elif choice == "2":
                        # copying code here instead of calling a helper function cleanly, oops
                        present_movies()
                        try:
                                 movie_number = int(input("Enter movie number: "))
                                 if movie_number in movies:
                                     display_seats(movie_number)
                                 else:
                                     print("Invalid movie number.")
                        except ValueError:
                                 print("Please enter a number.")

            elif choice == "3":
                        book_ticket()
            elif choice == "4":
                        cancel_ticket()
            elif choice == "5":
                        print("Thank you Fam! Catch you later.")
                        break
            else:
                        print("Invalid choice, pick between 1-5.")

if __name__ == "__main__":
    main()