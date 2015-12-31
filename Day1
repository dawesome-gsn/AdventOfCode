import Utils

class Day1:
    def UpOrDown(self, char):
        if char == '(':
            return 1
        elif char == ')':
            return -1
        else:
            return 0

    def CalculateFloor(self, str):
        floor = 0
        for char in str:
            floor += self.UpOrDown(char)

        return floor

    def FindFirstBasement(self, str):
        floor = 0
        position = 1
        for char in str:
            floor += self.UpOrDown(char)
            if floor < 0:
                return position
            position += 1


if __name__ == '__main__':
    s = Utils.ReadFile('Day1Input.txt')
    print(s)

    day1 = Day1()

    floor = day1.CalculateFloor(s)
    print floor
    firstBasement = day1.FindFirstBasement(s)
    print firstBasement