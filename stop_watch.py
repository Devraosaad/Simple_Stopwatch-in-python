import time 
current_time = time .localtime()
print(time .strftime(f"the date is %d/%m/%Y and the time is %H:%M:%S", current_time))
class stop_watch():
     def __init__(self):
          self.time_start = None
          
          self.elapsed_time = 0
          self.running = False
     
     def start(self):
         if not self.time_start:
            self.start_time = time.time() - self.elapsed_time
            self.running= True
            print("Stopwatch started.")

     def stop (self):
         if self.running:
             self.elapsed_time = time.time() - self.start_time
             self.running = False
             print("Stopwatch stopped.")

     def get_elapsed_time(self):
        if self.running:
            return time.time() - self.start_time
        else:
            return self.elapsed_time

     def __str__(self):
         elapsed_time = self.get_elapsed_time()
         minutes, seconds = divmod(elapsed_time, 60)
         return f"{int(minutes):02}:{seconds:05.2f}"







stopwatch = stop_watch()

while True:
    print("Enter a command (start, stop, reset, time, quit):")
    command = input().strip().lower()

    if command == "start":
        stopwatch.start()
    elif command == "stop":
        stopwatch.stop()
    elif command == "reset":
        stopwatch.reset()
    elif command == "time":
        print(f"Elapsed time: {stopwatch}")
    elif command == "quit":
        break
    else:
        print("Invalid command. Please enter start, stop, reset, time, or quit.")
