calls = 0
def count_calls():
    global calls
    calls += 2
    return calls

def string_info(string):
   return (len(string), string.upper(), string.lower())

print(string_info('Copybara'))
print(string_info('Armageddon'))

count_calls()

def is_contains(string, list_to_searc):
    list_to_searc = []
    if string in list_to_searc:
        return True
    else:
        return False

print(is_contains('Urban', ['ban','BaNaN','urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))

count_calls()
print(calls)