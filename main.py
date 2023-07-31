import fileinput
import json


class CapitalGains:
    def __init__(self):
        self.weighted_avg_price = 0
        self.qty = 0
        self.tax_rate = .2
        self.tax_threshold = 20_000
        self.profit = 0

    def calc_tax(self, entry):
        type, price, qty = entry['operation'], entry['unit-cost'], entry['quantity']

        if type == 'buy':
            if self.qty:
                self.weighted_avg_price = (self.qty * self.weighted_avg_price + qty * price) / (self.qty + qty)
            else:
                self.weighted_avg_price = price
            self.qty += qty
            return 0
        else:
            self.profit += (price - self.weighted_avg_price) * qty
            self.qty -= qty
            if price * qty <= self.tax_threshold or self.profit <= 0:
                tax = 0
            else:
                tax = self.profit * self.tax_rate
            self.profit = min(self.profit, 0)
            return tax

    def get_taxes(self, line):
        events = json.loads('{"data": ' + line + '}')['data']
        taxes = [self.calc_tax(e) for e in events]
        s = ','.join(f'{{"tax": {t:.2f}}}' for t in taxes)

        return f'[{s}]'


if __name__ == '__main__':
    inp = fileinput.input()
    for line in inp:
        res = CapitalGains().get_taxes(line)
        print(res)
