from queue import Queue
import random


class ServiceCenter:
    def __init__(self):
        self.queue = Queue()

    def generate_request(self):
        num_applications = random.randint(1, 10)

        for i in range(num_applications):
            self.queue.put(i)

    def process_request(self):
        while not self.queue.empty():
            current_applic = self.queue.get()
            print(f"Application {current_applic} was processed.")

        print("The queue is empty!")


center = ServiceCenter()

while True:
    user_input = input("Click Enter or type \"exit\":")

    if user_input.lower() == "exit":
        print("Exit the program")
        break  

    center.generate_request()
    center.process_request()
