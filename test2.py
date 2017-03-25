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
    try:
        line = input("Input number: ")
        if line:
            row = 0
            while row < 7:
                col = 0
                tmp_line = ""
                while col < len(line):
                        digits = int(line[col])
                        element = Big_data[digits]

                        tmp_line += element[row].replace('*', line[col])

                        col += 1
                print(tmp_line)
                row += 1;
            else:
                break
        else:
            break
    except ValueError as err:
        print("Ошибка - ", err)
        break
