# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room, items):
        self.name = name
        self.room = room
        self.items = items
    
    def __str__(self):
        data = f"Items in room:" 
        p_items = f"Your items:"   
        if len(self.room.items) == 0:
            data += " None"
        else:
            for i, item in enumerate(self.room.items): 
                data += f"\n  {str(i + 1)}: {item.name}"
                data += f"\n  Description: {item.description}"
         
        if len(self.items) == 0:
            p_items += " None"
        else:
            for i, item in enumerate(self.items):
                p_items += f"\n  {str(i + 1)}: {item.name}"
                p_items += f"\n  Description: {item.description}"  
        return f"{self.name}, you are currently in the {self.room.name}.\n{self.room.description}\n{data}\n{p_items}"
    
    def get_item(self, item):
        self.items.append(item)
        print(f"You have picked up a {item.name}")

    def drop_item(self, item):
        self.items.remove(item)
        self.room.items.append(item)
        print(f"You have left the {item.name} in the {self.room}")