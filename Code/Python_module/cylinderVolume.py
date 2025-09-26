def find_cylinder_volume(radius, height):
    pi = 3.14
    volume = pi * radius**2 * height
    return volume

def find_cylinder_surface_area(radius, height):
    pi = 3.14
    surface_area = 2 * pi * radius * (radius + height)
    return surface_area