'''
#1. Add two numbers
        # Prompting the user to enter the first number
first_number = int(input("Enter the first number: "))

        # Prompting the user to enter the second number
second_number = int(input("Enter the second number: "))

        # Calculate the sum of the two numbers
total_sum = first_number + second_number

print(f"The sum of the {first_number} and {second_number} is {total_sum}")


#2. Agreement Boot
        # Prompting the user to ask their favorite animal
favorite_animal :str = input("What's your favorite animal?")
        # Respoding the user by telling our favorite animal also
print(f"My favorite animal is also {favorite_animal}!")



#3. Fahrenheit to Celsius
        # Prompting user to enter temperature in fahrenheit degree
degree_fahrenheit = float(input("Enter the temperature in fahrenheit degree: "))

        # Calculating temperature in degree celcius
degree_celcius = (degree_fahrenheit - 32) * 5.0/9.0

print(f"Temperature : {degree_fahrenheit}F = {degree_celcius}C")




#4. Triangle Perimeters

        # Prompting User to enter lengths of triangle
first_length = float(input("What is the length of side 1? "))
second_length = float(input("What is the length of side 2? "))
third_length = float(input("What is the length of side 3? "))

        # Calculating the perimeter of triangle

perimeter = first_length + second_length +third_length

print(f"The perimeter of the triangle is {perimeter}.")



#5. Square Number
        # Prompting the user for a number
number = float(input("Type a number to see its square: "))
        # Calculating the square of the number
result = number * number

print(f"{number} squared is {result}")



#6. Delete a number

numbers : list[int] = [1, 2, 3, 4, 5]
print(numbers)        
        #Removing the number '3' from the list
numbers.remove(3)

print(numbers)



#7. Creating a list 

list_1 = [1,2,3]
list_2 = [4,5,6]
        #Using extend() method
list_1.extend(list_2)

print(list_1)



#8. Pop method

items = [10, 20, 30, 40]
print(items)
        #Using pop() method
items.pop()
print(items)
print("By using pop() method the last value in the list will be removed")


#9. Index Method

colors = ['red', 'blue', 'green', 'yellow']
        #Using index() method
green_index = colors.index("green")

print(f"The index of the green color will be: {green_index}.")




#10. Get last element

def get_last_element(lst):

    last_element = lst[-1] 

    print(last_element)

list = [1, 2, 3, 4, 5]
get_last_element(list)  



'''
#11. Get a List

def get_input_list():
    result = []
    while True:
        value = input("Enter a value: ")
        if value == "":
            break
        result.append(value)
    print("Here's the list:", result)

get_input_list()