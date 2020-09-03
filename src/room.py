# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items

    def __str__(self):
        data = f"Items in room:\n"
        for i, item in enumerate(self.items): 
            data += f"  {str(i + 1)}: {item.name}\n"
            data += f"  Description: {item.description}"
            return data
