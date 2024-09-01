totalflushed_day = 14 # 14 times per day
waters_toflush = 15 #liters 
new_waters_toflush = 2 # liters
newtoilet_cost = 150 # dollars

population = int(input("Enter the community population :"))

magnitude = 2 * totalflushed_day
water_saved = waters_toflush*totalflushed_day - new_waters_toflush*totalflushed_day
toilet_population_cost = newtoilet_cost * population
print("The magnitude is", magnitude, "flush per day per toilet and the cost to build new toilet for the community is", toilet_population_cost," dollars.")
print("The amount of water saved is", water_saved, "per day.")


