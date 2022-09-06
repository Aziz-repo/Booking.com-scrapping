from booking.booking import Booking
from enums.sort_filter import sortFilters

with Booking() as bot:
    bot.land_first_page()
    bot.change_currency(currency='TND')
    bot.select_place_to_go(place_to_go="New York")
    bot.select_date(check_in_date="2022-09-04", check_out_date="2022-09-11")
    bot.pick_filters(count=[3, 2, 2], children_age=[12, 14])
    bot.sumbit_search()
    bot.apply_filtration(sortFilters.LOW_PRICE, 2, 3, 4)
    print("Exiting...")