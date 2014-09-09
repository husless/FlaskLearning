from threading import Thread

def async(func):
    def wrapper(*args, **kwargs):
        thrd = Thread(target=func, args=args, kwargs=kwargs)
        rhrd.start()
    return wrapper
