from classandfunctions.error_message import error


class MultiItems:
    def __init__(self, won, yang, miktar):
        self.won = won
        self.yang = yang
        self.miktar = miktar

    @staticmethod
    def multi_calculate(*args):
        total_won = 0
        total_yang = 0
        for item in args:
            if item.won == '' or item.yang == '':
                error()
            else:
                yang_to_won = int(item.yang) * int(item.miktar)
                created_won = yang_to_won // 100
                yang_left = yang_to_won % 100
                total_won += int(item.won) * int(item.miktar)
                total_won += created_won
                total_yang += yang_left
        return total_won, total_yang
