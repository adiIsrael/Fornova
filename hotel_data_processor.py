import json


class HotelDataProcessor:
    def __init__(self, data):
        self.data = data
        print("Initializing HotelDataProcessor with data")

    def get_cheapest_price(self):
        # Extracting shown_prices in the data
        shown_prices = self.data['assignment_results'][0]['shown_price']
        room_iterator = iter(shown_prices)  # I put the iterator on shown prices , iter contains an object so far
        first_room = next(room_iterator)  # I initialize first_room with  the first key "Hearing Accessible/Non-Smoking"
        cheapest_price = float(shown_prices[first_room])  # Accessing the value + Convert the first price to a float
        cheapest_room = first_room

        # Compare other room prices to find the cheapest
        for room_type, price in shown_prices.items():
            price = float(price)
            if price < cheapest_price:
                cheapest_price = price
                cheapest_room = room_type

        number_of_guests = self.data['assignment_results'][0]['number_of_guests']

        return cheapest_room, cheapest_price, number_of_guests

    def calculate_total_prices(self):
        print("Begin calculating total prices ")
        taxes = json.loads(self.data['assignment_results'][0]['ext_data']['taxes'])
        print(f"Taxes data: {taxes}")

        # Calculating taxes
        sum_of_taxes = 0
        for summer in taxes.values():
            sum_of_taxes += float(summer)  # Convert each value to a float before adding
        print(f"Total taxes: {sum_of_taxes}")

        total_prices = []

        # Adding taxes with rooms prices, rounding 2 numbers after the . (Checked no data with more than 2 numbers)
        for room_type, net_price in self.data['assignment_results'][0]['net_price'].items():
            net_price = float(net_price)
            total_price = round(net_price + sum_of_taxes, 2)
            total_prices.append((room_type, total_price))
            print(f"Room: {room_type}, Net price: {net_price}, Total price: {total_price}")

        return total_prices

    def save_to_file(self, output_file):
        # Printing message + import  necessary data
        print("Printing data in a file")
        cheapest_room, cheapest_price, number_of_guests = self.get_cheapest_price()
        total_prices = self.calculate_total_prices()
        # Open a file, and writing what asked in the task (the "with" close the file , 'w' write mode )
        with open(output_file, 'w') as file:
            file.write(f"Cheapest Room: {cheapest_room}\n")
            file.write(f"Cheapest Price: {cheapest_price}\n")
            file.write(f"Number of Guests: {number_of_guests}\n")

            file.write("Total Prices (Net Price + Taxes):\n")
            # total_prices = [("King Studio Suite", 131.76), ("Queen Suite", 130.76)] is a list of tuples
            for room_type, total_price in total_prices:
                file.write(f"{room_type}: {total_price}\n")
        print(f"Data saved to {output_file}")
