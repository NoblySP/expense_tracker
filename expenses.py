import itertools as it


class Expense:
    id_iter = it.count()

    def __init__(self, category, amount, date):
        # self.id = next(self.id_iter)
        self.category = category
        self.amount = amount
        self.date = date

    def __str__(self):
        # return f"{self.id} | {self.category} | {self.amount} | {self.date}"
        return f"{self.category} | {self.amount} | {self.date}"


