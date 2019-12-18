import numpy as np


class StatusWriter:
    def get_status_string(self, moons):
        all_positions = np.stack([moon.pos for moon in moons], axis=0)
        all_velocities = np.stack([moon.vel for moon in moons], axis=0)

        pos_lens = [self.get_padding_size(all_positions[:, i]) for i in range(3)]
        vel_lens = [self.get_padding_size(all_velocities[:, i]) for i in range(3)]

        status_format = f"pos=<x={{pos[0]:{pos_lens[0]}d}}, y={{pos[1]:{pos_lens[1]}d}}, z={{pos[2]:{pos_lens[2]}d}}>, vel=<x={{vel[0]:{vel_lens[0]}d}}, y={{vel[1]:{vel_lens[1]}d}}, z={{vel[2]:{vel_lens[2]}d}}>"

        lines = [status_format.format(pos=moon.pos, vel=moon.vel) for moon in moons]

        return "\n".join(lines)

    def get_padding_size(self, values):
        return max(max(len(str(value)) for value in values), 2)
