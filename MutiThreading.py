import requests
import threading
import datetime

def number_needed():
    url = r'https://www.google.com'
    r = requests.get(url)
    print('req',str(threading.current_thread()))

def multithread():
    for i in range(21):
        if threading.active_count() == 11:
            print('reached count')
            while threading.active_count() !=1:
                continue
        else:
            t1 = threading.Thread(target=number_needed)
            t1.start()
    print('Threading Ends Now')


def single():
    for i in range(21):
        number_needed()

if __name__ == "__main__":
    print('asd')
    x = datetime.datetime.now()
    single()
    y = datetime.datetime.now()
    print(y-x)
    x = datetime.datetime.now()
    multithread()
    y = datetime.datetime.now()
    print(y-x)
    