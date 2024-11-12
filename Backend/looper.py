import requests
import schedule
import time

# Function to trigger the route every 2 minutes
def trigger_route_every_two_minutes():
    try:
        # Send a GET request to the trigger_route API
        response = requests.get('http://127.0.0.1:8080/trigger_route')
        
        # Print the response from the API
        if response.status_code == 200:
            print("API Triggered Successfully!")
            print(response.json())
        else:
            print(f"Failed to trigger API. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error occurred: {e}")

# Schedule the function to run every 2 minutes
schedule.every(2).minutes.do(trigger_route_every_two_minutes)

# Run the scheduler continuously
if __name__ == "__main__":
    while True:
        schedule.run_pending()  # Run scheduled jobs
        time.sleep(1)  # Sleep to avoid high CPU usage
