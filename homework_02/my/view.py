import messages

def show_menu_items():

    for i in range(messages.menu_items):
        print(messages.menu_items[i])


user_menu_item = input(print(messages.user_choice_input))