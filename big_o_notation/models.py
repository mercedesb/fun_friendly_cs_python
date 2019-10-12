from django.db import models

# Create your models here.

class Cupcakes:
  def __init__(self):
    self.recipe_ratios = {
      "butter": {"name": "butter", "number": 1, "measurement": "C."},
      "sugar": {"name": "sugar", "number": 2, "measurement": "C."},
      "eggs": {"name": "eggs", "number": 4, "measurement": ""},
      "flour": {"name": "flour", "number": 3, "measurement": "C."},
      "baking_powder": {"name": "baking powder", "number": 1, "measurement": "tbsp"},
      "milk": {"name": "mlk", "number": 1, "measurement": "C."},
    }

  # O(1)
  def preheat_oven(self, number_of_batches):
    return f"Preheating oven to 350 degrees to make {number_of_batches} batches of cupcakes: O(1)"

  # O(1)
  def combine_butter_and_sugar(self, number_of_batches):
    steps = []
    butter = {
      "ingredient": self.recipe_ratios["butter"],
      "amount": number_of_batches * self.recipe_ratios["butter"]["number"]
    }
    sugar = {
      "ingredient": self.recipe_ratios["sugar"],
      "amount": number_of_batches * self.recipe_ratios["sugar"]["number"]
    }

    steps.append(self.beat_with_electric_mixer([butter, sugar], 3))
    steps.append("Combine butter and sugar: O(1)")
    return "<br/>".join(steps)

  # O(n)
  def add_eggs(self, number_of_batches):
    steps = []
    one_egg = { "ingredient": self.recipe_ratios["eggs"], "amount": 1 }
    butter_mixture = { "ingredient": "butter mixture" }

    amount = number_of_batches * self.recipe_ratios["eggs"]["number"]
    for _ in range(amount):
      steps.append(self.beat_with_electric_mixer([one_egg, butter_mixture], 1))

    steps.append("Added eggs: O(n)")
    return "<br/>".join(steps)

  # O(1)
  def combine_flour_and_baking_powder(self, number_of_batches):
    steps = []
    flour = {
      "ingredient": self.recipe_ratios["flour"],
      "amount": number_of_batches * self.recipe_ratios["flour"]["number"]
    }
    baking_powder = {
      "ingredient": self.recipe_ratios["baking_powder"],
      "amount": number_of_batches * self.recipe_ratios["baking_powder"]["number"]
    }

    steps.append(self.stir_with_spoon([flour, baking_powder]))
    steps.append("Combined flour and baking powder: O(1)")
    return "<br/>".join(steps)

  # O(n^2)
  def combine_flour_mixture_and_milk_and_butter_mixture(self, number_of_batches):
    steps = []
    butter_mixture = { "ingredient": "butter mixture" }
    flour_mixture = { "ingredient": "flour mixture" }
    milk = {
      "ingredient": self.recipe_ratios["milk"],
      "amount":
        (number_of_batches * self.recipe_ratios["milk"]["number"]) / (number_of_batches * number_of_batches)
    }

    steps.append(self.beat_with_electric_mixer([butter_mixture, flour_mixture], 1))

    for _batch in range(number_of_batches):
      for _portion in range(number_of_batches):
        steps.append(self.beat_with_electric_mixer([butter_mixture, milk], 1))
        steps.append(self.beat_with_electric_mixer([butter_mixture, flour_mixture], 1))

    steps.append("Slowly combined milk, flour mixture, and butter mixture: O(n^2)")

    return "<br/>".join(steps)

  # O(1)
  def bake(self):
    return "Poured into muffin tins. Baked for 28-30 minutes: O(1)"

  # See private function calculate_fibonacci_number: O(2^n)
  def fibonacci_frosting(self, number_of_batches):
    number_to_frost = self.calculate_fibonacci_number(number_of_batches)
    return f"Iced the fibonacci number {number_to_frost} to all of the cupcakes: O(2^n) (check out the console for the process)"

  def beat_with_electric_mixer(self, components, time_in_minutes):
    component_text = ", ".join(map(self.get_ingredient_text, components))
    return f"Beating {component_text} with mixer at medium speed for {time_in_minutes} minutes"

  def stir_with_spoon(self, components):
    component_text = ", ".join(map(self.get_ingredient_text, components))
    return f"Stirring {component_text} with spoon"

  def get_ingredient_text(self, component):
    text = ""
    if component.get("amount"):
      text += f"{component['amount']} "

    ingredient = component.get("ingredient", {})
    if isinstance(ingredient, dict) and ingredient.get("measurement"):
        text += f"{ingredient['measurement']} "
    elif isinstance(ingredient, dict) and ingredient.get("name"):
        text += f"{ingredient['name']} "
    else:
        text += f"{ingredient}"

    return text

  # O(2^n)
  def calculate_fibonacci_number(self, number):
    if number <= 1:
      print("Fibonacci base case!")
      return number
    else:
      print(f"Adding fibonacci numbers {number} and {number - 1}")
      return self.calculate_fibonacci_number(number - 1) + self.calculate_fibonacci_number(number - 2)
