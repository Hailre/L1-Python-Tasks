chocolate_bars = 18
people_count = 5

whole_bars = chocolate_bars // people_count #How many whole bars can be divided among the people.
extra_squares = whole_bars * 7 // people_count #Takes the total chocolate squares and divides it equally among the people.
squares_leftover = whole_bars * 7 % people_count #Takes the total chocolate squares and displays the remainder of dividing it by the amount of people.

print(f"Whole bars each: {whole_bars} \n Extra squares each: {extra_squares} \n Leftovers: {squares_leftover}")
