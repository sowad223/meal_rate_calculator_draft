class MealRateCalculator:
    def __init__(self):
        self.persons = []

    def add_person(self, name, meal_count, given_money):
        person = {
            'name': name,
            'meal_count': float(meal_count),
            'given_money': float(given_money)
        }
        self.persons.append(person)

    def calculate(self, left_amount):
        total_meals = sum(person['meal_count'] for person in self.persons)
        total_money_given = sum(person['given_money'] for person in self.persons)

        if total_meals == 0:
            raise ValueError("Total meal count cannot be zero.")

        meal_rate = (total_money_given + left_amount) / total_meals

        results = []
        for person in self.persons:
            amount_spent = person['meal_count'] * meal_rate
            money_diff = person['given_money'] - amount_spent
            results.append({
                'name': person['name'],
                'meal_count': person['meal_count'],
                'given_money': person['given_money'],
                'amount_spent': amount_spent,
                'money_diff': money_diff
            })

        return meal_rate, results
