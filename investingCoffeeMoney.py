# This function calculates how much $ you'll have in X years, if you invest your coffee money (save and invest weekly)

def investingCoffeeMoney(coffee_price, times_per_week, num_years, cagr):
  cagr_val = (100+cagr)/100
  yearly_spend = coffee_price*times_per_week*52
  start = yearly_spend*cagr_val

  for i in range(num_years+1):
    if i > 1:
      next = (start + yearly_spend)*cagr_val
      start = next
      if i == num_years:
        savings = round(next,2)
        print('You will have',savings,'if you invest your coffee $ for %s years.'%i)

# How much do you pay for a cup of coffee?
coffee_price = 2.50
# How many times per week do you buy coffee?
times_per_week = 5
# How many years can you go without buying coffee? :D
num_years = 5
# Compound Annual Growth Rate (ROI %)
cagr = 15

investingCoffeeMoney(coffee_price, times_per_week, num_years, cagr)
