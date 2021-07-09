grades = {}

# key - value
grades["현승"] = 80
grades["태호"] = 60
grades["영훈"] = 70
grades["지웅"] = 90
grades["동욱"] = 95

print(grades)
print(grades["동욱"])
print(grades["현승"])

# key 를 이용한 삭제
grades.pop("태호")
grades.pop("지웅")

print(grades)