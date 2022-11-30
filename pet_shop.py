def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, amount):
    pet_shop["admin"]["pets_sold"] += amount

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, pet_breed):
    found_breed = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == pet_breed:
            found_breed.append(pet)
    return found_breed

def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet

def remove_pet_by_name(pet_shop, pet_name):
    pet_to_remove = find_pet_by_name(pet_shop, pet_name)
    pet_shop["pets"].remove(pet_to_remove)

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, amount):
    customer["cash"] -= amount

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

def customer_can_afford_pet(customer, new_pet):
    if customer["cash"] >= new_pet["price"]:
        return True
    return False








# # WRITE YOUR FUNCTIONS HERE
# def get_pet_shop_name(pet_shop):
#     return pet_shop["name"]

# def get_total_cash(num):
#     return num["admin"]["total_cash"]

# def add_or_remove_cash(pet_shop, num):
#     pet_shop["admin"]["total_cash"] += num

# def get_pets_sold(total_number_sold):
#     return total_number_sold["admin"]["pets_sold"]

# def increase_pets_sold(pet_shop, num):
#     pet_shop["admin"]["pets_sold"] += 2

# def get_stock_count(pet_shop):
#     return len(pet_shop["pets"])

# def get_pets_by_breed(pet_shop, pet_breed):
#     named_breed = []
#     for pets in pet_shop["pets"]:
#         if pets["breed"] == pet_breed:
#             named_breed.append(pets)
#     return named_breed

# # def get_pets_by_breed(pet_shop, pet_breed):
# #     breed_not_found = []
# #     for pets in pet_shop["pets"]:
# #         if pet_breed == 0:
# #             breed_not_found.append(pets)
# #         return breed_not_found

# def find_pet_by_name(pet_shop, pet_name):
#     for pets in pet_shop["pets"]:
#         if pets["name"] == pet_name:
#             return pets
#     else:
#         return None

# # def find_pet_by_name(pet_shop, pet_name):
# #     for pets in pet_shop["pets"]:
# #         if pets["name"] == pet_name:
# #             return pets
# #         else:
# #             return None


# # Go through the dictionaries within the list. First you have to find the pet, then you have to remove it.
# def remove_pet_by_name(pet_shop, pet_name):
#     pet_to_remove = find_pet_by_name(pet_shop, pet_name)
#     pet_shop["pets"].remove(pet_to_remove)


# def add_pet_to_stock(pet_shop, new_pet):
#     pet_shop["pets"].append(new_pet)

# def get_customer_cash(num):
#     return num["cash"]

# def remove_customer_cash(customer, num):
#     customer["cash"] -= num

# def get_customer_pet_count(customer):
#     return len(customer["pets"])

# def add_pet_to_customer(customer, new_pet):
#     customer["pets"].append(new_pet)


# # For the customer_can_afford_pet function, you need to see if the cash held against a certain customer's name is greater than or equal to the price of the given pet.

