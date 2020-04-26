
class Property:

    def __init__(self, position, sale_price, rental_price, owner):
        self._position = position
        self._sale_price = sale_price
        self._rental_price = rental_price
        self._owner = owner

    @property
    def position(self):
        """get position"""
        return self._position

    @position.setter
    def position(self, position):
        """set position"""
        self._position = position

    @property
    def sale_price(self):
        """get sale price"""
        return self._sale_price

    @sale_price.setter
    def sale_price(self, sale_price):
        """set sale price"""
        self._sale_price = sale_price

    @property
    def rental_price(self):
        """get rental price"""
        return self._rental_price

    @rental_price.setter
    def rental_price(self, rental_price):
        """set rental price"""
        self._rental_price = rental_price

    @property
    def owner(self):
        """get owner"""
        return self._owner

    @owner.setter
    def owner(self, owner):
        """set owner"""
        self._owner = owner

    def has_owner(self):
        return self.owner is not None
