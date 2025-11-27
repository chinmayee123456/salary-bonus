import sys
if len(sys.argv)==2:
  script_name=sys.argv[0]
  salary=sys.argv[1]
  print("user provided input values:")
else:
  salary=90000
  print("no input given-using default values:")
  bonus = salary * 0.10
  total_salary = salary + bonus
  print("Bonus Amount:", bonus)
  print("Total Salary after adding bonus:", total_salary)

