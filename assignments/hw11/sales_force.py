"""
Garrett Lail
sales_force.py
I certify this class is my own work
"""
from sales_person import SalesPerson

class SalesForce:
    def __init__(self):
        self.sales_people = []
    def add_data(self, file_name):
        file = open(file_name, 'r')
        for line in file.readlines():
            self.sales_people.append(line.split(','))
        print(self.sales_people)

    def quota_report(self, quota):
        for person in self.sales_people:
            sales = person[2].split(' ')
            for sale in sales:
                person.enter_sale(sale)
            if person.total_sales >= quota:
                person.append(True)
            else:
                person.append(False)
        return self.sales_people

    def top_seller(self):
        pass

    def individual_sales(self, employee_id):
        for person in self.sales_people:
            if person[0] == employee_id:
                return person
        return None

    def get_sale_frequencies(self):
        pass