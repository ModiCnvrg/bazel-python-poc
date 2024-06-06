import time
from datetime import datetime

def main():
    while True:
        # Print the current date and time
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        # Wait for one second
        time.sleep(1)

if __name__ == "__main__":
    main()
