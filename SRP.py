class Invoice:
    def __init__(self, items):
        self.items = items

class InvoiceCalculator:
    @staticmethod
    def calculate_total(invoice):
        return sum(item['price'] * item['quantity'] for item in invoice.items)

class InvoicePrinter:
    @staticmethod
    def print_invoice(invoice, total):
        print("Invoice")
        for item in invoice.items:
            print(f"{item['name']} - {item['quantity']} x {item['price']}")
        print(f"Total: {total}")

class InvoiceRepository:
    @staticmethod
    def save(invoice):
        print("Saving invoice to database...")

class InvoiceEmailSender:
    @staticmethod
    def send(invoice):
        print("Sending invoice email...")

invoice = Invoice([
    {'name': 'Apple', 'price': 2, 'quantity': 5},
    {'name': 'Banana', 'price': 1, 'quantity': 10}
])

# total = InvoiceCalculator.calculate_total(invoice)
# print(total)
# printing = InvoicePrinter.print_invoice(invoice, total)
print(invoice.items)