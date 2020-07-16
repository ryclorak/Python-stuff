class Motorcycle:

  def __init__(self, speed=0):
    self.speed = speed
    self.odometer = 0
    self.time = 0
		
  def SayState(self):
    print("I'm going {} mph!".format(self.speed))
		
  def Accelerate(self):
    self.speed += 5
		
  def Brake(self):
    if self.speed == 0:
      print("I've stopped!")
    else:
      self.speed -= 5
		
  def Step (self):
    self.odometer += self.speed
    self.time += 1
    
  def AverageSpeed(self):
    if self.time != 0:
      return self.odometer / self.time
    else:
      pass
            

if __name__ == '__main__':

  myBike = Motorcycle()
  print("I'm a Motorbichael!")
  while True:
    action = input("What should I do? [A]ccelerate, [B]rake, "
                    "show [O]dometer, or show average [S]peed?").upper()
        
    if action not in "ABOS" or len(action) != 1:
      print("What?")
      continue
    if action == 'A':
      myBike.Accelerate()
    elif action == 'B':
      myBike.Brake()
    elif action == 'O':
      print("The Motorbichael has ridden {} miles".format(myBike.odometer))
    elif action == 'S':
      print("The Motorbichael's average speed was {} mph".format(myBike.AverageSpeed()))
    
    myBike.Step()
    myBike.SayState()