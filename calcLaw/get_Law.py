import math


class Servo(object):
    def __init__(self, radius, height, base_angle_pivot,platform_height,horn_length, rod_length, horn_angle,
                 horn_angle_base,dx,dy,dz,phi,theta,psi):
        self.height = height
        self.platform_height = platform_height
        self.base_angle_pivot = base_angle_pivot  # Угол между шарнинром на двигателе и горизонтальной линией на базе
        self.radius = radius
        self.horn_length = horn_length # Длина кривошипа
        self.horn_angle = horn_angle # Начальный угол поворота
        self.horn_angle_base = horn_angle_base # Угол между кривошипом и горизонталью (Ось х)
        self.dx = dx
        self.dy = dy
        self.dz = dz
        self.phi = phi
        self.theta = theta
        self.psi = psi
        self.rod_length = rod_length


    # Координата x шарнира на сервоприводе
    def get_base_x_coordinate(self):
        value = self.radius * math.cos(math.radians(self.base_angle_pivot))
        return round(value, 2)

    # Координата y шарнира на сервоприводе
    def get_base_y_coordinate(self):
        value = self.radius * math.sin(math.radians(self.base_angle_pivot))
        return round(value, 2)

    # Координата z шарнира на сервоприводе
    def get_base_z_coordinate(self):
        value = self.height * 1
        return round(value, 2)

    # Полные координаты шарнира на сервоприводе
    def get_base_full_coordinates(self):
        value = []
        value.extend([self.get_base_x_coordinate(), self.get_base_y_coordinate(), self.get_base_z_coordinate()])
        return value

    # Координата x шарнира на платформе
    def get_platform_x_coordinate(self):
        value = self.radius * math.cos(math.radians(self.base_angle_pivot))
        return round(value, 2)

    # Координата y шарнира на платформе
    def get_platform_y_coordinate(self):
        value = self.radius * math.sin(math.radians(self.base_angle_pivot))
        return round(value, 2)

    # Координата z шарнира на платформе
    def get_platform_z_coordinate(self):
        value = self.platform_height * 1
        return round(value, 2)

    # Полные координаты шарнира на платформе
    def get_platform_full_coordinates(self):
        value = []
        value.extend([self.get_platform_x_coordinate(), self.get_platform_y_coordinate(),
                      self.get_platform_z_coordinate()])
        return value
    def get_horn_x_coordinate(self):
        value = self.get_base_x_coordinate() + self.horn_length * math.cos(math.radians(self.horn_angle)) * math.cos(
            math.radians(self.horn_angle_base))
        return round(value, 2)

    # Координата y шарнира на кривошипе
    def get_horn_y_coordinate(self):
        value = self.get_base_y_coordinate() + self.horn_length * math.sin(
            math.radians(self.horn_angle_base)) * math.cos(math.radians(self.horn_angle))
        return round(value, 2)

    # Координата z шарнира на кривошипе
    def get_horn_z_coordinate(self):
        value = self.horn_length * math.sin(math.radians(self.horn_angle)) + self.get_base_z_coordinate()
        return round(value, 2)

    # Полные координаты шарнира на кривошипе
    def get_horn_full_coordinates(self):
        value = []
        value.extend([self.get_horn_x_coordinate(), self.get_horn_y_coordinate(), self.get_horn_z_coordinate()])
        return value

    def get_platform_new_x_coordinate(self):
        value = self.get_platform_x_coordinate() * math.cos(math.radians(self.phi)) * math.cos(
            math.radians(self.psi)) + self.get_platform_y_coordinate() * (
                        math.sin(math.radians(self.theta)) * math.sin(math.radians(self.phi)) * math.cos(
                    math.radians(self.phi)) - math.cos(math.radians(self.theta)) * math.sin(
                    math.radians(self.psi))) + self.dx
        return value

    def get_platform_new_y_coordinate(self):
        value = self.get_platform_x_coordinate() * math.cos(math.radians(self.phi)) * math.sin(
            math.radians(self.psi)) + self.get_platform_y_coordinate() * (
                        math.cos(math.radians(self.theta)) * math.cos(math.radians(self.psi)) + math.sin(
                    math.radians(self.theta)) * math.sin(math.radians(self.phi)) * math.sin(
                    math.radians(self.psi))) + self.dy
        return value

    def get_platform_new_z_coordinate(self):
        value = self.get_platform_x_coordinate() * math.sin(math.radians(self.phi)) + self.get_platform_y_coordinate(
        ) * math.sin(math.radians(self.theta)) * math.cos(math.radians(self.phi)) + self.dz + self.platform_height
        return value

    def get_platform_new_full_coordinates(self):
        value = []
        value.extend([self.get_platform_new_x_coordinate(), self.get_platform_new_y_coordinate(),
                      self.get_platform_new_z_coordinate()])
        return value

    def get_dimension(self):
        return [x - y for x, y in zip(self.get_base_full_coordinates(),self.get_platform_new_full_coordinates())]

    def get_virtual_length_rod(self):
        list_one = [x ** 2 for x in self.get_dimension()]
        result = math.sqrt(sum(list_one))
        return result

    def get_length_cathet_L(self):
        return self.get_virtual_length_rod() ** 2 - (self.rod_length ** 2 - self.horn_length ** 2)

    def get_length_cathet_M(self):
        value = 2 * self.horn_length * (self.get_platform_new_z_coordinate() - self.get_base_z_coordinate())
        return value

    def get_length_cathet_N(self):
        value = 2 * self.horn_length * (math.cos(math.radians(self.base_angle_pivot)) *
                                        (self.get_platform_new_x_coordinate() - self.get_base_x_coordinate()) +
                                        math.sin(math.radians(self.base_angle_pivot)) *
                                        (self.get_platform_new_y_coordinate() - self.get_base_y_coordinate()))
        return value

    def get_angle_of_rod(self):
        sqrt_0 = math.sqrt(self.get_length_cathet_M() ** 2 + self.get_length_cathet_N() ** 2)
        value_0 = self.get_length_cathet_L() / sqrt_0
        asin = math.asin(value_0)
        atan = math.atan(self.get_length_cathet_N() / self.get_length_cathet_M())
        angle = asin - atan
        return math.degrees(angle)