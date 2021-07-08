def log_read(name):
    with open(f"{name}.txt") as f:
        return int(f.read())

def log_update(name,seatsAva):
    with open(f"{name}.txt","w") as f:
        f.write(str(seatsAva))    

print('''********************************************************************************
Hi! Welcome to Indian Railways!
********************************************************************************''')

class Train:
    def details(self,name):
        self.name = name
        self.seatsAva = log_read(self.name)

    def bookTicket(self):
        self.seatsAva=self.seatsAva-1
        log_update(self.name,self.seatsAva)

class Passeneger:
    name=input("Enter your name: \n")
    age=input("Enter your age: \n")
    gender=input("Enter your gender: \n")
    def __details__(self, name, age, gender):
        self.name = name
        self.age=age
        self.gender = gender
    def bookTicket(self):
        name=input("Enter Train Name: \n").lower()
        trin=Train()
        trin.details(name)
        if trin.seatsAva!=0:
            print(f'''
    ********************************************************************************
    A seat has been booked to 
    {self.name}
    Age:{self.age}
    Gender:{self.gender}
    Train Name: {trin.name}
    Seat number: {trin.seatsAva}
    ''')
            trin.bookTicket()
            print(f'''Seats Left: {trin.seatsAva}
    ********************************************************************************''')
        elif trin.seatsAva ==0:
            print('''********************************************************************************

Sorry, no seats available
Try in some other train.

********************************************************************************''')
while True:
    print('''
How may I help you?
''')
    command=input(">")
    command=command.lower()

    if command=="book a ticket":
        pas=Passeneger()
        pas.bookTicket()
    elif command == "exit":
        break    
    else:
        print("I don't understand that.")