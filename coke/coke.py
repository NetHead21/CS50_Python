COKE_PRICE = 50  # Price in cents
ACCEPTED_COINS = [25, 10, 5]  # Quarter, dime, nickel

def get_valid_coin_input() -> int:
    """Get and validate coin input from user."""
    while True:
        try:
            coin_input = input("Insert Coin: ").strip()
            coin_value = int(coin_input)
            
            if coin_value in ACCEPTED_COINS:
                return coin_value
            else:
                print(f"Invalid coin. Only accepts: {', '.join(map(str, ACCEPTED_COINS))} cents")
                
        except ValueError:
            print("Please enter a valid number")


def vending_machine():
    """Simulate a Coke vending machine that accepts coins and gives change."""
    amount_due = COKE_PRICE
    print(f"Amount Due: {amount_due}")

    while amount_due > 0:
        coin = get_valid_coin_input()
        
        if coin >= amount_due:
            # Customer paid exact amount or overpaid
            change = coin - amount_due
            if change > 0:
                print(f"Change Owed: {change}")
            amount_due = 0
        else:
            # Customer needs to pay more
            amount_due -= coin
            print(f"Amount Due: {amount_due}")
    
    print("Thank you!")

def main():
    """Main function to run the vending machine."""
    try:
        vending_machine()
    except KeyboardInterrupt:
        print("\nOperation cancelled.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
