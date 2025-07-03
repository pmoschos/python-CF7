class MyTime:
    def __init__(self, hours=0, minutes=0, seconds=0):
        # Initialize the time attributes        
        self.hours = hours        
        self.minutes = minutes        
        self.seconds = seconds
    
    def to_seconds(self):
        # Convert the current time to total seconds
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def increment(self, seconds):
        # Add seconds to the current time        
        self.seconds += seconds
        
        # Adjust the minutes and seconds if seconds exceed 60
        while self.seconds >= 60:
            self.seconds -= 60            
            self.minutes += 1

        # Adjust the hours and minutes if minutes exceed 60
        while self.minutes >= 60:
            self.minutes -= 60            
            self.hours += 1
        
        # def display_time(self):
        def __str__(self):
            # Display the time in HH:MM:SS format
            return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

        def add_time(self, other):
            # Add time from another MyTime instance
            total_seconds = self.to_seconds() + other.to_seconds()
            result = MyTime()  # Create a new MyTime instance to store the result
            result.increment(total_seconds)
            return result

# Create two MyTime objects
time1 = MyTime(1, 30, 45)
time2 = MyTime(2, 45, 10)

# Increment the first time by 90 seconds
time1.increment(90)
print("After incrementing time1 by 90 seconds:", time1)
# Output: After incrementing time1 by 90 seconds: 01:32:15

# Add the two MyTime objects using the add_time method
time3 = time1.add_time(time2)
print("After adding time1 and time2 (using add_time):", time3)
# Output: After adding time1 and time2 (using add_time): 04:17:25

# Add the two MyTime objects using the + operator
time4 = time1 + time2
print("After adding time1 and time2 (using + operator):", time4)
# Output: After adding time1 and time2 (using + operator): 04:17:25