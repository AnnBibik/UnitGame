from abc import ABC, abstractmethod


class Unit(ABC):
    _name = ''
    _health = 0
    _attack = 0
    _defence = 0

    @property
    @abstractmethod
    def dmg(self):
        pass

    @dmg.setter
    @abstractmethod
    def dmg(self, val):
        pass

    @property
    @abstractmethod
    def defence(self):
        pass

    @defence.setter
    @abstractmethod
    def defence(self, val):
        pass

    @property
    @abstractmethod
    def health(self):
        pass

    @health.setter
    def health(self, val):
        pass

    def hit(self, enemy):
        if not isinstance(enemy, Unit) or enemy.health < 0:
            raise Exception("Enemy must be an is instance of Unit with health > 0")

        enemy_def = enemy.defence
        damage = self.dmg - enemy_def

        if damage > 0:
            enemy.health -= damage


class Human(Unit, ABC):
    _head = None
    _l_arm = None
    _r_arm = None

    def equip(self, eq_obj):
        if not isinstance(eq_obj, Equipment):
            return

        if hasattr(self, eq_obj.eq_place):
            setattr(self, eq_obj.eq_place, eq_obj)


class Equipment:
    eq_place = ''
    dmg_mod = 0
    def_mod = 0
    health_mod = 0

    def __init__(self, damage, defence, health, place):
        self.place = place
        self.damage = damage
        self.defence = defence
        self.health = health

    @property
    def place(self):
        return self.eq_place

    @place.setter
    def place(self, value):
        if not isinstance(value, str):
            raise Exception
        else:
            self.eq_place = value

    @property
    def damage(self):
        return self.dmg_mod

    @damage.setter
    def damage(self, value):
        if not isinstance(value, int):
            raise Exception
        else:
            self.dmg_mod = value

    @property
    def defence(self):
        return self.def_mod

    @defence.setter
    def defence(self, value):
        if not isinstance(value, int):
            raise Exception
        else:
            self.def_mod = value

    @property
    def health(self):
        return self.health_mod

    @health.setter
    def health(self, value):
        if not isinstance(value, int):
            raise Exception
        else:
            self.health_mod = value


class Knight(Human):
    @property
    def dmg(self):
        return self._attack

    @dmg.setter
    def dmg(self, value):
        self._attack = value

    @property
    def defence(self):
        return self._defence

    @defence.setter
    def defence(self, value):
        self._defence = value

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, val):
        if val < 0:
            val = 0
        self._health = val


class Mag(Human):

    @property
    def dmg(self):
        return self._attack

    @dmg.setter
    def dmg(self, value):
        self._attack = value

    @property
    def defence(self):
        return self._defence

    @defence.setter
    def defence(self, value):
        self._defence = value

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, val):
        if val < 0:
            val = 0
        self._health = val
