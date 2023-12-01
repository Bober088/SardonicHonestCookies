user_input = float(input("Введите свою температуру тела:"))
if user_input > 36.7:
 print("Тебе стоит обратиться к врачу!")
elif user_input < 36:
 print("ты наверно устал раз температура понижена. Отдохни!")
else:
 print("Ты здоров!")
