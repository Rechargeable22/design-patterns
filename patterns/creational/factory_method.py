"""Factory method is a creational design pattern that provides an interface for creating
objects in a superclass, but allows subclasses to alter the type of objects that will be
created"""


class Product:
    def use(self):
        raise NotImplementedError("Not implemented!")


class ConcreteProductA(Product):
    def use(self):
        return "# Using Concrete Product A #"


class ConcreteProductB(Product):
    def use(self):
        return "# Using Concrete Product B #"


class Creator:
    def factory_method(self):
        pass

    def some_operation(self):
        # Call the factory method to create a Product object.
        product = self.factory_method()
        result = f"Creator: The same creator's code has just worked with {product.use()}"
        return result


class ConcreteCreatorA(Creator):
    def factory_method(self):
        return ConcreteProductA()


class ConcreteCreatorB(Creator):
    def factory_method(self):
        return ConcreteProductB()


def client_code(creator: Creator):
    print(creator.some_operation())


if __name__ == '__main__':
    # Application picks creator type based on need / configuration / env
    creator_a = ConcreteCreatorA()
    client_code(creator_a)

    creator_b = ConcreteCreatorB()
    client_code(creator_b)
