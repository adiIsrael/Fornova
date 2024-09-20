# main.py

# Importing json and the class hotel_data_processor
import json
from hotel_data_processor import HotelDataProcessor

# Load the JSON data from the file (also it's common call it 'f' file is ok)
with open('Python-task.json', 'r') as file:
    data = json.load(file)


# Create an instance of the  class
processor = HotelDataProcessor(data)

# Find the cheapest room, price and  number of guests
cheapest_room, cheapest_price, number_of_guests = processor.get_cheapest_price()
print(f"Cheapest Room: {cheapest_room}, Price: {cheapest_price} , Number of guests: {number_of_guests}")

# Calculate the total prices for all rooms
total_prices = processor.calculate_total_prices()
print("Total Prices (Net Price + Taxes):")
for room_type, total_price in total_prices:
    print(f"{room_type}: {total_price}")

# Save the output to a file
processor.save_to_file('output.txt')
