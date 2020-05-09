'''
:also known as virtual constructor
:provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created

'''

class ABC:
    def abstractmethod():
        pass

class Creator(ABC):
    '''
    :Creator class declares the factory method that returns an object of a Product class
    :Creator's subclass provides the implementation of this method
    '''

    @abstractmethod
    def factory_method(self):
        '''
        :Creator may also provide some default implemetaion of the factory method
        '''
        pass

    def business_logic(self) -> str:
        '''
        :Creator's primary responsibility is not creating products. Usually, it contains some core business
         logic that relies on Product objects returned by the factory method
        :Subclasses can indirectly change that business logic by overriding the factory method and returning
         a different type of product from it.
        '''

        # call the factory method to create a Product object
        product = self.factory_method()

        result = f"Creator: The sames creator's code has just worked with {product.operation()}"

        return result