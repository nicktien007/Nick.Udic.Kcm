from datetime import datetime


def show_current_time():
    return datetime.now().strftime("%H:%M:%S")