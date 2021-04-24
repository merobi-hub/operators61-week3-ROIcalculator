from IPython.display import clear_output


class returnOnInvestment:
    def __init__(self):
        self.propertyInfo = {}
        self.expenses = {}
        self.income = {}
        self.purchaseCosts = {}
        self.m_cash_flow = int()
        self.m_expenses = int()
        self.tot_income = int()
        self.coc_ROI_round = float()
        self.tot_purchaseCosts = int()

    def start(self):
        """Start gathers expense and income info from the user for calculations, saving the data in
        self.expenses, self.propertyInfo, and self.purchaseCosts"""
        clear_output(wait=True)
        purchase = input(
            'Will you take out a mortgage on the property or pay cash? m/c')
        if purchase == 'm':
            clear_output(wait=True)
            homePrice = input('What will the price of the home be?')
            self.purchaseCosts['price'] = int(homePrice)
            downpayment = input('How much will you put down?')
            self.purchaseCosts['downpayment'] = int(downpayment)
            clear_output(wait=True)
            mortgagePayment = input(
                'What will the monthly mortgage payment be?')
            self.expenses['mortgagePayment'] = int(mortgagePayment)
            self.costOfBuying()

        elif purchase == 'c':
            clear_output(wait=True)
            purchasePrice = input('What will the price of the home be?')
            self.purchaseCosts['price'] = int(purchasePrice)
            self.propertyInfo['value'] = int(purchasePrice)
            self.costOfBuying()

    def costOfBuying(self):
        """This fun collects user info about upfront purchase costs"""
        clear_output(wait=True)
        closing = input(
            'How much do you expect to pay in closing costs? If n/a enter 0. To use the national average, press a.')
        if closing.lower() == 'a':
            self.purchaseCosts['closing'] = int(
                self.purchaseCosts['price']*.02)
        else:
            self.purchaseCosts['closing'] = int(closing)
        clear_output(wait=True)
        rehab = input(
            'Some repairs are often necessary after purchasing a property. What is the most you could spend on repairs? To use a typical amount, enter a.')
        if rehab.lower() == 'a':
            self.purchaseCosts['rehab'] = 5000
        else:
            self.purchaseCosts['rehab'] = int(rehab)
        clear_output(wait=True)
        misc = input(
            'Enter any other likely upfront costs. If none or unknown, enter 0.')
        self.purchaseCosts['misc'] = int(misc)
        self.tot_purchaseCosts = sum(self.purchaseCosts.values())
        self.monthlyIncome()

    def monthlyExpenses(self):
        """This fun collects info about monthly expenses"""
        clear_output(wait=True)
        averageExpenses = input(
            'To use a conservative estimate of expenses based on the rent you expect to collect each month, enter a. To itemize expenses, enter 0.')
        if averageExpenses.lower() == 'a':
            self.expenses['average'] = int(self.income['rent']*.15)
            self.monthlyCashFlow()
        else:
            self.expenses['average'] = int(averageExpenses)
            tax = input(
                "Now let's break down the monthly expenses. What do you expect to pay in monthly taxes? To use the national average enter a.")
            if tax.lower() == 'a':
                self.expenses['tax'] = int(
                    (self.purchaseCosts['price']*.01)/12)
            else:
                self.expenses['tax'] = int(tax)
            clear_output(wait=True)
            utilities = input(
                'What is the monthly cost of utilities not passed on to tenants? To use a conservate estiment, enter a.')
            if utilities.lower() == 'a':
                self.expenses['utilities'] = int(self.income['rent']*.1)
            else:
                self.expenses['utilities'] = int(utilities)
            clear_output(wait=True)
            hoa = input('HOA fee (if none enter 0): ')
            self.expenses['hoa'] = int(hoa)
            clear_output(wait=True)
            lawn_snow = input(
                'Lawn or snow maintenance expenses. To use a conservative estimate, enter a: ')
            if lawn_snow.lower() == 'a':
                self.expenses['lawn_snow'] = 75
            else:
                self.expenses['lawn_snow'] = int(lawn_snow)
            clear_output(wait=True)
            vacancy = input(
                'Vacancy savings (to use a typical amount, enter a): ')
            if vacancy.lower() == 'a':
                self.expenses['vacancy'] = int(self.income['rent']*.05)
            else:
                self.expenses['vacancy'] = int(vacancy)
            clear_output(wait=True)
            repairs = input(
                'Expected monthly repair costs (to use a typical amount, enter a): ')
            if repairs.lower() == 'a':
                self.expenses['repairs'] = 100
            else:
                self.expenses['repairs'] = int(repairs)
            clear_output(wait=True)
            capex = input('CapEx savings (to use a typical amount, enter a): ')
            if capex.lower() == 'a':
                self.expenses['capex'] = 100
            else:
                self.expenses['capex'] = int(capex)
            clear_output(wait=True)
            mngt = input(
                'Property management expenses (to use a typical amount, enter a): ')
            if mngt.lower() == 'a':
                self.expenses['mngt'] = int(self.income['rent']*.1)
            else:
                self.expenses['mngt'] = int(mngt)
            self.monthlyCashFlow()

    def monthlyIncome(self):
        """This fun collects data concerning monthly cash flow"""
        clear_output(wait=True)
        rent = input(
            "Now let's break down the income. What is the expected monthly rental income from the property?")
        self.income['rent'] = int(rent)
        clear_output(wait=True)
        other_rent = input(
            'What do expect to collect from storage units, laundry, etc.?')
        self.income['other'] = int(other_rent)
        self.tot_income = sum(self.income.values())
        self.monthlyExpenses()

    def monthlyCashFlow(self):
        """This fun calculates and outputs the monthly cash flow (income minus expenses)"""
        #clear_output(wait=True)
        print('Now that we know the monthly income and expenses, we can estimate the cash flow.')
        if self.expenses['average'] != 0:
            self.m_expenses = sum(self.expenses.values())
        else:
            self.m_expenses = sum(self.expenses.values()) - \
                self.expenses['average']
        self.m_cash_flow = sum(self.income.values()) - self.m_expenses
        print(f'Monthly cash flow from the property: ${self.m_cash_flow}.')
        self.cashOnCashROI()

    def cashOnCashROI(self):
        """Calculates CoC (dividing annual cash flow by total investment) and returns a rounded percentage"""
        #clear_output(wait=True)
        print('Now that we know your cash flow, we can calculate the annual ROI.')
        tot_purchaseCosts = sum(self.purchaseCosts.values())
        coc_ROI = ((self.m_cash_flow * 12) /
                   ((self.m_expenses * 12) + tot_purchaseCosts)) * 100
        self.coc_ROI_round = "%.2f" % round(coc_ROI, 2)
        #clear_output(wait=True)
        print(f'Your estimated Cash on Cash ROI is: {self.coc_ROI_round}%.')
        rec_check = input(
            'Would you like an itemized estimate including all your data? y/n')
        if rec_check.lower() == 'y':
            self.receipt()
        else:
            print('Thank you.')

    def receipt(self):
        """Outputs collected data and calculations"""
        clear_output(wait=True)
        print("="*71)
        print(f"Here's an overview of your property income, expenses, and ROI estimate:")
        print("="*71)
        print('Monthly expenses:')
        for k, v in self.expenses.items():
            print(f'${v}')
        print(f'Total: ${self.m_expenses}')
        print('Purchase Costs:')
        for k, v in self.purchaseCosts.items():
            print(f'${v}')
        print(f'Total: ${self.tot_purchaseCosts}')
        print('Monthly Income:')
        for k, v in self.income.items():
            print(f'${v}')
        print(f'Total: ${self.tot_income}')
        print(f'Your estimated Cash on Cash ROI is: {self.coc_ROI_round}%.')
        print("="*71)


def run():
    calculator = returnOnInvestment()
    while True:
        response = input(
            'Welcome to the Easy Street Real Estate ROI Calculator. Enter all amounts in whole numbers only. Press the s key to continue.')
        if response.lower() == 's':
            calculator.start()


run()
