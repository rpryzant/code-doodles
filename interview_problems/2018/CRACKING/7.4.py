


"""
qs:
   -what kind of cars?
       -there could be
       -cars
       -busses
       -motercycles
       -compacts
       -e.v.'s
   -multiple levels?
   -is the lot independantly operated? or attached to some other buisness like a grocery store

"""




abstract class for vehicle 

class Vehicle:
    parking spots
    license plate
    spots needed
    size
    
    def parkInSpot(spot):
        spots.append(spot)

    def canFitInSpot(spot):
        pass


class Bus(Vehicle):
    spotsneeded = 1
    size = ...

class Motercycle(Vehicle):
    pass

class Bus(Vehicle):
    spotsneeded = 5


class ParkingLot:
    levels = [Levels]

# note that level is seperated from parking lot
# so that spot-finding logic can be serperated out
# from the parking lot class
class Level:
    spots = [ParkingSpot]

    def findAvailableSpots
    
    def parkVehicle

class ParkingSpot:
    def canFitVehicle

    def isAvailable

    def removeVehicle


...
