class Workout():
    def __init__(self, duration):
        self._duration = duration
  
    @property
    def duration(self):
        return self._duration
    
    @duration.setter
    def duration(self, time):
        self._duration = time
    
def main():
    workout = Workout(60)
    print("The workout is:", workout.duration, "minutes long")

    workout.duration = 30
    print("New length:", workout.duration, "minutes long")

if __name__ == "__main__":
    main()
    