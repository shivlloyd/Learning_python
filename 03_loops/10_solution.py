import time

wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
    print(f"Attempt {attempts + 1} - wait time {wait_time} seconds")
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1


"""
It begins by setting the initial wait time to 1 second and initializing the number of attempts to 0. 
The code enters a while loop that continues as long as the number of attempts is 
less than the maximum allowed retries. Within each iteration of the loop, 
it prints the current attempt number along with the current wait time in seconds. 
It then pauses execution for the specified wait time using the `time.sleep()` function. 
After waiting, it doubles the wait time for the next attempt by multiplying it by 2. 
Finally, it increments the attempt counter by 1. This process continues until 
the maximum number of retries is reached.
"""
