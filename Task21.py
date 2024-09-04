def cm_to_ft(cm):
    return cm / 30.48

def km_to_miles(km):
    return km * 0.621371

def usd_to_inr(usd):
    return usd * 82.5  # Assume 1 USD = 82.5 INR

while True:
    print("\nMenu:")
    print("1. cm to ft")
    print("2. km to miles")
    print("3. USD to INR")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        cm = float(input("Enter length in cm: "))
        print(f"{cm} cm = {cm_to_ft(cm):.2f} ft")
    elif choice == 2:
        km = float(input("Enter distance in km: "))
        print(f"{km} km = {km_to_miles(km):.2f} miles")
    elif choice == 3:
        usd = float(input("Enter amount in USD: "))
        print(f"{usd} USD = {usd_to_inr(usd):.2f} INR")
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
