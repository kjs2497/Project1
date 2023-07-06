## 함수부
def add_func(n1, n2) :
    return n1+n2

def sub_func(n1, n2) :
    return n1-n2

def xxx_func(n1, n2) :
    return n1*n2

def yyy_func(n1, n2) :
    return n1/n2

## 전역 변수부
num1, num2, result = 100, 200, 0


## 메인 코드부
result = add_func(num1, num2)
print(num1, '+', num2, '=', result)

result = sub_func(num1, num2)
print(num1, '-', num2, '=', result)

result = xxx_func(num1, num2)
print(num1, '*', num2, '=', result)

result = yyy_func(num1, num2)
print(num1, '/$RECYCLE.BIN', num2, '=', result)
