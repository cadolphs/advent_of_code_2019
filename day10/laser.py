from helpers import Coord


class LaserDriver:
    def __init__(self, laser):
        self.laser = laser

    def fire_and_forget(self):
        while True:
            try:
                yield self.laser.fire()
                self.laser.rotate_to_next_asteroid()
            except NoAsteroidInLineOfFireException:
                break


class Laser:
    def __init__(self, asteroid_map, laser_position):
        self.asteroid_map = asteroid_map

        self.laser_position = laser_position
        self.laser_direction = Coord(0, -1)

        if self.laser_position in self.asteroid_map.asteroid_positions:
            self.asteroid_map.remove_asteroid(self.laser_position)

    def fire(self):
        try:
            asteroid_hit = next(
                self.asteroid_map.all_asteroids_in_line_of(
                    self.laser_position, self.laser_direction
                )
            )
        except StopIteration:
            raise NoAsteroidInLineOfFireException()

        self.asteroid_map.remove_asteroid(asteroid_hit)
        return asteroid_hit

    def rotate_to_next_asteroid(self):
        # Find smallest rotation from current position
        def angle_between_laser_and(asteroid):
            vector_to_asteroid = asteroid - self.laser_position
            return self.laser_direction.angle_with(vector_to_asteroid)

        asteroid_candidates = self.asteroid_map.asteroid_positions.difference(
            self.asteroid_map.all_asteroids_in_line_of(
                self.laser_position, self.laser_direction
            )
        )

        if asteroid_candidates:
            next_asteroid = min(
                asteroid_candidates, key=lambda x: angle_between_laser_and(x),
            )

        self.laser_direction = (next_asteroid - self.laser_position).normalized()


class NoAsteroidInLineOfFireException(Exception):
    pass
