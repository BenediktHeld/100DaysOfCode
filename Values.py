def test(baseSalary, **values):
    print(f"Base Salary: {baseSalary}")
    print(f"Level 2: {baseSalary * values['Level2']}")
    print(f"Level 3: {baseSalary * values['Level3']}")
    print(f"Level 4: {baseSalary * values['Level4']}")

test(4000, Level2=1.2, Level3=1.6, Level4=2.2)
