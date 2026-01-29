# Generator yield-> you save money and you don't want the result immediately lazy evaluation

def server_chai():
    yield "Cup 1: Masala Chai"
    yield "Cup 2: Ginger Chai"
    yield "Cup 3: Cardamom Chai"

stall= server_chai()

# for cup in stall:
    # print(cup)


def get_chai_list():
    return ["Cup1", "Cup2", "Cup3"]

# generator function

def get_chai_get():
    yield "Cup1"
    yield "Cup2"
    yield "Cup3"
chai_gen= get_chai_get()
# print(next(chai_gen))
# print(next(chai_gen))
# print(next(chai_gen))


# infinite generator

# stream, constant
def infinite_chai():
    count=1
    while True:
        yield f"Refil # {count}: Chai"
        count += 1
refil= infinite_chai()
user2= infinite_chai()
# for _ in range(5):
#     print(next(refil))
#
# for _ in range(6):
#     print(next(user2))


#/////////////////////

def chai_customer():
    # print("Welcome ! What chai would you like?")
    order = yield
    while True:
        # print(f'Preparing your {order}...')
        order = yield
stall= chai_customer()
next(stall)  # start the generator
stall.send("Masala Chai")
stall.send("Ginger Chai")


# ====================================================
def local_chai():
     yield "Masala Chai"
     yield "Ginger Chai"

def imported_chai():
    yield "Matcha"
    yield "Oolong"
def full_menu():
    yield from local_chai()
    yield from imported_chai()

for chai in full_menu():
    print(chai)

def chai_stall():
    try:
        while True:
            order = yield "waiting for order"
    except:
        print("order is done")



stall= chai_stall()
print(next(stall))
stall.close() # cleanup code
# yeild pause and resume function
#next() -> starts the generator and runs until the first yield
#send() -> sends a value to the generator and resumes execution until the next yield
#throw() -> raises an exception inside the generator at the point of the current yield
#close() -> terminates the generator and raises a GeneratorExit exception inside it