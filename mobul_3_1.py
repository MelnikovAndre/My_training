calls=0
def count_calls():
    global calls
    calls+=1
def string_info(string):
    print((len(string), string.upper(), string.lower()))
    count_calls()

def is_contains(string,list_to_search):
    for i in list_to_search:
        if string in list_to_search:
            i = True
        else:
            i = False
    print(i)
    count_calls()
string_info('Batman')
string_info('Zorro')
string_info('Hulk')
is_contains('Batman', ['Armageddon','Batman', 'Superman','Hulk'])
is_contains('Zorro', ['Armageddon','Batman', 'Superman', "Hulk"])
is_contains('Hulk', ['Armageddon','Batman', 'Superman', "Hulk"])

print(calls)