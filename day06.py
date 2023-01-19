#ch 10 객체 class
#
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



class Pikachu(Pokemon): #inheritance
    pass

pi1= Pikachu('피카츄', '덴트', '번개')
pi1.info()    ##??

p1 = Pokemon('피카츄', '한지우', '50만 볼트/100만 볼트/번개')
p2 = Pokemon('꼬부기', '양수경', '우하하/배고파/날룸')