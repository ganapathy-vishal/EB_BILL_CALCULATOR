print("Enter The Details To Check Your Bill Amount")
Consumer_Name=input("Consumer Name:")
Tariff=input("Enter Tariff:")
Units=float(input("Units Consumed:"))
Subsidy=float(input("Enter the Subsidy amount:"))
Surcharge=(84)
if Units <= 100:
    Bill_amount = Units * 2.90

elif Units <= 200:
    Bill_amount = (100 * 2.90) + ((Units - 100) * 4.20)

elif Units <= 300:
    Bill_amount =(100 * 2.90) + (100 * 4.20) + ((Units - 200) * 6.20)

else:
    Bill_amount =(100 * 2.90) + (100 * 4.20) + (100 * 6.20) + ((Units - 300) * 7.70)

final_payable=(Bill_amount-Subsidy+Surcharge)
print("|||||EB PAYMENT CALCULATOR||||| ")
print("Consumer Name  :",Consumer_Name)
print("Units Consumed :",Units)

print(f"Total Amount   :₹{Bill_amount:.2f}")
print(f"Fixed Surcharge:₹{Surcharge}")
print(f"Subsidy        :₹{Subsidy:.2f}")
print(f"Final Payable  :₹{final_payable:.2f}")
