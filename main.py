import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Wash Your Eye!!",
            message = "Reduce Eye Strain.. Be happy",
            app_icon = "photo.ico",
            timeout = 10,
        )
        time.sleep(30*60)
