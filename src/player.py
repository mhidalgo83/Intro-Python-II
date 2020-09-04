# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room, items):
        self.name = name
        self.room = room
        self.items = items
    
    def __str__(self):
        data = f"Items in room:" 
           
        if len(self.room.items) == 0:
            data += " None"
        else:
            for i, item in enumerate(self.room.items): 
                data += f"\n  {str(i + 1)}: {item.name}"
                data += f"\n  Description: {item.description}"
                
        return f"{self.name}, you are currently in the {self.room.name}.\n{self.room.description}\n{data}"
    
    def get_item(self, item_name):
        if len(self.room.items) == 0:
            print("There are no items in the room to pick up.")
        else:
            for item in self.room.items:
                if item_name == item.name:
                    self.items.append(item)
                    self.room.items.remove(item)
                    print(f"You have picked up a {item.name}")
                    print("---------------")
                else:
                    print("Item not in room. Try picking up something else.")
                    print("---------------")

    def drop_item(self, item_name):
        for item in self.items:
            if item_name == item.name:
                self.items.remove(item)
                self.room.items.append(item)
                print(f"You have left the {item.name} in the {self.room}")
                print("---------------")

    def check_inventory(self):
        p_items = f"Your items:"
        if len(self.items) == 0:
            p_items += " None"
        else:
            for i, item in enumerate(self.items):
                p_items += f"\n  {str(i + 1)}: {item.name}"
                p_items += f"\n  Description: {item.description}"  
        print(f"{p_items}")
        print("---------------")