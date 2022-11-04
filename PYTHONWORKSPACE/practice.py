print(5)
print(-10)
print(3.14)
print(5+2)
print(2*8)
print(3*(3+1))
print('풍선')
print('ㅋ'*8)
# 참/거짓
print(4>10)
print(4<10)
print(True)
print(not True)
print(not False)
print(not(5>10))
# 애완동물을 소개해 주세요~
animal = '강아지'
name = '연탄이'
age = 4
hobby = '산책'
is_adult = age >= 3

print('우리집 '+ animal+ '의 이름은 '+name+ '이예요')
print(name+ '는 '+str(age)+' 살이며, '+hobby+'을 아주 좋아해요')
print(name+ '는 어른일까요?' + str(is_adult))

'''이렇게 하면 
긴 주석이 됩니다
으하하하
'''

station = '사당', '신도림', '인천공항'
print(station,'행 열차가 들어오고 있습니다.')

print(5//2) #2

print(2 + 3 *4) # 14
print((2+3)*4) # 20
number = 2 + 3 * 4 # 14
print(number)
number = number + 2 # 16
number +=2 # 18
print(number)
number *=2 # 36
print(number)
number /=2 #18
print(number)
number-=2 #16
print(number)

number%= 5 #1
print(number)

print(abs(-5)) #5 절대값
print(pow(4,2)) # 4^2 = 4*4  = 16 제곱

print(max(5, 12)) # 12
print(min(5, 12)) # 5

print(round(3.14)) # 3 = 반올림
print(round(4.99))

from math import *
print(floor(4.99)) # 내림. 4
print(ceil(3.14)) # 올림. 4
print(sqrt(16)) # 제곱근. 4