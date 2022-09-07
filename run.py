from booking.booking import Booking
from filters.sort_filter import SortFilters

try:
    with Booking() as bot:
        bot.land_first_page()
        bot.change_currency(currency="TND")
        bot.select_place_to_go(place_to_go="New York")
        bot.select_date(check_in_date="2022-09-04", check_out_date="2022-09-11")
        bot.pick_filters(count=[3, 2, 2], children_age=[12, 14])
        bot.sumbit_search()
        bot.apply_filtration(SortFilters.LOW_PRICE, 2, 3, 4)
        #bot.report_result()
        print("Exiting...")
except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot form CLI \n'
            'Please add to PATH your selenium driver\n'
            'Windows: \n'
            '   set PATH=%PATH%;C:path-to-your-folder  \n\n'
            'Linux:  \n'
            '   PATH=$PATH:/path/to/your/folder \n')
    else:
        raise
