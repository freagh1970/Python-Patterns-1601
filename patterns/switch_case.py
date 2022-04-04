class Switcher(object):
    def numbers_to_months(self, argument):
        """Dispatch method"""
        method_name = 'month_' + str(argument)
        print(method_name)
        # Get the method from 'self'. Default to a lambda.
        method = getattr(self, method_name, lambda: "Invalid month")
        # Call the method as we return it
        return method()

    def month_1(self):
        return "January"

    def month_2(self):
        return "February"

    def month_3(self):
        return "March"


print(a.numbers_to_months(2))

a = Switcher()
b = Switcher()
# Changes made

