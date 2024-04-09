# An integer divisible by the sum of its digits is said to be a Harshad number. You are given an integer x. 
# Return the sum of the digits of x if x is a Harshad number, otherwise, return -1.

def HasghedNumber(x: int) -> int:
    sum = 0
    while x != 0: # x = 121
        sum += x%10 # Extrai o resto da divisão -> 121/10, resta => 1
        x = x//10 # Pega o valor da divisão, ignorando o resto -> 121/10 => 12
    return sum

print(HasghedNumber(121))
