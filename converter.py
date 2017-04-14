def binary_to_decimal(number_to_convert):
    number_list = list(number_to_convert)
    number_lengh = len(number_list)
    power = number_lengh - 1
    decimal_value = 0
    for i in range(number_lengh):
        decimal_value += int(number_list[i]) * (2 ** (power))
        power -= 1
    return(decimal_value)

def decimal_to_binary(number_to_convert):
    binary_list=[]
    number_to_convert = int(number_to_convert)
    while number_to_convert > 0:
        modulo = int(float(number_to_convert % 2))
        binary_list.append(modulo)
        number_to_convert = (number_to_convert - modulo) / 2
    binary_list.append(0)
    binary_value = ""
    for i in binary_list[::-1]:
        binary_value  = binary_value + str(i)
    return(binary_value)


def main():
    correct_input = True
    wrong_numbers = ['2','3','4','5','6','7','8','9']
    while correct_input:
        try:
            number_to_convert, number_system = map(str, input().split(' '))
        except ValueError:
            print("something went wrong ! input 2 numbers seperate by space")
        else:
            correct_input = False
            wrong_number = False

        for i in range(len(number_to_convert)):
            if number_to_convert[i] in wrong_numbers:
                wrong_number = True


        if number_system == "2" and number_to_convert.isdigit() and wrong_number == False:
            print (binary_to_decimal(number_to_convert), " 10")
        elif number_system == "10" and number_to_convert.isdigit():
            print (decimal_to_binary(number_to_convert), " 2")
        else:
            correct_input = True
            print("invalid sign !")

main()
