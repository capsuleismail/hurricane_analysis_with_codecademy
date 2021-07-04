weight = 60
#flat_charge
flat_charge_gsp = 125.00
flat_charge_gs = 20
flat_charge_d = 0
#ground_shipping
if weight <= 2:
  cost_ground = weight * 1.5 + flat_charge_gs
  print(cost_ground)
elif weight > 2 and weight <= 6:
  cost_ground = weight * 3.00 + flat_charge_gs
  print(cost_ground)
elif weight > 6 and weight <= 10:
  cost_ground = weight * 4.00 + flat_charge_gs
  print(cost_ground)
elif weight > 10:
  cost_ground = weight * 4.75 + flat_charge_gs
  print(cost_ground)

weight = 8.4
price = 4.00
cost_ground = weight * price + flat_charge_gs
print(cost_ground)
#premium_shipping
cost_premium = flat_charge_gsp
print(cost_premium)
#drone_shipping

if weight <= 2:
  cost_drone = weight * 4.5 + flat_charge_gs
  print(cost_ground)
elif weight > 2 and weight <= 6:
  cost_drone = weight * 9.00 + flat_charge_gs
  print(cost_ground)
elif weight > 6 and weight <= 10:
  cost_drone = weight * 12.00 + flat_charge_gs
  print(cost_ground)
elif weight > 10:
  cost_drone = weight * 14.25 + flat_charge_gs

weight = 1.5
price = 4.50
flat_charge_d = 0

cost_drone = weight * price + flat_charge_d 
print(cost_drone)
