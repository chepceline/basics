# Data type

number = 25  #int
second = 56.78 #float
text = "Hello There" #string
ispythoninteresting = "True"  #bool

# store multiple values in a single variable

cars = ["toyota", "nissan", "vw"] #list -ordered and changeable
fruits = ("banana", "orange", "apple") #Tuple -unordered and unchangeable
countries = {"Kenya", "Tunisia", "Algeria"} # Set -unordered and unchangeable
details = {
    "firstname" : "Damaris",
    "age" : 25,
    "course" : "web development",
    "nationality" : "Kenyan"
}  # dictionary - Key-value pair

print(second)
print(text)
print(ispythoninteresting)
print(cars)
print(countries)
print(details ["age"])

# Typecasting - converting one data type to another

print(float(number))