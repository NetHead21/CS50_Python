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