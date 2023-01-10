import threading
import time


def ham_in(thread):
    if(thread == 1):
        time.sleep(3)
    print(f"Đây là thread thứ {thread}")
    print(f"luồng {thread} kết thúc")


if __name__ == '__main__':
    threads = []
    for i in range(5):
        thread = threading.Thread(target=ham_in, args=(i,))
        threads += [thread]

    for thread in threads:
        thread.start()


