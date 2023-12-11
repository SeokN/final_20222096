#<오픈소스프로그래밍 기말 프로젝트>
#
# ● 아래의 코드를 수정 혹은 프로그래밍하여 문제를 해결하시오.
# ● 문제의 점수는 각각 표시되며, 부분점수가 존재합니다.
#
# 학번 : 20222096 이름 : 최석현

import os
import time

# Q.1 10점
#
# 문자열 my_string과 target이 매개변수로 주어질 때,
# target이 문자열 my_string의 부분 문자열이라면 1을,
# 아니라면 0을 return 하는 solution 함수를 작성하시오.
#
# 제한사항
# 1 ≤ my_string 의 길이 ≤ 100
# my_string 은 영소문자로만 이루어져 있습니다.
# 1 ≤ target 의 길이 ≤ 100
# target 은 영소문자로만 이루어져 있습니다.

def solution(my_string, target):
    answer = 0
    tmp = my_string.find(target) 
    """
    매개변수 my_string에 target문자열이 포함되어있으면 그 위치값을 tmp에 저장하고,
    포함되어 있지 않으면 -1을 tmp에 저장한다.
    """
    if tmp != -1: # tmp가 -1이 아니면(부분 문자열이라면)
        answer = 1 # answer에 1을 대입한다.
    return answer

# Q.2 10점
#
# 모스부호 해독 프로그램 만들기
# 문자열 letter 가 매개변수로 주어질 때,
# letter 영어 소문자로 바꾼 문자열을 return 하는
# solution 함수를 완성하시오.
#
# 제한사항
# 1 ≤ letter 의 길이 ≤ 1,000
# letter 의 모스부호는 공백으로 나누어져 있습니다.
# letter 에 공백은 연속으로 두 개 이상 존재하지 않습니다.
#
# letter = 여러분의 좌우명 또는 인상 깊었던 말을 쓰시오.

def solution(letter):
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'}
    str = letter.split() # 매개변수로 입력받은 letter 문자열을 공백 기준으로 나누어 str 리스트에 선언한다.
    answer = ''
    for i in range (len(str)):
        answer += morse[str[i]] # 딕셔너리 자료를 호출하여 공백 기준으로 나뉜 모스부호를 알파벳으로 변환한다.
    return answer

# Q.3 10점
#
# 행성의 나이를 알파벳으로 표현할 때,
# a는 0, b는 1, ..., j는 9
# 예를 들어 cd는 23살, fb는 51살입니다.
# age가 매개변수로 주어질 때
# PROGEAMMER-857식 나이를 return 하도록
# solution 함수를 완성하시오.
#
# 제한사항
# age는 자연수입니다.
# age ≤ 1,000
# PROGRAMMERS-857 행성은 알파벳 소문자만 사용합니다.

def solution(age):
    answer = ''
    tmp = list(str(age)) # 매개변수로 입력받은 정수를 string형태로 바꾸어 한자리씩 리스트에 저장
    res = [] # 빈 리스트 res 생성
    for i in range(len(tmp)):
        res.append((chr(int(tmp[i])+97))) # chr함수를 이용하여 tmp 원소를 문자로 변환한 뒤, a의 아스키코드인97을 더해 알파벳으로 표현한다.
    
    for j in range(len(res)):
        answer += res[j] # answer문자열에 res의 원소를 하나씩 삽입한다.
    return answer

# Q.4 10점
#
# x축과 y축으로 이루어진 2차원 직교 좌표계에 중심이 원점인
# 서로 다른 크기의 원이 두 개 주어집니다.
# 반지름을 나타내는 두 정수 r1, r2가 매개변수로 주어질 때,
# 두 원 사이의 공간에 x좌표와 y좌표가 모두 정수인 점의 개수를
# return하도록 solution 함수를 완성해주세요.
# ※ 각 원 위의 점도 포함하여 셉니다.
#
# 제한사항
# 1 ≤ r1 < r2 ≤ 1,000,000
import math
def solution(r1, r2):
    answer = 0
    for i in range(1, r2+1):
        k1 = math.floor((r2**2 - i**2)**(1/2)) # 원의 방정식을 이용하여 1사분면의 r2안에 있는 점들을 구함.
        if(i < r1):
            k2 = math.ceil((r1**2 - i**2)**(1/2)) # 원의 방정식을 이용하여 1사분면의 r1안에 있는 점들을 구함.
        else: k2 = 0
        answer += k1 - k2 + 1 # 1사분면의 r2 점 개수에서 r1 점 개수를 차감하여 r2와 r1사이의 점들의 개수를 구함.
    return (answer)*4 # 1사분면만 구했기 때문에 4배를 하여 리턴해줌.

# Q.5 10점
#
# 0 또는 양의 정수가 주어졌을 때,
# 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
#
# 예를 들어, 주어진 정수가 [6, 10, 2]라면
# [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,
# 이중 가장 큰 수는 6210입니다.
#
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어
# return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
#
# numbers = [8, 30, 17, 2, 23]

def solution(numbers):
    answer = ''
    sum = 0
    numlist = list(map(str, numbers)) # 매개변수로 입력받은 numbers를 string 형태로 모두 바꾸어 numlist에 저장.
    for i in range(len(numlist)):
        numlist[i] = numlist[i]*4 # numlist의 원소들을 모두 4배의 길이로 늘림.
        numlist[i] = numlist[i][0:4] # 4배로 늘어난 numlist의 원소들을 모두 4글자로 잘라냄.
    numlist = list(map(int, numlist)) # string 형태의 numlist 원소들을 int형으로 변환함.
    for i in range(len(numlist)):
        sum += numlist[i] # numlist의 원소들의 합을 sum변수에 저장함.
    numbers = [i for _, i in sorted(zip(numlist, numbers))] # zip 함수를 통해 numlist 기준으로 numbers 배열을 정렬한다.
    numbers.reverse() # sorted함수의 기본 동작은 오름차순인데, 필요한 것은 내림차순 정렬이기에 reverse함수를 이용해 뒤집어준다.
    numbers = list(map(str, numbers)) # numbers배열의 원소를 모두 string형으로 변환해준다. 
    if (sum != 0): 
        for i in range(len(numbers)):
            answer += numbers[i] # answer 문자열에 numbers 원소를 하나씩 삽입해주어 문자열로 만들어준다.
    else:
        answer += '0' # 매개변수로 입력되는 numbers배열이 모두 0이면 0000.. 식으로 출력되기에 만약 0만 입력된다면 0만 출력되도록 조건문을 설정하였다.
    return answer