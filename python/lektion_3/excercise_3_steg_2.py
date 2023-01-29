#mini räknare

###############
# Steg 2: Lägga till input validering
###############

# adderingsfunktion

def addering(a):
    result = 0 
    for i in a: 
        result += i 
    return result


# input funktion

def användarens_input():
    first = (input("What is the first number? (integers only) "))
    second = (input("What is the second number? (integers only) "))
    return first, second

def wrong_input():
    first = (input("At least one of your entered values was not an integer, try again (ex. 1, 123 etc.) "))
    second = (input("At least one of your entered values was not an integer, try again (ex. 1, 123 etc.) "))
    return first, second

# input validering
# funktion ska ta in användarenns input 
            
def check_tuple_digit(t):
    for item in t:
        if not str(item).isdigit():
            return False
    return True

def validering(a):
    while a == False:
        input_retry_a = wrong_input()
        input_retry_b = check_tuple_digit(input_retry_a)
        if input_retry_b == True:
            break
        return input_retry_a # return the final validated input
def validated(a, b, c):
    """
    validated(check_tuple_digit, användarens_input, validation= validering)
    Ska ta in 
    """
    if a == True:
        return b
    elif a == False:
        return c(a) # call the function and return final validated input 
    
## turn input into two integers ## 

# #Main funktionen returnera och skrivas ut alla resultat från de andra 
# # funktioner 
def main_function():
    """
    
    """
    print("Miniräknare")
    validated_input = validated(check_tuple_digit(användarens_input()), användarens_input(), validering)
    # validated_input = validated(check_tuple_digit(användarens_input()), användarens_input(), validering)
    print( validated_input)
    resultat = addering(validated_input)
    return resultat 



##*****************************##
## KÖR PROGRAMMET ## 
##*****************************##


# usr_num_tuple=användarens_input()


# time_to_validate = check_tuple_digit(usr_num_tuple)

# validation = validering(time_to_validate)

# users_validated_value= validated(check_tuple_digit, användarens_input, validation)

# print(users_validated_value)
print(main_function())
#final_result = main_function(addering(validation))

# print(final_result)

