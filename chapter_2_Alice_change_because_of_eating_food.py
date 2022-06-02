# 앨리스 객체
# 상태 : 키, 위치, 손에 있는 것
# 행동 : 음식을 먹으면 키가 작아지거나 커진다
#       키가 적정 수치 이하로 낮아지면 위치를 이동할 수 있다

class Alice:
    def __init__(self):
        self.__height = 160
        self.__location = '하늘정원'
        self.__hand = None

    def get_height(self):
        return self.__height

    def get_location(self):
        return self.__location

    def get_hand(self):
        return self.__hand

    def hold_food(self, food):
        self.__hand = food
        print(f'앨리스의 손에 {food.get_name()}이(가) 있습니다.')

    def put_down_food(self):
        self.__hand = None
        print('앨리스의 손에 아무것도 없습니다.')

    def drink_juice(self):
        if type(self.__hand) is not Drink:
            print('앨리스의 손에 음료가 없습니다.')
        else:
            if self.__hand.get_left_over() != 0:
                self.__hand.drunk()
                self.__height -= 50
                print(f'앨리스의 키가 {self.__height}이 되었습니다.')
                if self.__height <= 0:
                    self.__height = 0
                    print('앨리스가 소멸했습니다.')
            print('남아있는 음료가 없습니다.')

    def eat_cake(self):
        pass

    def eat_mushroom(self):
        pass

    def fan_oneself(self):
        pass

    def through_door(self):
        print(f'앨리스의 현재 위치는 {self.__location} 입니다.')
        if self.__height <= 60:
            self.__location = '궁전'
            print(f'{self.__location}으로 이동했습니다.')
        else:
            print(f'현재 앨리스의 키 보다 {self.__height - 60}만큼 작아져야 이동가능합니다.')


class Food:
    def __init__(self):
        self.__name = '음식'
        self.__total = 200
        self.__amount = 0


class Drink(Food):
    def __init__(self):
        super(Drink, self).__init__()
        self.__total = 150
        self.__name = '음료'
        self.__amount = 50

    def get_name(self):
        return self.__name

    def get_left_over(self):
        return self.__total

    def drunk(self):
        if self.__total <= 0:
            self.__total = 0
            print(f'남아있는 {self.__name}이(가) 없습니다.')
        else:
            print(f'꿀꺽꿀꺽 -{self.__amount}')
            self.__total -= self.__amount
            print(f'남아있는 {self.__name}의 양: {self.__total}')


def main():
    alice = Alice()
    juice = Drink()

    print(alice.get_height())
    print(juice.get_left_over())

    alice.hold_food(juice)
    alice.drink_juice()
    alice.through_door()

    alice.drink_juice()
    alice.through_door()

    alice.drink_juice()
    print(alice.get_location())

    alice.drink_juice()

    alice.drink_juice()


if __name__ == "__main__":
    main()

