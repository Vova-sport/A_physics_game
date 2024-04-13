import random


def fill_sprite_list(textures_name,
                     obj_class,
                     path,
                     size,
                     coords: list,
                     sprite_list,
                     fill_random='',
                     center_x=450,
                     center_y=300):
    local_func_coords = coords

    if fill_random == 'random y' or fill_random == 'random x' or fill_random == 'random all':
        for img in textures_name:
            obj = obj_class(path + '/' + img, size)

            if fill_random == 'random y':
                y = random.choice(local_func_coords[0])
                i = local_func_coords[0].index(y)
                local_func_coords[0].pop(i)
                obj.center_y = y
                obj.center_x = center_x
            elif fill_random == 'random x':
                x = random.choice(local_func_coords[0])
                i = local_func_coords[0].index(x)
                local_func_coords[0].pop(i)
                obj.center_x = x
                obj.center_y = center_y

            elif fill_random == 'random all':
                x = random.choice(local_func_coords[0])
                i_x = local_func_coords[0].index(x)
                local_func_coords[0].pop(i_x)
                obj.center_x = x

                y = random.choice(local_func_coords[1])
                i_y = local_func_coords[1].index(y)
                local_func_coords[1].pop(i_y)
                obj.center_y = y

            sprite_list.append(obj)

        return

    for index, img in enumerate(textures_name):
        obj = obj_class(path + '/' + img, size)
        obj.center_x = local_func_coords[0][index][0]
        obj.center_y = local_func_coords[0][index][1]
        sprite_list.append(obj)
