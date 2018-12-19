shopping_list = []

def show_help():
    print('What should you pick up at the store?')
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help
Enter 'SHOW LIST' to see your list
    """)


def add_to_list(item):
    shopping_list.append(item)
    print('Added! List have {} items.'.format(len(shopping_list)))

def show_list():
    print('Here is your list:')
    for x in shopping_list:
        print('* {}'.format(x))

show_help()
while True:
    new_item = input('> ')

    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW LIST':
        show_list()
        continue

    add_to_list(new_item)

show_list()
