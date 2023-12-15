class Vehicle:

    def __init__(self, name, max_speed, acceleration, deceleration, turning_speed):
        self.name = name
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.deceleration = deceleration
        self.turning_speed = turning_speed
        self.time_to_max_speed = self.get_time_to_max_speed()
        self.distance_to_max_speed = self.get_distance_to_max_speed()
        self.time_to_stop_from_max_speed = self.get_time_from_max_speed_to_stop()
        self.distance_to_stop_from_max_speed = self.get_distance_to_stop_from_max_speed()

    def get_time_to_max_speed(self):
        time_to_max_speed = self.max_speed / self.acceleration
        return time_to_max_speed

    def get_distance_to_max_speed(self):
        distance_to_max_speed = self.max_speed ** 2 / (2 * self.acceleration)
        return distance_to_max_speed

    def get_time_from_max_speed_to_stop(self):
        time_from_max_speed_to_stop = self.max_speed / self.deceleration
        return time_from_max_speed_to_stop

    def get_distance_to_stop_from_max_speed(self):
        distance_from_max_speed_to_stop = self.max_speed ** 2 / (2 * self.deceleration)
        return distance_from_max_speed_to_stop

