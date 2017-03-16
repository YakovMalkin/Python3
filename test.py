Zero  = [" *** ",
         "*   *",
         "*   *",
         "*   *",
         "*   *",
         "*   *",
         " *** "]
One   = [" * ",
         "** ",
         " * ",
         " * ",
         " * ",
         " * ",
         "***"]
Two   = [" *** ",
         "*   *",
         "*  * ",
         "  *  ",
         " *   ",
         "*    ",
         "*****"]
Three = [" *** ",
         "*   *",
         "    *",
         "  ** ",
         "    *",
         "*   *",
         " *** "]
Four  = ["    * ",
         "   ** ",
         "  * * ",
         " *  * ",
         "******",
         "    * ",
         "    * "]
Five  = ["*****",
         "*    ",
         "*    ",
         " *** ",
         "    *",
         "*   *",
         " *** "]
Six   = [" *** ",
         "*   *",
         "*    ",
         "**** ",
         "*   *",
         "*   *",
         " *** "]
Seven = ["*****",
         "    *",
         "   * ",
         "  *  ",
         " *   ",
         "*    ",
         "*    "]
Eight = [" *** ",
         "*   *",
         "*   *",
         " *** ",
         "*   *",
         "*   *",
         " *** "]
Nine  = [" ****",
         "*   *",
         "*   *",
         " ****",
         "    *",
         "    *",
         " *** "]

Big_data = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

while True:
    line = input("Input number: ")
    if line:
        i = 0
        while i<len(line):
            try:
                number = int(line[i])
                j = 0
                element = Big_data[number]
                while j<7:
                    print(element[j])
                    j += 1
                i += 1
            except ValueError as err:
                print("Ошибка - ", err)
                break
        else:
            print("Thank you!")
            break
    else:
        break






# проверяем число ли + отработка исключений - типа
# Введи что-то другое и заново
# Если число - то берём первый символ и выводим на экран
# символ из кортежа с этим номером (может минус 1)
#
#
#
#
#