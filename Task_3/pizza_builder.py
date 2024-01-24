class Pizza:
    def __init__(self):
        self.size = ""
        self.cheese = False
        self.pepperoni = False
        self.mushrooms = False
        self.onions = False
        self.bacon = False

    def __str__(self):
        return f"Пицца: размер = {self.size}, сыр = {self.cheese}, пепперони = {self.pepperoni}, грибы = {self.mushrooms}, лук = {self.onions}, бекон = {self.bacon}"


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size):
        self.pizza.size = size
        return self

    def add_cheese(self):
        self.pizza.cheese = True
        return self

    def add_pepperoni(self):
        self.pizza.pepperoni = True
        return self

    def add_mushrooms(self):
        self.pizza.mushrooms = True
        return self

    def add_onions(self):
        self.pizza.onions = True
        return self

    def add_bacon(self):
        self.pizza.bacon = True
        return self

    def build(self):
        return self.pizza


class PizzaDirector:
    def __init__(self, builder):
        self.builder = builder

    def make_pizza(self):
        pizza_builder = self.builder
        pizza_builder.set_size("Большая")
        pizza_builder.add_cheese()
        pizza_builder.add_pepperoni()
        pizza_builder.add_mushrooms()

        pizza = pizza_builder.build()

        return pizza


builder = PizzaBuilder()
director = PizzaDirector(builder)
pizza = director.make_pizza()

print(pizza)
