from script import render_message, get_menu
import datetime

if __name__ == "__main__":
    import sys
    datetime_object = None
    if len(sys.argv) == 2:
        datetime_object = datetime.datetime.strptime(sys.argv[1], '%d/%m/%Y')
        
    menu = get_menu() # TODO: add the possibility to mock the http call, for those who are so eager to work on the weekend. The response is probably an empty json those days, because the service is not provided

    msg = render_message(menu)

    print(msg)
