import random
import json
import os


##############
#### display menu
def displayMenu():
    # Show the main menu options
    print("Main Menu:")
    print("1. Place Order")
    print("2. View Orders")
    print("3. Dispatch Orders")
    print("4. Track Order")
    print("5. Update Order")
    print("6. Search Customer")
    print("7. Total Orders")
    print("8. Group by Route")
    print("9. Remove Order")
    print("10. Save Orders")
    print("11. Load Orders")
    print("12. Exit")

    ######
    #### addOrder
def addOrder(orders, customerData):
    name = input("Enter customer name: ")
    address = input("Enter address: ")
    product = input("Enter product: ")
    trackingId = generateTrackingId(name) # Generate a unique tracking ID
# Creates a dictionary called order
    order = {
        "trackingId": trackingId,
        "name": name,
        "address": address,
        "product": product,
        "status": "Pending",
        "route": None
    }
# adds the newly created order dictionary to the orders list.
    orders.append(order)

#####
### generateTrackingId
## Generates a unique tracking ID based on the customer's name
## and a random number.
def generateTrackingId(name):
    prefix = name[:3].upper() # Takes the first 3 letters of the name and converts them to uppercase
    number = random.randint(100, 999) # Generates a random number between 100 and 999
    return prefix + str(number) # Concatenates the prefix and number to create a unique tracking ID

######
##### validateTrackingId(trackingId)
def validateTrackingId(trackingId):
    if len(trackingId) == 6 and trackingId.isalnum(): # Check if the ID is 6 characters long and alphanumeric
        return True # If the ID is valid, the function returns True and stops running.
    else:
        newId = input("Invalid ID. Enter a valid 6-character alphanumeric tracking ID: ") #It asks the user to enter a new tracking ID.
        return validateTrackingId(newId) # The function calls itself with the new ID to check if it's valid.

### 
### assignRoute(address)
# Assigns a route based on the address provided
def assignRoute(address):
    if "North" in address:
        return "Route A"
    elif "South" in address:
        return "Route B"
    elif "East" in address:
        return "Route C"
    elif "West" in address:
        return "Route D"
    else:
        return "Route X"

###
### dispatchOrders(orders)
# Dispatches orders by assigning routes and updating status
# This function iterates through each order in the orders list.
# For each order, it assigns a route based on the address using the assignRoute function.
def dispatchOrders(orders):
    for order in orders:
        route = assignRoute(order["address"])
        order["route"] = route
        order["status"] = "Dispatched" # Updates the order status to "Dispatched"

#########
##### trackOrder(orders, trackingId)
# Tracks an order by its tracking ID
# This function iterates through each order in the orders list.
def trackOrder(orders, trackingId):
    for order in orders:
        if order["trackingId"] == trackingId: # Checks if the tracking ID matches
            print("Status:", order["status"])
            return # If a match is found, it prints the status of the order.
    print("Order not found")


### 
### updateOrderStatus(orders, trackingId, newStatus)
# Updates the status of an order by its tracking ID
def updateOrderStatus(orders, trackingId, newStatus):
    for order in orders:
        if order["trackingId"] == trackingId: # Checks if the tracking ID matches
            order["status"] = newStatus # Updates the status of the order
            print("Order status updated.") # If a match is found, it updates the status and prints a confirmation message.
            return
    print("Order not found") # If no match is found, it prints an error message.

###
### printOrderSummary(orders)
# Prints a summary of all orders
# This function iterates through each order in the orders list.
# For each order, it prints the tracking ID, name, product, and status.
def printOrderSummary(orders):
    print("Tracking ID | Name | Product | Status")
    for order in orders:
        print(order["trackingId"], "|", order["name"], "|", order["product"], "|", order["status"])

## 
## searchOrdersByCustomer(orders, customerName)
# Searches for orders by customer name
def searchOrdersByCustomer(orders, customerName):
    for order in orders:
        if customerName.lower() in order["name"].lower(): # Checks if the customer name matches
            print(order)

###
#### calculateTotalOrders(orders)
# Calculates the total number of orders
def calculateTotalOrders(orders):
    return len(orders) # Returns the length of the orders list, which represents the total number of orders.

###
## groupOrdersByRoute(orders)
# Groups orders by their assigned routes
def groupOrdersByRoute(orders):
    routeGroups = {} # Initializes an empty dictionary to store route groups

    for order in orders:
        route = order["route"] # Gets the route of the order
        if route not in routeGroups: # Checks if the route is already in the dictionary
            routeGroups[route] = [] # If not, it creates a new list for that route
        routeGroups[route].append(order["trackingId"]) # Adds the tracking ID to the list for that route

    return routeGroups

###
## removeOrder(orders, trackingId)
# Removes an order by its tracking ID
def removeOrder(orders, trackingId):
    for order in orders:
        if order["trackingId"] == trackingId: # Checks if the tracking ID matches
            orders.remove(order) # Removes the order from the list
            print("Order removed.") # If a match is found, it removes the order and prints a confirmation message.
            return
    print("Order not found.") # If no match is found, it prints an error message.

##
### saveOrdersToFile(orders, filename)
# Saves orders to a file
def saveOrdersToFile(orders, filename):
    with open(filename, "w") as file: # Opens the file in write mode
        for order in orders: # Iterates through each order in the orders list
            line = f'{order["trackingId"]}, {order["name"]}, {order["product"]}, {order["status"]}\n'
            file.write(line) # Writes the order details to the file
    print("Orders saved.")

###
## loadOrdersFromFile(filename)
# Loads orders from a file
def loadOrdersFromFile(filename):
    newOrders = [] # Initializes an empty list to store loaded orders

    with open(filename, "r") as file: # Opens the file in read mode
        for line in file:
            parts = line.strip().split(", ") # Splits the line into parts based on commas
            if len(parts) == 4: # Checks if there are exactly 4 parts
                # Creates a dictionary for the order with the loaded details
                order = {
                    "trackingId": parts[0],
                    "name": parts[1],
                    "product": parts[2],
                    "status": parts[3],
                    "address": "",
                    "route": None
                }
                newOrders.append(order)

    return newOrders

# --- Main function to run the program ---
# This function will be called when the program is run.
def main():
    orders = []
    customerData = {}

    while True:
        displayMenu()
        choice = input("Select an option (1-12): ").strip()

        if choice == "1":
            addOrder(orders, customerData)
        elif choice == "2":
            printOrderSummary(orders)
        elif choice == "3":
            dispatchOrders(orders)
        elif choice == "4":
            trackingId = input("Enter tracking ID: ")
            if validateTrackingId(trackingId):
                trackOrder(orders, trackingId)
        elif choice == "5":
            trackingId = input("Enter tracking ID: ")
            if validateTrackingId(trackingId):
                newStatus = input("Enter new status: ")
                updateOrderStatus(orders, trackingId, newStatus)
        elif choice == "6":
            name = input("Enter customer name: ")
            searchOrdersByCustomer(orders, name)
        elif choice == "7":
            print("Total Orders:", calculateTotalOrders(orders))
        elif choice == "8":
            groups = groupOrdersByRoute(orders)
            for route, ids in groups.items():
                print(f"{route}: {', '.join(ids)}")
        elif choice == "9":
            trackingId = input("Enter tracking ID to remove: ")
            removeOrder(orders, trackingId)
        elif choice == "10":
            filename = input("Enter filename to save orders: ")
            saveOrdersToFile(orders, filename)
        elif choice == "11":
            filename = input("Enter filename to load orders from: ")
            orders = loadOrdersFromFile(filename)
        elif choice == "12":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

# --- Entry point to start the program, This checks: “Is this file being run directly by the user?” ---
# If it is, then it will call the main function to start the program.
if __name__ == "__main__":
    main()