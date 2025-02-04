import messages

def show_menu_items():

    for i in range(len(messages.menu_items)):
        print(messages.menu_items[i])

def print_message(data: str):
    print(data)