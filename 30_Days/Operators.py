# Given meal base cost,tip percentage , tax add the total and return it from a function

def solve(meal_cost: float, tip_percent: int, tax_percent : int):
    tip_cost = meal_cost*(tip_percent/100)
    tax = meal_cost *( tax_percent/100)
    total_price = tip_cost + tax+ meal_cost
    print(round(total_price))



meal_cost = float(input().strip())

tip_percent = int(input().strip())

tax_percent = int(input().strip())

solve(meal_cost, tip_percent, tax_percent)