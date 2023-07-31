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
                self.weighted_avg_price = round((self.qty * self.weighted_avg_price + qty * price) / (self.qty + qty), 2)
            else:
                self.weighted_avg_price = price
            self.qty += qty
            return 0
        else:
            profit = (price - self.weighted_avg_price) * qty

            if price * qty <= self.tax_threshold:
                tax = 0
                if profit < 0:
                    self.profit += profit
            elif self.profit + profit <= 0:
                tax = 0
                self.profit += profit
            else:
                tax = (self.profit + profit) * self.tax_rate
                self.profit = min(0, self.profit + profit)
            self.qty -= qty
            return tax

    def get_taxes(self, line):
        events = json.loads(line)
        taxes = [self.calc_tax(e) for e in events]
        return json.dumps([{"tax": '{0:.2f}'.format(t)} for t in taxes])


if __name__ == '__main__':
    inp = fileinput.input()
    for line in inp:
        res = CapitalGains().get_taxes(line)
        print(res)
