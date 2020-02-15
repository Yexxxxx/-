import re
var = {}
C_number = {"零":0,"一":1,"二":2,"三":3,"四":4,"五":5,"六":6,"七":7,"八":8,"九":9}
C_unit  = ["","十","百","千","万"]
def define(name,value):
    global var
    var[name] = value

def println(name):
    global var
    try:
        print(var[name])
    except:
        result = re.findall(r'“(.*?)”',name)
        print(result[0])

def add(name,num):
    global var
    try:
        rubbish = var[name]
    except:
        print("查无此变量")
    else:
        result = number([var[name]][0]) + number(num)
        var[name] = chinese(result)

def subtract(name,num):
    global var
    try:
        rubbish = var[name]
    except:
        print("查无此变量")
    else:
        result = number([var[name]][0]) - number(num)
        var[name] =  chinese(result)

def multiplication(name,num):
    global var
    try:
        rubbish = var[name]
    except:
        print("查无此变量")
    else:
        result = number([var[name]][0]) * number(num)
        var[name] = chinese(result)

def division(name,num):
    global var
    try:
        rubbish = var[name]
    except:
        print("查无此变量")
    else:
        if num == 0:
            print("除数不符合规则")
        else:
            result = number([var[name]][0]) / number(num)
            var[name] = chinese(result)

def ifelse(str_get_input):
    global var, C_number
    get_input = str_get_input.split()
    num = number([get_input[3]][0])
    var_value = number(var[get_input[1]])
    idx_result_1, idx_result_2 = str_get_input.find("则"), str_get_input.find("否则")
    if get_input[2] == "大于":
        if var_value > num:
            main(str_get_input[idx_result_1 + 2:idx_result_2])
        else:
            main(str_get_input[idx_result_2 + 3:])
    elif get_input[2] == "小于":
        if var_value < num:
            main(str_get_input[idx_result_1 + 2:idx_result_2])
        else:
            main(str_get_input[idx_result_2 + 3:])
    elif get_input[2] == "等于":
        if var_value == num:
            main(str_get_input[idx_result_1 + 2:idx_result_2])
        else:
            main(str_get_input[idx_result_2 + 3:])
    else:
        print("输入不符合规则")

def chinese_decimal(str_num):
    global C_number
    result = ""
    for z in range(len(str_num)):
        for x in C_number:
            if int(str_num[z]) == C_number[x]:
                result = result + x
    return result

def chinese(num):
    global C_number, C_unit
    str_num = str(num)
    if "." in str_num:
        point = str_num.find(".")
        if point != str_num.rfind("."):
            print("输入不合法")
        else:
            result_1 = chinese(str_num[:point]) + "点"
            result_2 = chinese_decimal(str_num[point + 1:])
            result = result_1 + result_2
            return result
    else:
        num = int(num)
        if num < 0:
            num = str(num)
            num = chinese(num[1:])
            result = "负" + num
            return result
        elif num <= 10:
            for x in C_number:
                if num == C_number[x]:
                    return x
        else:
            num = str(num)
            n = len(num) - 1
            result = ""
            for x in range(len(num)):
                if chinese(int(num[x])) == "零":
                    if x == len(num):
                        result = result
                    else:
                        result = result + chinese(int(num[x]))
                else:
                    result = result + chinese(int(num[x])) + C_unit[n]
                n = n - 1
            return result

def number(cnum):
    global C_number
    num = 0
    decimal = "0."
    if cnum:
        idx_q, idx_b, idx_s, idx_x = cnum.find('千'), cnum.find('百'), cnum.find('十'), cnum.find('点')
        if idx_x != -1:
            result = number(cnum[:idx_x])
            point = cnum[idx_x + 1:]
            for x in range(len(point)):
                decimal = decimal + str(C_number[point[x]])
            result = result + float(decimal)
            return result
        else:
            if idx_q != -1:
                num += C_number[cnum[idx_q - 1:idx_q]] * 1000
            if idx_b != -1:
                num += C_number[cnum[idx_b - 1:idx_b]] * 100
            if idx_s != -1:
                num += C_number.get(cnum[idx_s - 1:idx_s], 1) * 10
            if cnum[-1] in C_number:
                num += C_number[cnum[-1]]
            return num

def main(str_get_input):
    get_input = str_get_input.split()
    try: rubbish = get_input[0]
    except:print("无输入")
    else:
        if get_input[0] == "整数":
            if get_input[2] != "等于":
                print("输入不符合规则")
            else :
                define(get_input[1],get_input[3])
        elif get_input[0] == "看看":
            println(get_input[1])
        elif get_input[0] == "无":
            print("无")
        elif get_input[0] == "如果":
            ifelse(str_get_input)
        else :
            if get_input[1] == "增加":
                add(get_input[0],get_input[2])
            elif get_input[1] == "减少":
                subtract(get_input[0],get_input[2])
            elif get_input[1] == "乘以":
                multiplication(get_input[0],get_input[2])
            elif get_input[1] == "除以":
                division(get_input[0],get_input[2])
            else :
                print("输入不符合规则")
while True :
    str_get_input = input()
    main(str_get_input)

