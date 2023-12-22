class Home:
    def __init__(self, width, breadth):
        self.width = width
        self.breadth = breadth

    def room1(self):
        print('Area of room1:', self.width * self.breadth)

    def kitchen(self):
        print('Area of kitchen:', self.width * self.breadth)


class FirstHome(Home):
    def __init__(self, width, breadth):
        super().__init__(width, breadth)

    def study_room(self):
        print('This home has an extra study room.')


class SecondHome(Home):
    def __init__(self, width, breadth):
        super().__init__(width, breadth)

    def work_area(self):
        print('This home has a work area.')



first_home = FirstHome(100, 100)
second_home = SecondHome(1222, 4888)


first_home.room1()
first_home.kitchen()

second_home.room1()
second_home.kitchen()


first_home.study_room()
second_home.work_area()