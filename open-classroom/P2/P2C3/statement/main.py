# Write your code here!
def monthly_salary(annual_salary):
  return annual_salary / 12

def weekly_salary(monthly_salary):
   return monthly_salary / 4

def hourly_wage(weekly_salary, hours_worked):
   return weekly_salary / hours_worked

def main():
   annualy_salary = float(input("Add your annualy salary: "))
   weekly_hours_worked = float(input(" Provide hours you work per week: "))

   user_monthly_salary = monthly_salary(annualy_salary)
   user_weekly_salary = weekly_salary(user_monthly_salary)
   user_hourly_wage= hourly_wage(user_weekly_salary, weekly_hours_worked)

   print(f"Your hourly wage is {user_hourly_wage} dollars")

# Do not modify the code below
if __name__ == "__main__":
    main()