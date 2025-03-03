# Week 8 Homework

def make_sandwich(*ingredients):
    print('\nMaking your sandwich now with the following ingredients:')
    for ingredient in ingredients:
        print(f'* {ingredient}')

# Calling the function two times
make_sandwich('Ham', 'Cheese', 'Olives', 'Spicy Mustard','Wheat Toast')
make_sandwich('Turkey', 'Avacado', 'Hot sauce','White Bread')