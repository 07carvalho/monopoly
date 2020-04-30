
class Property:

    def __init__(self, position: int, sale_price: int, rental_price: int, owner):
        self._position = position
        self._sale_price = sale_price
        self._rental_price = rental_price
        self._owner = owner

    def __str__(self):
        return str(self._position)

    @property
    def position(self) -> int:
        """get position"""
        return self._position

    @position.setter
    def position(self, position: int):
        """set position"""
        self._position = position

    @property
    def sale_price(self) -> int:
        """get sale price"""
        return self._sale_price

    @sale_price.setter
    def sale_price(self, sale_price: int):
        """set sale price"""
        self._sale_price = sale_price

    @property
    def rental_price(self) -> int:
        """get rental price"""
        return self._rental_price

    @rental_price.setter
    def rental_price(self, rental_price: int):
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

    def has_owner(self) -> bool:
        return self.owner is not None
