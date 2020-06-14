'''
1.设定一个回合制2人对打游戏，每个人物都有hp，power,skill
hp代表血量，power代表攻击力，skill将攻击力翻倍
每三个回合可以使用一次skill
'''
import yaml


#
# data=[]
#
# with open("game.yml","w") as f:
#     yaml.dump(data,f)

class Game:
    def __init__(self):
        infor = yaml.safe_load(open("./game.yaml"))
        print(infor)
        default = infor["default"]
        self.first = default[0]
        self.second = default[1]
        # 定义第一个人物
        self.first_hp = infor[self.first]["hp"]
        self.first_power = infor[self.first]["power"]
        self.first_skill = infor[self.first]["skill"]

        # 第二个人物
        self.second_hp = infor[self.second]["hp"]
        self.second_power = infor[self.second]["power"]
        self.second_skill = infor[self.second]["skill"]

    def fight(self):
        round = 0

        while True:
            print(self.first, self.first_hp)
            print(self.second, self.second_hp)

            round += 1
            if round % 3 == 0:
                self.first_hp = self.first_hp - self.second_power * self.second_skill
                self.second_hp = self.second_hp - self.first_power * self.first_skill
            else:
                self.first_hp = self.first_hp - self.second_power
                self.second_hp = self.second_hp - self.first_power
            if self.first_hp <= 0:
                print("{}lose".format(self.first))
                break
            elif self.second_hp <= 0:
                print("{}lose".format(self.second))
                break


if __name__ == '__main__':
    game = Game()
    game.fight()
