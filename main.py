import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "You need to hydrate yourself!!",
            message = "The National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids for men. About 11.5 cups (2.7 liters) of fluids a day for women.",
            app_icon = "C:\\Users\\ASUS\\Desktop\\Hydrate-Me\\icon.ico",
            timeout=10
        )
        time.sleep(60*60)


# The above notification is for every 1 hr duration

# To run this app as a background process:

# 1.Get to your terminal
# 2.type pythonw .\main.py