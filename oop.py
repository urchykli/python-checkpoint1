# #1: Define a Vehicle class with the following properties and methods: 
# - `vehicle_type` 
# - `wheel_count`
# - `name` 
# - `cost` 
# - `colors` 
# - `vehicle_brand` 
# - `mpg`, a 'dict', with the following properties:
#     - `city`
#     - `highway` 
#     - `combined` 
# - `get_vehicle_type` should return the `vehicle_type`
# - `get_vehicle_brand` should return the classes `vehicle_brand`
# - `get_vehicle_drive` if the `wheel_count` for that class is "no wheels!" then
#     it should return "no wheels send it back to the shop" otherwise it should
#     return "I have "  + self.wheel_count  + " wheel drive"
#
# Your Vehicle class should take one argument (a `dict`) with the above
# attributes. Define the properties on the class from the dict that is passed in.
class Vehicle: 
	def __init__(self, dict):
		vehicle_type = dict['vehicle_type']
		wheel_count = dict['wheel_count']
		name = dict['name']
		cost = dict['cost']
		colors = dict['colors']
		vehicle_brand = dict['vehicle_brand']
		mpg = dict['city', 'highway', 'combined']
		self.vehicle_type = vehicle_type
		self.wheel_count = wheel_count
		self.name = name
		self.cost = cost
		self.colors = colors
		self.vehicle_brand = vehicle_brand
		self.mpg = mpg
	def get_vehicle_type(self):
		return self.vehicle_type
	def get_vehicle_brand(self):
		return self.vehicle_brand
	def get_vehicle_drive(self):
		if self.wheel_count == 'no wheels!':
			return "no wheels send it back to the shop"
		else:
			return f"I have "  + {self.wheel_count}  + " wheel drive"


# #2: Create a Motorcycle class that inherits from the Vehicle class and has the
# following properties and methods:
# - property: `wheel_count` defaults to "no wheels!"
# - method: `pop_wheelie` if `wheel_count` is not equal to 2 then it should be False,
#       otherwise return "......pop!"



# #3: Define a Car class that inherits from the vehicle class with the following attributes and methods:
# - property: `wheel_count` defaults to 4
# - method: `can_drive` that should return 'Vrrooooom Vroooom'



# #4: Define a Truck class that inherits from the vehicle class with the following attributes and methods:
# - property: `wheel_count` defaults to "no wheels!"
# - method: `rev_engine` that should return 'revvvvvreeeev'



# Commit when you finish working on these questions!