class student :
    grade = 8
    name = "idah"

    def intro(self):
        print("i am a kidnapper")

    def details(self):
        print("i am in grade ", self.grade)
        print("i have kidnapped ", self.name)

ob = student()
ob.intro()
ob.details()