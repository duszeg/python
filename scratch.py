##proste sumowanie liczb podanych przez użytkownika

user_input = input("Wprowadź liczby oddzielone znakiem '+': ")
my_list = user_input.split("+")
my_list = [int(x) for x in my_list]
print("Suma wynosi:")
print(sum(my_list))
input("Press Enter to continue. . .")
