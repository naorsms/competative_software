number_of_tests = int(input())
for tests_index in range(number_of_tests):
    tests_information = input()
    number_of_floors = int(tests_information.split(" ")[0])
    number_of_rooms = int(tests_information.split(" ")[1])
    switches_flip = int(tests_information.split(" ")[2])
    wrong_wired_list = []
    for floors_index in range(number_of_floors):
        wrong_wired_list.append(int(input()))
    wrong_wired_list.sort()
    for switches_index in range(switches_flip):
        wrong_wired_list[switches_index] = number_of_rooms - wrong_wired_list[switches_index]
    Sum = sum(wrong_wired_list)
    print(Sum)

