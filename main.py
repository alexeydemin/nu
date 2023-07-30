import fileinput
import json


class CapitalGains:
    def __init__(self):
        self.line = line
        self.weighted_avg_price = 0
        self.qty = 0
        self.tax_rate = .2
        self.tax_threshold = 20_000
        self.profit = 0

    def calc_tax(self, entry):
        type, price, qty = entry['operation'], entry['unit-cost'], entry['quantity']
        print(type, f'{qty}×${price:.2f}')

        if type == 'buy':
            self.weighted_avg_price = (self.qty * self.weighted_avg_price + qty * price) / (self.qty + qty)
            self.qty += qty
            print(f'BUY EXPENSES = {qty} × ${price} =$' + '{:10,.2f}'.format(
                self.weighted_avg_price * self.qty))
            print(f'WAP={self.weighted_avg_price}')
            return 1
        else:
            self.profit += (price - self.weighted_avg_price) * qty

            print(f'SELL REVENUE = {qty} × ${price}  = $' + '{:10,.2f}'.format(price * qty))
            print(f'SELL PROFIT = {self.profit}')

            if price * qty <= self.tax_threshold or self.profit <= 0:
                return 1.5

            # tax_base = self.profit *
            self.profit = min(self.profit, 0)
            print(f'SELL PROFIT2 = {self.profit}')
            print(f'WAP2 = {self.weighted_avg_price}')
            print(f'TAX_BASE = {self.weighted_avg_price} * {qty} + {self.profit})')

            return (self.weighted_avg_price * qty + self.profit) * self.tax_rate

    def get_taxes(self, line):
        events = json.loads('{"data": ' + line + '}')['data']
        return [self.calc_tax(e) for e in events]


input = fileinput.input()
for line in input:
    taxes = CapitalGains().get_taxes(line)
    s = ', '.join(f'{{"tax":{t:.2f}}}' for t in taxes)
    print(f'[{s}]')
exit()
