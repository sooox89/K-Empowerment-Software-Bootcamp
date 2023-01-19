#ch 10 객체 class
#
# class Pokemon:
#     def __init__(self):   # 객체 생성 시 동작
#         print("포켓몬 객체 생성됨")
#
# p1 = Pokemon()   # 코드 0x1008eda90
# p2 = Pokemon()   # 코드 0x1008edad0  // p1, p2 코드 다름
# print(p1,p2)

class Pokemon:
    def __init__(self,name,owner, skills):
        self.name = name
        self.owner = owner
        self.skills = skills.split('/')     ## 리스트 split !
        print(f"포켓몬 {name} 생성됨")

    def info(self):
        print(f'{self.owner}의 포켓몬은 {self.name}입니다')    #실행 시점의 클래스 실행
        for skill in self.skills:
            print(skill)


p1 = Pokemon('피카츄', '한지우', '50만볼트/100만볼트/번개')
p2 = Pokemon('꼬부기', '오바람', '고속스핀/거품/몸통박치기/하이드로펌프')
p2.info()
p1.info()
# print(p2.skills)
# print(f'{p2.owner}의 포켓몬은 {p2.name}입니다')
# print(f'{p1.owner}의 포켓몬은 {p1.name}입니다')
# print(p1,p2)