from application.salary import calculate_salary as calc_salary
from application.db.people import get_employees
from datetime import datetime as dt

def main():
    print(dt.now().date(), '\n')
    calc_salary()
    get_employees()

if __name__ == '__main__':
    main()