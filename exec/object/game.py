"""
愤怒的小鸟
"""

class Birds:
    def __init__(self, name, color, skill_desc):
        self.name = name
        self.color = color
        self.skill_desc = skill_desc

    def fly(self):
        pass

    def call(self):
        pass

    def use_skill(self):
        print(f"{self.name}使用了{self.skill_desc}进行了攻击")

class RedBirds(Birds):
    def __init__(self):
        super().__init__("红火","红色", "撞击前方障碍物，造成大量伤害")

    def fly(self):
        print(f"{self.name}以稳定的速度向前飞行...")

    def call(self):
        print(f"{self.name}发出吱吱的声音")

class YellowBirds(Birds):
    def __init__(self):
        super().__init__("黄蜂","黄色","瞬间加速，穿透薄障碍物")

    def fly(self):
        print(f"{self.name}快速向前飞行...")

    def call(self):
        print(f"{self.name}发出嗡嗡的声音")


class BlueBirds(Birds):
    def __init__(self):
        super().__init__("蓝冰", "蓝色", "分裂成三只小鸟，分散攻击")

    def fly(self):
        print(f"{self.name}优雅地向前飞行......")

    def call(self):
        print(f"{self.name}发出喳喳的声音")

class Obstacle:
    def __init__(self,name,strength):
        self.name = name
        self.strength = strength

    def beAttacked(self,bird):
        print(f"{bird.name}向{self.name}发起了攻击")
        bird.use_skill()

        if isinstance(bird, RedBirds):
            damage = 80
        elif isinstance(bird, YellowBirds):
            damage = 50
        else:
            damage = 3*30
        # 障碍物对应的坚固值减去对应伤害值
        self.strength -= damage

        if self.strength <= 0:
            print(f"{self.name}已经被摧毁")
        else:
            print(f"当前障碍物{self.name}还剩{self.strength}点坚固值")

b1 = RedBirds()
b2 = YellowBirds()
b3 = BlueBirds()

o1 = Obstacle("木头堡垒",100)
o2 = Obstacle("石头堡垒",200)

o1.beAttacked(b1)
o1.beAttacked(b2)
o2.beAttacked(b3)