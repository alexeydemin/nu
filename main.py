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
        # print(type, f'{qty}×${price:.2f}')

        if type == 'buy':
            self.weighted_avg_price = (self.qty * self.weighted_avg_price + qty * price) / (self.qty + qty) if self.qty else price
            self.qty += qty
            # print(f'BUY EXPENSES = {qty} × ${price} =$' + '{:10,.2f}'.format(self.weighted_avg_price * self.qty))
            # print(f'WAP={self.weighted_avg_price}')
            # print(f'SELL PROFIT_B = {self.profit}')
            # print()
            return 0
        else:
            self.profit += (price - self.weighted_avg_price) * qty

            # print(f'SELL REVENUE = {qty} × ${price}  = ' + '${:10,.2f}'.format(price * qty))
            # print(f'SELL PROFIT = {self.profit}')

            if price * qty <= self.tax_threshold or self.profit <= 0:
                # print('WE ARE HERE')
                self.qty -= qty
                # print(f'SELL PROFIT_BEFORE = {self.profit}')
                self.profit = min(self.profit, 0)
                # print(f'SELL PROFIT* = {self.profit}')
                # print()
                return 0

            tax = self.profit * self.tax_rate
            self.profit = min(self.profit, 0)
            self.qty -= qty
            # print(f'SELL PROFIT2 = {self.profit}')
            # print(f'WAP2 = {self.weighted_avg_price}')
            # print(f'TAX = {tax}')
            # print()

            return tax

    def get_result(self, line):
        events = json.loads('{"data": ' + line + '}')['data']
        taxes = [self.calc_tax(e) for e in events]
        s = ','.join(f'{{"tax": {t:.2f}}}' for t in taxes)

        return f'[{s}]'


if __name__ == '__main__':
    inp = fileinput.input()
    for line in inp:
        res = CapitalGains().get_result(line)
        print(res)
