while True:
    TicketType=input("input the ticket type(E  or S): ")
    BaggageWeight= int(input("input the baggage weight: "))
    if TicketType=="E" or TicketType =="S":
        break
if TicketType=="E":
    BaggageAllowance=16
    ChargeRate=3.5
elif TicketType == "S":
    BaggageAllowance = 20
    ChargeRate=5.75
ExcessWeight = BaggageWeight-BaggageAllowance
if ExcessWeight >0:
    Charge=ExcessWeight * ChargeRate
else:
    Charge = 0

print(Charge)
