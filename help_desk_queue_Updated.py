<<<<<<< HEAD
# Import the Node class you created in node.py
from node_Updated import Node

# Implement your Queue class here
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_customer = Node(value)
        if not self.front:
            self.front = new_customer
            self.rear = new_customer
        else:
            self.rear.next = new_customer
            self.rear = new_customer
    
    def dequeue(self):
        if not self.front:
            return None
        removed_customer = self.front
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return removed_customer.value
    
    def peek(self):
        if self.front:
            return self.front.value
        else:
            return None
    
    def print_queue(self):
        current = self.front
        if not current:
            print("Queue is empty")
            return
        while current:
            print(f"- {current.value}")
            current = current.next

    


def run_help_desk():
    # Create an instance of the Queue class
    help_desk_queue = Queue()


    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter customer name: ")
            # Add the customer to the queue
            help_desk_queue.enqueue(name)
            print(f"{name} added to the queue.")
        
        elif choice == "2":
            # Help the next customer in the queue and return message that they were helped
            helped_customer = help_desk_queue.dequeue()
            if helped_customer:
                print(f"{helped_customer} has been helped")
            else:
                print("No customers in queue")


        elif choice == "3":
            # Peek at the next customer in the queue and return their name
            next_customer = help_desk_queue.peek()
            if next_customer:
                print(f"Next Customer: {next_customer}")
            else:
                print("No customers in queue")


        elif choice == "4":
            # Print all customers in the queue
            print("\nWaiting customers:")
            help_desk_queue.print_queue()
            

        elif choice == "5":
            print("Exiting Help Desk System.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_help_desk()

'''For our undo/redo program, a stack is the right choice for this type of scenario because of the
Last-In, First-Out order of operations. In our Undo/Redo program we are looking to undo our most recent
action, as well as redo our most recent action in the undo stack. In other words, we want to have our last
action be the first thing undone and the last thing undone to be the first thing redone. This fits the
usage of a stack perfectly as we are looking to go back through our most recent actions and reverse the
most recent one. For our Help Desk Queue program we are looking to create a list where new customers are 
added to the back and the customers at the front of the queue are taken care of first. In our prgorm this
means putting new entries at the back of the queue and taking out the first entry in the queue when we are
finished with it. This fits a queue well because of the First-In, First-Out order of operations. A queue also
works here because we are handling requests in the order they arrive, when customers request help, and fairness
 and timing matter, first customer to request help, gets helped. The main difference between my implementations
 of Stacks and Queues compared to Lists is that the Lists are more for general purpose storage where Queues and Stacks 
=======
# Import the Node class you created in node.py
from node_Updated import Node

# Implement your Queue class here
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_customer = Node(value)
        if not self.front:
            self.front = new_customer
            self.rear = new_customer
        else:
            self.rear.next = new_customer
            self.rear = new_customer
    
    def dequeue(self):
        if not self.front:
            return None
        removed_customer = self.front
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return removed_customer.value
    
    def peek(self):
        if self.front:
            return self.front.value
        else:
            return None
    
    def print_queue(self):
        current = self.front
        if not current:
            print("Queue is empty")
            return
        while current:
            print(f"- {current.value}")
            current = current.next

    


def run_help_desk():
    # Create an instance of the Queue class
    help_desk_queue = Queue()


    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter customer name: ")
            # Add the customer to the queue
            help_desk_queue.enqueue(name)
            print(f"{name} added to the queue.")
        
        elif choice == "2":
            # Help the next customer in the queue and return message that they were helped
            helped_customer = help_desk_queue.dequeue()
            if helped_customer:
                print(f"{helped_customer} has been helped")
            else:
                print("No customers in queue")


        elif choice == "3":
            # Peek at the next customer in the queue and return their name
            next_customer = help_desk_queue.peek()
            if next_customer:
                print(f"Next Customer: {next_customer}")
            else:
                print("No customers in queue")


        elif choice == "4":
            # Print all customers in the queue
            print("\nWaiting customers:")
            help_desk_queue.print_queue()
            

        elif choice == "5":
            print("Exiting Help Desk System.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_help_desk()

'''For our undo/redo program, a stack is the right choice for this type of scenario because of the
Last-In, First-Out order of operations. In our Undo/Redo program we are looking to undo our most recent
action, as well as redo our most recent action in the undo stack. In other words, we want to have our last
action be the first thing undone and the last thing undone to be the first thing redone. This fits the
usage of a stack perfectly as we are looking to go back through our most recent actions and reverse the
most recent one. For our Help Desk Queue program we are looking to create a list where new customers are 
added to the back and the customers at the front of the queue are taken care of first. In our prgorm this
means putting new entries at the back of the queue and taking out the first entry in the queue when we are
finished with it. This fits a queue well because of the First-In, First-Out order of operations. A queue also
works here because we are handling requests in the order they arrive, when customers request help, and fairness
 and timing matter, first customer to request help, gets helped. The main difference between my implementations
 of Stacks and Queues compared to Lists is that the Lists are more for general purpose storage where Queues and Stacks 
>>>>>>> f327fd7c4be830f643ae11949d72355b174ae834
 are more built to have more precise control over memory and order.'''