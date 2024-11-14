calls =0
def count_calls():  #2
    global calls
    calls += 1

def string_info(string):    #3
    string_1 = str(string)
    result = (len(string_1), string_1.upper(), string_1.lower())
    count_calls()
    return result

def is_contains(string, list_to_search):    # 4
    string = str(string).lower()
    list_to_search = list(list_to_search)
    count_calls()
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string:
            result = True
            break
        else:
            result = False
            continue
    return result

print(string_info('Kukaruka'))
print(string_info('Harley-Davidson'))
print(is_contains('BreAD', ['Car', 'WorLD', 'indian', 'bReAd'])) # Urban ~ urBAN
print(is_contains('apple', ['bike', 'bicycle', 'Carrot'])) # No matches
print(calls)

