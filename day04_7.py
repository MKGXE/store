import matplotlib.pyplot as plt         # 그래프 그려주는 라이브러리(부속품)

# 문제 : 80점 이상인 사람의 수
시험점수 = [71, 85, 77, 81, 99, 23, 55, 100, 0]
_80점이상 = []

for i in 시험점수:
    if i >= 80:
        _80점이상.append(i)        
print(_80점이상)
print(len(_80점이상),'명')

# 데이터시각화 
plt.title('test')
plt.xlabel('score')
plt.ylabel('person')
plt.hist(시험점수)      # 막대그래프
plt.show()             # 그려줘