# Introduction to classes

class Bot():
    
    def __init__(self, posx, posy):
        self.posx = posx
        self.posy = posy
    
    def move(self, speedx, speedy):
        self.posx += speedx
        self.posy += speedy
    
bot = Bot(3, 4)
bot.move(2, -1)
print(bot.posx, bot.posy)

# ex 1

class Car():

    def __init__(self, maxspeed, acceleration):
        self.maxspeed = maxspeed
        self.acceleration = acceleration

    def acceltime(self, currentspeed):
        t = (self.maxspeed-currentspeed) / self.acceleration
        return t

car = Car(75, 3.5)
time = car.acceltime(30)
print(time)