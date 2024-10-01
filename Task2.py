class Water:
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Ground):
            return Mud()


class Air:
    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Ground):
            return Dust()


class Fire:
    def __add__(self, other):
        if isinstance(other, Ground):
            return Lava()


class Ground:
    pass


class Storm:
    answer = 'You added Water to Air and got class Storm'


class Steam:
    answer = 'You added Water to Fire and got class Steam'


class Mud:
    answer = 'You added Water to Ground and got class Mud'


class Lightning:
    answer = 'You added Air to Fire and got class Lightning'


class Dust:
    answer = 'You added Air to Ground and got class Dust'


class Lava:
    answer = 'You added Fire to Ground and got class Lava'


if __name__ == '__main__':
    water = Water()
    air = Air()
    fire = Fire()
    ground = Ground()
    addition1 = water + air
    addition2 = water + fire
    addition3 = water + ground
    addition4 = air + fire
    addition5 = air + ground
    addition6 = fire + ground
    print(addition1.answer, type(addition1))
    print(addition2.answer, type(addition2))
    print(addition3.answer, type(addition3))
    print(addition4.answer, type(addition4))
    print(addition5.answer, type(addition5))
    print(addition6.answer, type(addition6))


