"""
Garrett Lail
sales_person.py
I certify this class is my own work
"""

class SalesPerson:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []
    def get_id(self):
        return self.employee_id
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def enter_sale(self, sale):
        self.sales.append(sale)
    def total_sales(self):
        total = 0
        for i in range(len(self.sales)):
            total += self.sales[i]
        return total
    def get_sales(self):
        return self.sales
    def met_quota(self, quota):
        if self.total_sales() == quota:
            return True
        else:
            return False
    def compare_to(self, other):
        if other.total_sales() > self.total_sales():
            return -1
        if other.total_sales() < self.total_sales():
            return 1
        if other.total_sales() == self.total_sales():
            return 0
    def __str__(self):
        return '{}-{}:{}'.format(self.employee_id, self.name, self.total_sales())
