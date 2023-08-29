#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    store = []
    counter = 0
    for i in range(list_length):
        try:
            x = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            counter = 1
        except TypeError:
            print("wrong type")
            counter = 1
        except IndexError:
            print("out of range")
            counter = 1
        finally:
            if counter:
                counter = 0
                store.append(0)
            else:
                store.append(x)
    return store
