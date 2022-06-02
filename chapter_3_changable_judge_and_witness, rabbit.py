# 협력관계 : 판사 - 토끼 - 증인
# 각각의 역할과 상태
# 판사의 역할 : 목격자 호출 명령
# 판사의 상태 : 재판하라는 호출을 받아들일 수 있어야 함
# 토끼의 역할 : 증인 호출 명령
# 토끼의 상태 : 증인을 알고 있어야 함
# 증인의 역할 : 증언
# 증인의 상태 : 사건에 대한 내용을 알고 있어야 함

# 위의 상태와 역할에 만족한다면 어떠한 객체가 와도 관계 없음

class Judge:
    def __init__(self):
        self.__authority = 1
        self.__name = '하트왕'
        self.__rabbit = None
        self.__witness = None

    def get_judge_authority(self):
        return self.__authority

    def get_judge_name(self):
        return self.__name

    def command_call_witness(self, rabbit):
        if type(rabbit) is not Rabbit:
            print('목격자를 불러올 수 있는 객체가 아닙니다.')
            self.__rabbit = None
            return False
        self.__rabbit = rabbit
        print(f'{self.__name}: 목격자를 불러와라!')
        rabbit.command_enter_witness_their_seat()

    def command_testify(self, witness):
        if type(witness) is not Witness:
            print('증언할 수 있는 증인이 아닙니다.')
            self.__witness = None
            return False
        self.__witness = witness
        print(f'{self.__name}: 증언하라!')
        witness.testify_to_judge()


class Rabbit:
    def __init__(self):
        self.__aware_of_witness = ['Alice', 'Hat_merchant', 'Cook']
        self.__name = '토끼'
        self.__seat = None

    def get_seat_condition(self):
        return self.__seat

    def command_enter_witness_their_seat(self):
        print(f'{self.__name}: 증인석에 입장하라')
        self.__seat = self.__aware_of_witness[0]
        print(f'{self.__seat} 착석')


class Witness:
    def __init__(self):
        self.__aware_of_accident = '제가 확실히 보았습니다!'
        self.__name = '모자 장수'

    def testify_to_judge(self):
        print(f'{self.__name}: {self.__aware_of_accident}')


def main():
    judge = Judge()
    rabbit = Rabbit()
    witness = Witness()

    judge.command_call_witness(rabbit)
    judge.command_testify(witness)


if __name__ == "__main__":
    main()
