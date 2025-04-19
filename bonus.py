import random



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
    trackingId = generateTrackingId(name)

    order = {
        "trackingId": trackingId,
        "name": name,
        "address": address,
        "product": product,
        "status": "Pending",
        "route": None
    }

    orders.append(order)

#####
### generateTrackingId
def generateTrackingId(name):
    prefix = name[:3].upper()
    number = random.randint(100, 999)
    return prefix + str(number)

######
##### validateTrackingId(trackingId)
def validateTrackingId(trackingId):
    if len(trackingId) == 6 and trackingId.isalnum():
        return True
    else:
        newId = input("Invalid ID. Enter a valid 6-character alphanumeric tracking ID: ")
        return validateTrackingId(newId)

### 
### assignRoute(address)
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
def dispatchOrders(orders):
    for order in orders:
        route = assignRoute(order["address"])
        order["route"] = route
        order["status"] = "Dispatched"

#########
##### trackOrder(orders, trackingId)
def trackOrder(orders, trackingId):
    for order in orders:
        if order["trackingId"] == trackingId:
            print("Status:", order["status"])
            return
    print("Order not found")


### 
### updateOrderStatus(orders, trackingId, newStatus)
def updateOrderStatus(orders, trackingId, newStatus):
    for order in orders:
        if order["trackingId"] == trackingId:
            order["status"] = newStatus
            print("Order status updated.")
            return
    print("Order not found")

###
### printOrderSummary(orders)
def printOrderSummary(orders):
    print("Tracking ID | Name | Product | Status")
    for order in orders:
        print(order["trackingId"], "|", order["name"], "|", order["product"], "|", order["status"])

## 
## searchOrdersByCustomer(orders, customerName)
def searchOrdersByCustomer(orders, customerName):
    for order in orders:
        if customerName.lower() in order["name"].lower():
            print(order)

###
#### calculateTotalOrders(orders)
def calculateTotalOrders(orders):
    return len(orders)

###
## groupOrdersByRoute(orders)
def groupOrdersByRoute(orders):
    routeGroups = {}

    for order in orders:
        route = order["route"]
        if route not in routeGroups:
            routeGroups[route] = []
        routeGroups[route].append(order["trackingId"])

    return routeGroups

###
## removeOrder(orders, trackingId)
def removeOrder(orders, trackingId):
    for order in orders:
        if order["trackingId"] == trackingId:
            orders.remove(order)
            print("Order removed.")
            return
    print("Order not found.")

##
### saveOrdersToFile(orders, filename)
def saveOrdersToFile(orders, filename):
    with open(filename, "w") as file:
        for order in orders:
            line = f'{order["trackingId"]}, {order["name"]}, {order["product"]}, {order["status"]}\n'
            file.write(line)
    print("Orders saved.")

###
## loadOrdersFromFile(filename)
def loadOrdersFromFile(filename):
    newOrders = []

    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(", ")
            if len(parts) == 4:
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

# --- Main function (goes at the end) ---
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

# --- Entry point to start the program ---
if __name__ == "__main__":
    main()