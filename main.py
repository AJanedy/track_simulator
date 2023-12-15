from vehicle_class import Vehicle
from math import sqrt
import time


def main():
    vehicle_list = initiate_vehicles()
    simulate_track_1(vehicle_list)
    simulate_track_2(vehicle_list)
    simulate_track_3(vehicle_list)
    simulate_track_4(vehicle_list)
    simulate_track_5(vehicle_list)


def initiate_vehicles():
    suv = Vehicle("SUV", 50, 4, 3, 16)
    sedan = Vehicle("Sedan", 45, 5, 4, 13)
    my_car = Vehicle("My Car", 30, 3, 3, 6)
    motorcycle = Vehicle("Motorcycle", 60, 6, 4, 10)
    hover_car = Vehicle("Hover Car", 70, 4, 1, 2)

    list_of_vehicles = [suv, sedan, my_car, motorcycle, hover_car]

    return list_of_vehicles


def simulate_track_1(list_of_vehicles):
    track_length = 200
    print()

    for vehicle in list_of_vehicles:
        current_speed, distance_traveled_while_accelerating, start_time, \
            time_accelerating, total_distance_traveled, total_elapsed_time, \
            _, max_speed, _ = initialize_lap_variables()
        max_speed = 0
        while track_length > total_distance_traveled:
            if current_speed < vehicle.max_speed:
                time_accelerating = time.time() - start_time
                current_speed = vehicle.acceleration * time_accelerating
                if current_speed > max_speed:
                    max_speed = current_speed
                distance_traveled_while_accelerating = .5 * vehicle.acceleration * time_accelerating ** 2
                total_distance_traveled = distance_traveled_while_accelerating
                total_elapsed_time = time_accelerating
            else:
                time_at_max_speed = time.time() - start_time - time_accelerating
                current_speed = vehicle.max_speed
                max_speed = current_speed
                distance_traveled_at_max_speed = current_speed * time_at_max_speed
                total_distance_traveled = distance_traveled_at_max_speed + distance_traveled_while_accelerating
                total_elapsed_time = time_accelerating + time_at_max_speed

        print(f"{vehicle.name} completed track 1 in {total_elapsed_time:.2f} seconds "
              f"with a max speed of {max_speed:.2f} m/s")


def simulate_track_2(list_of_vehicles):
    track_length = 350
    print()

    for vehicle in list_of_vehicles:
        current_speed, distance_traveled_while_accelerating, start_time, \
            time_accelerating, total_distance_traveled, total_elapsed_time, \
            distance_to_wall, max_speed_reached, _ = initialize_lap_variables()
        while track_length > total_distance_traveled:
            if current_speed < vehicle.max_speed:
                distance_needed_to_stop = (current_speed ** 2) / (2 * vehicle.deceleration)
                time_accelerating = time.time() - start_time
                current_speed = vehicle.acceleration * time_accelerating
                max_speed_reached = current_speed
                distance_traveled_while_accelerating = .5 * vehicle.acceleration * time_accelerating ** 2
                total_distance_traveled = distance_traveled_while_accelerating
                distance_to_wall = track_length - distance_traveled_while_accelerating
                total_elapsed_time = time_accelerating
                if distance_to_wall <= distance_needed_to_stop:
                    time_to_stop = current_speed / vehicle.deceleration
                    total_elapsed_time += time_to_stop
                    break
            else:
                distance_needed_to_stop = (current_speed ** 2) / (2 * vehicle.deceleration)
                time_at_max_speed = time.time() - start_time - time_accelerating
                current_speed = vehicle.max_speed
                max_speed_reached = current_speed
                distance_traveled_at_max_speed = current_speed * time_at_max_speed
                total_distance_traveled = distance_traveled_at_max_speed + distance_traveled_while_accelerating
                distance_to_wall = track_length - total_distance_traveled
                total_elapsed_time = time_accelerating + time_at_max_speed
                if distance_to_wall <= distance_needed_to_stop:
                    time_to_stop = current_speed / vehicle.deceleration
                    total_elapsed_time += time_to_stop
                    break
        print(f"{vehicle.name} completed track 2 in {total_elapsed_time:.2f} seconds "
              f"with a max speed of {max_speed_reached:.2f} m/s")


def simulate_track_3(list_of_vehicles):
    length_lengths = [100, 300, 100, 300]
    print()

    for vehicle in list_of_vehicles:
        current_speed, distance_traveled_while_accelerating, _, \
            time_accelerating, distance_traveled, total_elapsed_time, \
            distance_to_wall, max_speed_reached, leg_time = initialize_lap_variables()
        for index, length in enumerate(length_lengths):
            start_time = time.time()
            distance_traveled = 0
            while distance_traveled < length:
                if current_speed < vehicle.max_speed:
                    distance_needed_to_slow = (current_speed**2 - vehicle.turning_speed**2) / (2 * vehicle.deceleration)
                    time_accelerating = time.time() - start_time
                    if index == 0:
                        current_speed = (vehicle.acceleration * time_accelerating)
                    else:
                        current_speed = vehicle.turning_speed + (vehicle.acceleration * time_accelerating)
                    if current_speed > max_speed_reached:
                        max_speed_reached = current_speed
                    distance_traveled_while_accelerating = .5 * vehicle.acceleration * time_accelerating ** 2
                    distance_to_corner = length - distance_traveled_while_accelerating
                    leg_time = time_accelerating
                    if distance_to_corner <= distance_needed_to_slow:
                        time_to_slow = (current_speed - vehicle.turning_speed) / vehicle.deceleration
                        leg_time += time_to_slow
                        total_elapsed_time += leg_time
                        current_speed = vehicle.turning_speed
                        distance_traveled += length
                        break
                else:
                    distance_needed_to_slow = (current_speed**2 - vehicle.turning_speed**2) / (2 * vehicle.deceleration)
                    time_at_max_speed = time.time() - start_time - time_accelerating
                    current_speed = vehicle.max_speed
                    max_speed_reached = current_speed
                    distance_traveled_at_max_speed = current_speed * time_at_max_speed
                    distance_traveled = distance_traveled_at_max_speed + distance_traveled_while_accelerating
                    distance_to_corner = length - distance_traveled
                    leg_time = time_accelerating + time_at_max_speed
                    if distance_to_corner <= distance_needed_to_slow:
                        time_to_slow = current_speed / vehicle.deceleration
                        leg_time += time_to_slow
                        total_elapsed_time += leg_time
                        distance_traveled += length
                        current_speed = vehicle.turning_speed
        print(f"{vehicle.name} completed track 3 in {total_elapsed_time:.2f} seconds "
              f"with a max speed of {max_speed_reached:.2f} m/s")


def simulate_track_4(list_of_vehicles):
    length_lengths = [200, 200, 200, 200]
    print()

    for vehicle in list_of_vehicles:
        current_speed, distance_traveled_while_accelerating, _, \
            time_accelerating, distance_traveled, total_elapsed_time, \
            distance_to_wall, max_speed_reached, leg_time = initialize_lap_variables()
        for index, length in enumerate(length_lengths):
            start_time = time.time()
            distance_traveled = 0
            while distance_traveled < length:
                if current_speed < vehicle.max_speed:
                    distance_needed_to_slow = (current_speed ** 2 - vehicle.turning_speed ** 2) / (
                                2 * vehicle.deceleration)
                    time_accelerating = time.time() - start_time
                    if index == 0:
                        current_speed = (vehicle.acceleration * time_accelerating)
                    else:
                        current_speed = vehicle.turning_speed + (vehicle.acceleration * time_accelerating)
                    if current_speed > max_speed_reached:
                        max_speed_reached = current_speed
                    distance_traveled_while_accelerating = .5 * vehicle.acceleration * time_accelerating ** 2
                    distance_to_corner = length - distance_traveled_while_accelerating
                    leg_time = time_accelerating
                    if distance_to_corner <= distance_needed_to_slow:
                        time_to_slow = (current_speed - vehicle.turning_speed) / vehicle.deceleration
                        leg_time += time_to_slow
                        total_elapsed_time += leg_time
                        current_speed = vehicle.turning_speed
                        distance_traveled += length
                        break
                else:
                    distance_needed_to_slow = ((current_speed ** 2 - vehicle.turning_speed ** 2) /
                                               (2 * vehicle.deceleration))
                    time_at_max_speed = time.time() - start_time - time_accelerating
                    current_speed = vehicle.max_speed
                    max_speed_reached = current_speed
                    distance_traveled_at_max_speed = current_speed * time_at_max_speed
                    distance_traveled = distance_traveled_at_max_speed + distance_traveled_while_accelerating
                    distance_to_corner = length - distance_traveled
                    leg_time = time_accelerating + time_at_max_speed
                    if distance_to_corner <= distance_needed_to_slow:
                        time_to_slow = current_speed / vehicle.deceleration
                        leg_time += time_to_slow
                        total_elapsed_time += leg_time
                        distance_traveled += length
                        current_speed = vehicle.turning_speed
        print(f"{vehicle.name} completed track 4 in {total_elapsed_time:.2f} seconds "
              f"with a max speed of {max_speed_reached:.2f} m/s")


def simulate_track_5(list_of_vehicles):
    track_length = 1000
    print()

    for vehicle in list_of_vehicles:
        current_speed, distance_traveled_while_accelerating, start_time, \
            time_accelerating, total_distance_traveled, total_elapsed_time, \
            _, max_speed, _ = initialize_lap_variables()
        max_speed = 0
        while track_length > total_distance_traveled:
            if current_speed < vehicle.max_speed:
                time_accelerating = time.time() - start_time
                current_speed = vehicle.acceleration * time_accelerating
                if current_speed > max_speed:
                    max_speed = current_speed
                distance_traveled_while_accelerating = .5 * vehicle.acceleration * time_accelerating ** 2
                total_distance_traveled = distance_traveled_while_accelerating
                total_elapsed_time = time_accelerating
            else:
                time_at_max_speed = time.time() - start_time - time_accelerating
                current_speed = vehicle.max_speed
                max_speed = current_speed
                distance_traveled_at_max_speed = current_speed * time_at_max_speed
                total_distance_traveled = distance_traveled_at_max_speed + distance_traveled_while_accelerating
                total_elapsed_time = time_accelerating + time_at_max_speed

        print(f"{vehicle.name} completed track 5 in {total_elapsed_time:.2f} seconds "
              f"with a max speed of {max_speed:.2f} m/s")


def initialize_lap_variables():
    distance_traveled_while_accelerating = 0
    distance_traveled_at_max_speed = 0
    total_distance_traveled = distance_traveled_at_max_speed + distance_traveled_while_accelerating
    current_speed = 0
    start_time = time.time()
    time_accelerating = 0
    time_at_max_speed = 0
    total_elapsed_time = time_accelerating + time_at_max_speed
    distance_to_wall = 350
    max_speed = 0
    leg_time = 0
    return current_speed, distance_traveled_while_accelerating, start_time, \
        time_accelerating, total_distance_traveled, total_elapsed_time, distance_to_wall, \
        max_speed, leg_time


main()
