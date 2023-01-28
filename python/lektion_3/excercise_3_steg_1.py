#mini räknare

###############
# Steg 1:
###############

# adderingsfunktion

def addering(a):
    result = 0 
    for i in a: 
        result += i 
    return result


# input funktion

def användarens_input():
    first = float(input("What is the first number? (up to two decimal places) "))
    second = float(input("What is the second number? (up to 2 decimal places) "))
    return first, second

# input validering



# #Main funktionen returnera och skrivas ut alla resultat från de andra 
# # funktioner 
def main_function(a):
    print("Miniräknare")
    print(a)
    return ""



##*****************************##
## KÖR PROGRAMMET ## 
##*****************************##
usr_num_tuple=användarens_input()

final_result = main_function(addering(usr_num_tuple))

print(final_result)

