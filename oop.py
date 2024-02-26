class Human:
        def __init__(self,nm, age, h, w, g, cntry):
                self.name = nm
                self.age = age
                self.height = h
                self.weight = w
                self.gender = g
                self.country = cntry

        def show(self):
                print(f'Name : {self.name}')
                print(f'age : {self.age}')
                print(f'Height: {self.height}')
                print(f'Weight : {self.weight}')
                print(f'gender : {self.gender}')
                print(f'country : {self.country}')

# making objects


h1 = Human('Ram',23,5.3,67,'M','Nepal')
h2 = Human('Shyan',25,5.3,65,'M','India')
h3 = Human('Gita',22,5.2,50,'M','Bhutan')

print(h1)
print(h2)
print(h3)

print(h1.name)
print(h2.name)

h1.show()
print('-'*15)
h3.show()