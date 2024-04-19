def calculate_result(number):
    units = number % 10
    tens = (number // 10) % 10
    hundreds = (number // 100) % 10
    thousands = (number // 1000) % 10
    ten_thousands = (number // 10000) % 10
    
    result = (tens ** units) * hundreds
    result /= ten_thousands - thousands
    
    return result


number = 46275
result = calculate_result(number)
print(result)