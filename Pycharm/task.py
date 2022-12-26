# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Использовать словарь, содержащий следующие ключи: название пункта назначения рейса;
номер рейса; тип самолета. Написать программу, выполняющую следующие действия: ввод
с клавиатуры данных в список, состоящий из словарей заданной структуры; записи должны
быть упорядочены по возрастанию номера рейса; вывод на экран номеров рейсов и типов
самолетов, вылетающих в пункт назначения, название которого совпало с названием,
введенным с клавиатуры; если таких рейсов нет, выдать на дисплей соответствующее
сообщение.
"""

if __name__ == '__main__':
    planes = list()
    while True:
        command = input('введите команду("help" - руководство по командам)\n>>>').lower()

        if command == 'exit':
            print("всего доброго")
            break

        elif command == 'help':
            print("add - добавление рейса\n"
                  "help - помощь по командам\n"
                  "select \"пункт назначения\" - вывод самолетов летящих в п.н.\n"
                  "exit - выход из программы")

        elif command == "add":
            plane = dict()
            plane["destination"] = input("Пункт назначения:\n")
            plane["flight_number"] = int(input("Номер рейса:\n"))
            plane["type_plane"] = input("Тип самолета\n")
            planes.append(plane)
            planes.sort(key=lambda key_plane: key_plane.get("flight_number"))
            print(planes)

        elif command == "select":
            lst = list(map(lambda x: x.get("destination"), planes))
            point = input('выберите нужное вам место\n')
            print("результаты поиска")
            if point in lst:
                print('рейсы в эту точку')
                for i in planes:
                    if point == i["destination"]:
                        print(f"{i['flight_number']}........{i['type_plane']}")
            else:
                print("рейсов не найдено")

        elif command == "plane_print":
            for i in planes:
                print(f"куда - {i['destination']} номер - {i['flight_number']} самолет - {i['type_plane']}")

        else:
            print('нет такой команды')
