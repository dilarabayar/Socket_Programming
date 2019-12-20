import datetime
import  check_available_room


def main():
    print("WELCOME TO Travel Agency\n")

    departuredate = input('\nEnter departure date in YYYY/MM/DD format : ')
    arrivaldate = input('\nEnter arrival date in YYYY/MM/DD format : ')
    hotel_name = input('\nEnter the hotel name : ')
    airline = input('\nEnter the airline name : ')
    num_of_travellers = input('\nEnter the number of travellers : ')
    input_string = departuredate +"-"+arrivaldate+"-" + hotel_name +"-"+ airline+"-" +num_of_travellers


    #check_available_room.check_available_room(departure_date, arrival_date, hotel_name,num_of_travellers)


    return input_string
