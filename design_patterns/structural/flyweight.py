from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


# Step 1: define flyweight interface
class IEnemyFlyweight(ABC):
    """
    Flyweight interface declares a method for acvcepting extrinsic state and
    performing operations based on it
    """

    @abstractmethod
    def render(self, x: int, y: int):
        """Render method accepting extrinsic state as input"""
        pass


# step 2: create concrete flyweight classes
class EnemyTypeA(IEnemyFlyweight):
    """Flyweight class for Enemy type A"""

    def __init__(self, texture: str):
        self._texture = texture  # shared state

    def render(self, x: int, y: int):
        """Render enemy type A with a given position"""
        print(f"EnemyTypeA: {self._texture}, ({x}, {y})")


# step 3: implement flyweight factory
class EnemyFlyweightFactory:
    """
    FlyweighFactory manages flyweight objects and ensures their uniqueness
    """

    _flyweights = {}

    @staticmethod
    def get_flyweight(texture):
        """
        Retreive or create a flyweight object based on the provided texture
        """
        if texture not in EnemyFlyweightFactory._flyweights:
            EnemyFlyweightFactory._flyweights[texture] = EnemyTypeA(texture)
        return EnemyFlyweightFactory._flyweights[texture]


# step 4: define client class
class GameEnvironment:
    """
    Client class represents objects that use flyweight objects
    """

    def __init__(self):
        self._enemies: List[IEnemyFlyweight] = []

    def add_enemy(self, texture, x: int, y: int):
        """
        Add new enemy to the game environment
        """
        flyweight = EnemyFlyweightFactory.get_flyweight(texture)
        self._enemies.append((flyweight, x, y))

    def render_enemies(self):
        """
        Render all enemies in the game environment
        """
        for flyweight, x, y in self._enemies:
            flyweight.render(x, y)


if __name__ == "__main__":
    game = GameEnvironment()

    for r in range(3):
        for c in range(3):
            if r % 2 == 0:
                texture = "green"
            else:
                texture = "red"
            game.add_enemy(texture, r, c)

    game.render_enemies()
