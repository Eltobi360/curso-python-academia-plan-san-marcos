def decorator (funcition):
    def funtion_modifier():
        print("inicio de la modificacion")
        list_1=funcition()
        list_1.append(100)
        print(list_1)
        print("Fin de la modificacion")
    return funtion_modifier
def create_list():
    return [i for i in range(10)]

def create_tuple():
    return [i for i in range(100)]

result_1= decorator(create_list)
result_1()

result_2=decorator(create_tuple)
result_2()

@decorator
def set_name(): 
    return "Jorge"

set_name