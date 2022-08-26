# name = "마린"
# hp = 40
# damage = 5

# print("{} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# name_tank = "탱크"
# hp_tank = 150
# damage_tank = 35

# print("{} 유닛이 생성되었습니다.".format(name_tank))
# print("체력 {0}, 공격력 {1}\n".format(hp_tank, damage_tank))


# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(name, location, damage))

# attack(name, "1시", damage)
# attack(name_tank, "1시", damage_tank)

#일반 유닛
class Unit:
    def __init__(self, name, hp, speed):  #__init__ 생성자
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0}, : {1} 방향으로 이동합니다. [속도 {2}] "\
            .format(self.name, location, self.speed))



# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True #클래스 외부에서 변수 추가

# if wraith2.clocking == True:
#     print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

#공격 유닛
class AttackUnit(Unit): #Unit 에 상속 받아 만들어짐
    def __init__(self, name, hp, speed ,damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))
    
    def damaged(self, damage):
        print("{0}, : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} :  현재 체력은 {1} 입니다. ".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))
    
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# firebat1.damaged(25)
# firebat1.damaged(25)

#날 수 있는 클래스
class Flyable :
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

#공중 공격 유닛 클래스

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self,name,hp,0,damage) #지상 스피드 0
        Flyable.__init__(self,flying_speed)
    
    def move(self, location):
        print("[공중유닛 이동]")
        self.fly(self.name, location)

# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")

# vulture =  AttackUnit("벌처", 80, 10, 20)

# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# battlecruiser.move("9시") #지상은 move 공중은 fly 귀찮.

# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         super().__init__(name, hp, 0) #두개 이상의 다중 상속에서는 초기화 필요 #클래스 2
#         self.location = location
        
    
