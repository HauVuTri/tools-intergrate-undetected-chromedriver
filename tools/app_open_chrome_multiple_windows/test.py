import threading
import time

# Global variable
statuses = {}

# Lock to control access to the global variable
lock = threading.Lock()

def worker_thread(thread_name):
    global statuses
    global lock

    # Acquire the lock to update the global variable
    lock.acquire()
    status[thread_name] = "running"
    # Release the lock
    lock.release()
    time.sleep(thread_name+1)

    # Do some work here...
    # Update the status again
    lock.acquire()
    status[thread_name] = "done"
    lock.release()

# Create and start worker threads
for i in range(3):
    t = threading.Thread(target=worker_thread, args=(i,))
    t.start()

# Main thread
while True:
    # Acquire the lock to read the global variable
    lock.acquire()
    print(statuses)
    # Release the lock
    lock.release()
    time.sleep(0.5)
