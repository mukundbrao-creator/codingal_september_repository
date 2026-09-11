def total_calc(bill_amount, tip_perc):
    """Use this to define how the to calculate the total amount of money that must be paid."""
    total = bill_amount * ( 1 * 0.01 * tip_perc)
    total = round(total, 2)
    print(f"Please pay ${total}.")

total_calc(150, 20)

