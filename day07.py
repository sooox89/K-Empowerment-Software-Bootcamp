# class
class Shape:
    def __init__(self, x ,y):
        self.x = x
        self.y = y

    def get_area(self):
        print('면적을 출력합니다')

class Circle(Shape):
    def __init__(self,x,y,radius):
        super().__init__(x,y)
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, x, y, width, length):
        super().__init__(x, y)
        self.width = width
        self.length = length

    def get_area(self):
        return  self.width * self.length

class Cylinder(Circle):
    def __init__(self, x, y, radius, height):
        super().__init__(x, y,radius)
        self.height = height

    def get_area(self):  # get volume
        return super().get_area() * self.height


cy1 = Cylinder(20,20, 10.2, 2)
c1 = Circle(100, 100, 10.0)
c2 = Circle(50,50,2.0)
r1 = Rectangle(100, 50, 5, 2)

print(f'사각형의 좌표는 x:{r1.x},y:{r1.y}이고 넓이는 {r1.get_area()}이다')
print(r1.get_area())
print(c1.get_area())
print(c2.get_area())















# class Duck():
#     color = 'red'
#     def __init__(self, input_name):
#         self.__hidden_name = input_name
#
#     @staticmethod ##
#     def test():
#         print('정적 메소드')
#     @classmethod  ##
#     def ace(cls):
#         print('클래스 메소드')
#     @property
#     def name(self):
#         print('inside the getter')
#         return self.__hidden_name
#     @name.setter
#     def name(self, input_name):
#         print('instide the setter')
#         self.__hidden_name = input_name
#
# don = Duck('Donald')
# print(Duck.ace(),Duck.test(),don.ace(),don.test())
# print(don.color, Duck.color)
# don.color = 'blue'
# print(don.color, Duck.color)
# Duck.color = 'green'   # 클래스 변수 값 변경
# d2 = Duck('Induk')
# print(don.color, Duck.color, d2.color)
#
#
#
#
#
# # don = Duck('Donald')
# # # print(don.get_name)
# # don.name = 'Donna'
# # print(don.name)
# # don.name = 'Kim inha'
# # print(don.name)
#
# # #mixin
# # class PrettyMixin():
# #     def time_print(self):
# #         import datetime
# #         print(datetime.date.today())
# #
# #     def dump(self):
# #         import pprint
# #         pprint.pprint(vars(self))
# #
# # class Thing(PrettyMixin):
# #     pass
# #
# #
# # t= Thing()  #객체 : t // 실행 시점의 객체 : self  // C++에서는 this
# # t.time_print()
# # t.name = 'Nyarlathotep'
# # t.feature = 'ichor'
# # t.age = 'eldritch'
# # t.gender = 'female'
# # t.gender = 'male'
# # t.dump()
# #
# #
# #
# #
#
#
#
#
#
#
#
#
#
#
#
#
# #
# # class Pokemon:
# #     def __init__(self, owner, skills):
# #         self.owner = owner
# #         self.skills = skills.split('/')
# #         print(f"포켓몬 생성 :", end=' ')
# #
# #     def info(self):
# #         print(f"{self.owner}의 포켓몬이 사용 가능한 스킬")
# #         # for skill in self.skills:
# #         #     print(skill)
# #         for i in range(len(self.skills)):
# #             print(f'{i+1} : {self.skills[i]}')
# #     def attack(self, idx):
# #         print(f'{self.skills[idx]} 공격 시전!')
# #
# #
# # class Pikachu(Pokemon):  # inheritance
# #     def __init__(self, owner, skills):
# #         super().__init__(owner, skills)
# #         self.name = "피카츄"
# #         print(f"{self.name}")
# #
# #     def attack(self, idx):  # override
# #         print(f'{self.owner}의 {self.name}가 {self.skills[idx]} 공격(전기) 시전!')
# #
# #
# # class Ggoboogi(Pokemon):  # inheritance
# #     def __init__(self, owner, skills):
# #         super().__init__(owner, skills)
# #         self.name = "꼬부기"
# #         print(f"{self.name}")
# #
# #     def attack(self, idx):  # override
# #         print(f'{self.owner}의 {self.name}가 {self.skills[idx]} 공격(물) 시전!')
# #
# #     def swim(self):
# #         print(f'{self.name}가 수영을 합니다')
# #
# # while True:
# #     menu = input('1) 포켓몬 생성 2) 프로그램 종료 : ')
# #     if menu == '2':
# #         print('프로그램을 종료합니다')
# #         break
# #     elif menu == '1':
# #         pokemon = input('1)피카츄 2) 꼬부기 3) 파이리 : ')
# #         if pokemon == '1':
# #             name = input('플레이어 이름 입려 : ')
# #             skill = input('사용 가능한 기술 입력(/로 구분하여 입력) : ')
# #             p = Pikachu(name,skill)
# #         elif pokemon == '2':
# #             name = input('플레이어 이름 입려 : ')
# #             skill = input('사용 가능한 기술 입력(/로 구분하여 입력) : ')
# #             p = Ggoboogi(name,skill)
# #         elif pokemon == '3':
# #             name = input('플레이어 이름 입력: ')
# #             skill = input('사용 가능한 기술 입력(/로 구분하여 입력) : ')
# #         else:
# #             print('메뉴에서 골라주세요')
# #         info_attack = input('1) 정보 조회 2) 공격 : ')
# #         if info_attack == '1':
# #             p.info()
# #         elif info_attack == '2' :
# #             p.info()
# #             attack_menu = input('공격 번호 선택 : ')
# #             p.attack(int(attack_menu)-1)
# #         else:
# #             print('메뉴에서 골라주세요')
# #
# #     else :
# #         print('메뉴에서 골라주세요')
# #
# # # p0 = Pokemon('아이리스', '어떤공격')
# # # p0.attack(0)
# # # # p0.swim()  # 꼬부기 클래스의 객체들이 사용할 수 있는 고유 메서드
# # #
# # # pk1 = Pikachu('한지우', '번개/100만 볼트')
# # # #pk1.info()
# # # ggo1 = Ggoboogi('오바람', '고속스핀/거품/몸통박치기')
# # # #ggo1.info()
# # # ggo1.swim()
# # # ggo1.attack(2)
# # # pk1.attack(1)
# #
