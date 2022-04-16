def build_house(dream, colors):
    def build_roof(r,rc):
        """
        input:r-data for build roof, rc-data for roof color
        return:bool
        """
        return True
    def build_walls(w,wc):
        """
        input:w-data for build walls, wc-data for roof color
        return:bool
        """
        return True
    def build_door(r,dc):
        """
        input:r-data for build door, dc-data for roof color
        return:bool
        """
        return True
    house=False
    roof_color=colors[0]
    house_color=colors[1]
    door_color=colors[2]
    roof=dream[0]
    walls=dream[1]
    while not house:
        roof_status=build_roof(roof,roof_color)
        walls_status=build_walls(walls,house_color)
        door_status=build_door(door_color,door_color)
        if roof_status==True and walls_status==True and door_status==True:
            house=True
            print('Дом построен')
    return house
idea=('roof','walls')
colors=('red','green','blue')
build_house(idea, colors)