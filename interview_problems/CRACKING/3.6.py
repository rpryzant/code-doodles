import time


class PetShop:
    def __init__(self):
        self.dogs = []
        self.cats = []
        
    def adopt(self, pet):
        if pet.type == 'dog':
            self.dogs.append((pet, time.time()))
        elif pet.type = 'cat':
            self.cats.append((pet, time.time()))
        else:
            print 'err'

    def get_dog(self):
        return self.dogs.pop()[0] if self.dogs else None

    def get_cat(self):
        return self.cats.pop()[0] if self.cats else None

    def get_pet(self):
        if self.dogs and self.cats:
            return self.dogs.pop()[0] if self.dogs[-1][1] < self.cats[-1][1] else self.cats.pop()[0]
        else:
            if self.dogs:
                return self.dogs.pop()[0]
            elif self.cats:
                return self.cats.pop()[0]
            else:
                return None
