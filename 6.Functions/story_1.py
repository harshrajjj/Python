def print_order(name, chai_type):
    print(f"{name} ordered a {chai_type} chai.")



# print_order("aman", "masala")
# print_order("sara", "ginger")
# print_order("john", "cardamom")


def fetch_sales():
    print("Fetching sales data...")

def filter_valid_sales():
    print("Filtering valid sales...")


def summerize_sales():
    print("Summarizing sales...")   

def generate_report():
    fetch_sales()
    filter_valid_sales()
    summerize_sales()
    print("Generating report...")


generate_report()