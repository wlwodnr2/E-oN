def array_a(number, number_sum,horizon,vertical, control):
    if number == 0:
        for k in range(len(double_list)):
            print (double_list[k])
        return
    a = 0
    b = 0
    while True:
        number_sum = number_sum + 1
        vertical = vertical + control
        double_list[horizon][vertical] = number_sum
        a = a + 1
        if a == number:
            break

    if number != 1:   
        while True:
            number_sum = number_sum + 1 
            horizon = horizon + control
            double_list[horizon][vertical] = number_sum
            b = b + 1
            if (b == number-1):
                control = control * (-1)
                break

    number = number - 1
    array_a(number,number_sum,horizon,vertical, control)
            
horizon = 0
vertical = -1
num_sum = 0
control = 1
num = int(input("수 입력 : "))
double_list = [[0] * num for i in range(num)]
array_a(num,num_sum,horizon,vertical,control)
