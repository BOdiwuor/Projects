#In this project, you’ll build a program that will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.

#Write a shipping.py Python program that asks the user for the weight of their package and then tells them which method of shipping is cheapest and how much it will cost to ship their package using Sal’s Shippers.

weight = 41.5

drone_weight = 41.5

flat_charge = 20

ground_shipping_premium_cost = 125

if weight <=2:
   cost = weight * 1.50 + flat_charge
elif weight >2 and weight <=6:
   cost = weight * 3.00 + flat_charge
elif weight >6 and weight <=10:
   cost = weight * 4.00 + flat_charge
else:
   cost = weight * 4.75 + flat_charge
print ( "Ground Shipping Cost is", ":", "$", cost)

print("Ground Shipping Premium Cost is",":", "$", ground_shipping_premium_cost)

#Drone Shipping

if drone_weight <=2:
   cost = drone_weight * 4.50
elif drone_weight >2 and drone_weight <=6:
   cost = drone_weight * 9.00
elif drone_weight >6 and drone_weight <=10:
   cost = drone_weight * 12.00
else:
   cost = drone_weight * 14.25
print ( "Drone Shipping Cost is", ":", "$", cost)

#Cheapest method to ship a 4.8 pound package is via Ground Shipping
#Cheapest method to ship a 41.5 pound package is via Ground Shipping Premium
