# 리스트 []
# 순서가 있는 값나열
# 지하철 칸별로 10명, 20명, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호가 몇 번째 칸에 타고있는가?
print(subway.index("조세호"))

# 하하가 다음 정류장에서 다음 칸에 탐 append 맨뒤에 붙음
subway.append("하하")
print(subway)

# 정형돈을 유재석과 조세호 사이에 넣기  index순서를 먼저 적고 넣을 값넣기
subway.insert(1, "정형돈")
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬도 가능
num_list = [1,5,6,8,2,3]
num_list.sort()
print(num_list)

# 순서 뒤집기
num_list.reverse()
print(num_list)

# 모두지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용
mix_list = ['조세호', 20, True]
num_list = [1,5,6,8,2,3]

num_list.extend(mix_list)
print(num_list)
