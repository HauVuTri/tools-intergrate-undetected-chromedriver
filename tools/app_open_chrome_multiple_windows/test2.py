import threading
from queue import Queue

status_queue = Queue()
thread_status = {}

def worker_thread(thread_name):
    # Do some work here...
    status_queue.put((thread_name, "running"))
    # Update the status again
    status_queue.put((thread_name, "done"))

# Create and start worker threads
for i in range(3):
    t = threading.Thread(target=worker_thread, args=(i,))
    t.start()

# Main thread
while True:
    thread_name, thread_status = status_queue.get()
    thread_status[thread_name] = thread_status
    print(thread_status)
