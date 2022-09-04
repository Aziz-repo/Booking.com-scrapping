from booking.booking import Booking


with Booking() as bot:
    bot.land_first_page()
    bot.change_currency(currency='TND')
    bot.select_place_to_go(place_to_go="New York")
    bot.select_date(check_in_date="2022-09-04", check_out_date="2022-09-11")
    bot.pick_filters(adult=True, children=False, rooms=True, count=[3, 2, 2])
    bot.sumbit_search()
    print("Exiting...")