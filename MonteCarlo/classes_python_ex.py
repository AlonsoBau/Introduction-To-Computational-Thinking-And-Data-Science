### Part 1: __init__ method & class attributes
class HelloWorld():
    def __init__(self) -> None:
        print('Hello World')
        self.feeling = 'Excited'
    def __str__(self) -> str:
        return 'This is me'

start = HelloWorld()
print(start.feeling)
print(start)
print('\n')
# # Part 2: super() and Inheritance
# class HelloAndBye(HelloWorld):
#     def __init__(self) -> None:
#         super().__init__()
#         print('Bye World')


# end = HelloAndBye()
# print(end.feeling)
# print(end)
###############

### Part 3: Inheritance is a little bit of a headache
## I am Happy Today but I should Rest
# class Happy():
#     def __init__(self):
#         print('Happy')

# class Event(Happy):
#     def __init__(self):
#         print('I am')
#         super().__init__()
#         print('Today')

# class Rest():
#     def __init__(self):
#         print('but I should')
#         print('Rest')      

# class Combination(Event, Rest) :
#     def __init__(self):
#         super().__init__()

# comb = Combination()
# print(Combination.__mro__)
# What do you think this will output

## Fix
# class Happy():
#     def __init__(self):
#         print('Happy')

# class Event(Happy):
#     def __init__(self):
#         print('I am')
#         super().__init__()
#         print('Today')

# class Rest(Event):
#     def __init__(self):
#         super().__init__()
#         print('but I should')
#         print('Rest')      

# class Combination(Rest, Event) :
#     def __init__(self):
#         super().__init__()
        

# comb = Combination()
# print(Combination.__mro__)

# What do you think this will output