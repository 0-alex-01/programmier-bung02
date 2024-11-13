def war_of_numbers(numbers):
    
    even_numbers=[]
    odd_numbers=[]
    
    def is_even(number): #soll True False zurückgeben wenn zahl odd/ even
        if number %2== 0:
            even_numbers.append(number)
            return True
        else:
            odd_numbers.append(number)
            return False
    
    for number in numbers:
        is_even(number)
        
    sum_even = sum(even_numbers)
    sum_odd = sum(odd_numbers)
    
    
    if sum_even > sum_odd:
        margin = sum_even - sum_odd
        print(f"The sum of the even numbers: {sum_even} is larger\nthan the sum of the odd numbers: {sum_odd}.\nEven numbers win by margin of {margin}")
    elif sum_even == sum_odd:
        print(f"The sums are the same! Nobody won.")
    else:
        margin = sum_odd - sum_even
        print(f"The sum of the odd numbers: {sum_odd} is larger\nthan the sum of the even numbers: {sum_even}\nOdd numbers win by margin of {margin}")
    
    #pseudocode/to do list:
    #es gibt eine liste 
    # die funktion war of numbers soll nun alle geraden und alle ungeraden zahlen mit einander addieren
    #liste der zahlen für die lokale funktion extrahieren
    # dabei soll die lokale iseven funktion genutzt werden um herauszufinden, 
    # je nach dem gweinnt die summer der ungeraden oder geraden
    # zum schluss soll noch der numerische unterschied der beiden angeben werden


numbers = [2, 3, 4, 5, 6, 7, 8, 9]
numbers2 = [6, 4, 7, 3]
war_of_numbers(numbers)
war_of_numbers(numbers2)
