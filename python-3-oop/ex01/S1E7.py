from S1E9 import Character

class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name, is_alive=True, family_name="Baratheon", eyes='brown', hairs='dark'):
        """Your docstring for Constructor"""
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs
    def die(self):
        """Your docstring for Method"""
        self.is_alive = False
    
    def __str__(self):
        # Custom output format to mimic bound method output style
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        # Custom output format to mimic bound method output style
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
   

class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(self, first_name, is_alive=True, family_name="Lannister", eyes='blue', hairs='light'):
        """Your docstring for Constructor"""
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs
    
    def die(self):
        """Your docstring for Method"""
        self.is_alive = False
    
    def __str__(self):
        # Custom output format to mimic bound method output style
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        # Custom output format to mimic bound method output style
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
    
    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Class method to create a new Lannister instance"""
        return cls(first_name, is_alive)
