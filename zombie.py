import random, os

class Zombie:
    top: int
    left: int
    head: str
    head_rotate: str
    trunk: str
    trunk_rotate: str
    left_arm: str
    left_arm_rotate: str
    right_arm: str
    right_arm_rotate: str
    left_leg: str
    left_leg_rotate: str
    right_leg: str
    right_leg_rotate: str
    
    def __init__(self, top: int, left: int, head: str, trunk: str, left_arm: str, right_arm: str, left_leg: str, right_leg: str):
        self.top = top
        self.left = left
        self.head = head
        self.trunk = trunk
        self.left_arm = left_arm
        self.right_arm = right_arm
        self.left_leg = left_leg
        self.right_leg = right_leg
    
    def __init__(self, top: int, left: int):
        self.top = top
        self.left = left
        self.head = ' ' if random.randint(0, 1) else Zombie.get_random_skin()
        self.head_rotate = random.randint(-60, 60)
        self.trunk = Zombie.get_random_skin()
        self.left_arm = ' ' if random.randint(0, 1) else Zombie.get_random_skin()
        self.left_arm_rotate = random.randint(0, 90)
        self.right_arm = ' ' if random.randint(0, 1) else Zombie.get_random_skin()
        self.right_arm_rotate = random.randint(0, 90)
        self.left_leg = ' ' if random.randint(0, 1) else Zombie.get_random_skin()
        self.left_leg_rotate = random.randint(0, 90)
        self.right_leg = ' ' if random.randint(0, 1) else Zombie.get_random_skin()
        self.right_leg_rotate = random.randint(0, 90)
        
    #def __init__(self):
    #    self.__init__(self, random.randint(10, 400), random.randint(10, 400))
        
    def get_random_skin() -> str:
        return "/static/image/skin/" +  random.choice(os.listdir("static/image/skin/")) #change dir name to whatever
        