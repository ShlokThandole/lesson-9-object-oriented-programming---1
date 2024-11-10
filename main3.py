class parrot:
    species = "bird"

    def __init__(self,name,age):
        self.name = name
        self.age = age

suu = parrot("suu", 60)
kha = parrot("kha", 90)

print("suu is a {}".format(suu.species))
print("skha is also a {}".format(kha.species))

print("soon {}'ll be {} years old".format(suu.name, suu.age))
print("soon {}'ll be {} years old".format(kha.name, kha.age))