import win32api
import win32con
import time

def click(x, y):
    # Move the cursor to the position (x, y)
    win32api.SetCursorPos((x, y))
    
    # Perform left mouse button down and up actions to simulate a click
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

# Function to calculate clicks per second
def measure_clicks_per_second(num_clicks, x, y):
    start_time = time.time()  # Start time before the clicks
    
    # Perform the specified number of clicks
    for _ in range(num_clicks):
        click(x, y)
    
    end_time = time.time()  # End time after the clicks
    
    # Calculate the duration and clicks per second
    duration = end_time - start_time
    clicks_per_second = num_clicks / duration
    
    return clicks_per_second, duration

# Example usage
x, y = 500, 500  # The coordinates where you want to click
num_clicks = 1000  # The number of clicks to measure

clicks_per_second, duration = measure_clicks_per_second(num_clicks, x, y)
print(f"Performed {num_clicks} clicks in {duration:.4f} seconds")
print(f"Clicks per second: {clicks_per_second:.2f}")
