class cls :
    x, y = 10, 20

    def change(self) : 
        temp = self.x
        self.x = self.y
        self.y = temp


a = cls()
print(a.x, a.y)
a.change()
print(a.x, a.y)