def get_invoice_items(items):
    # Items is a dictionary with a quantity and price key, and a name key
    # Return a list of all the invoice line items in the following format:
    # quantity name subtotal currency
    # For example, if we had the following:
    # [
    #   {'name': 'Apple', 'quantity': 1, price: 0.2 },
    #   {'name': 'Orange', 'quantity': 4, price: 0.3 },
    # ]
    # We should return the following:
    # ['1 Apple 0.200KD', '4 Orange 1.200KD']
    # ---
    # Write your code here
    # ...
    invoice_items = []
    for item in items:
        invoice_items.append("{} {} {:.3f}KD".format(item['quantity'], item['name'], (item['price']*item['quantity'])))
    return invoice_items

def get_total(items):
    # Items is a dictionary with a quantity and price key
    # Calculate the total of all items in the cart
    # Write your code here
    # ...
    total = 0
    for item in items:
        total += (item['price']*item['quantity'])
    return "{:.3f}".format(total)


def print_receipt(invoice_items, total):
    # invoice_items will be the list of formatted items received from
    # `get_invoice_items`, and total will be a float. Print out a nice receipt
    # displaying a title, all the invoice items on separate lines, and the
    # total at the end.
    # ---
    # Write your code here
    # ...
    print("\n-------------------\nreceipt\n-------------------")
    for item in invoice_items:
        # total += (item['price']*item['quantity'])
        print(item)
    print("-------------------\n Total Price: {}KD".format(total))

def main():
    # Write your main logic here
    # ...
    items = []
    while True:
        Item = input("Item (enter \"done\" when finished): ")
        if (Item.casefold() != "done"):
            while True:
                try:
                    Price = float(input("Price: "))
                    Quantity = int(input("Quantity: "))
                except:
                    print("inputs are invalid. try again.")
                else:
                    items.append({'name': Item, 'quantity': Quantity, 'price': Price })
                    break
        else:
            invoice_items = get_invoice_items(items)
            total = get_total(items)
            print_receipt(invoice_items, total)
            break


if __name__ == "__main__":
    main()
