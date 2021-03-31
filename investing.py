# This function calculates how much $ you'll have in X years, if you invest weekly.

# How much are you investing per week?
weekly_in = 100
# How many years do you plan on investing for?
num_years = 10
# Compound Annual Growth Rate (ROI %)
cagr = 15

def investing(weekly_in, num_years, cagr):
  cagr = (100+cagr)/100
  yearly_in = weekly_in*(365/7)
  start = yearly_in*cagr

  for i in range(num_years+1):
    if i > 1:
      next = (start + yearly_in)*cagr
      start = next
      if i == num_years:
        savings = "%.2f" % round(next,2)
        print('You will have',savings,'if you invest',weekly_in,'/week for %s years.'%i)

investing(weekly_in, num_years, cagr)
