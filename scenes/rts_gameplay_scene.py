import pygame
from engine.scene import Scene
from game.unit import Unit
from game.resource import Resource
from game.constants import UNIT_TYPES, RESOURCE_TYPES, RTS_SETTINGS

class RTSGameplayScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.units = []
        self.resources = []
        self.selected_unit = None

    def on_enter(self):
        self.units = [Unit('worker', (100, 100), UNIT_TYPES['worker']['health'], UNIT_TYPES['worker']['attack'], UNIT_TYPES['worker']['speed'])]
        self.resources = [Resource('wood', RESOURCE_TYPES['wood']['amount'])]

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse_click(event.pos)
            elif event.type == pygame.KEYDOWN:
                self.handle_key_press(event.key)

    def handle_mouse_click(self, position):
        for unit in self.units:
            if self.is_unit_clicked(unit, position):
                self.selected_unit = unit
                break

    def handle_key_press(self, key):
        if key == pygame.K_m and self.selected_unit:
            self.selected_unit.move((200, 200))
        elif key == pygame.K_a and self.selected_unit:
            self.selected_unit.attack_unit(self.units[0])
        elif key == pygame.K_g and self.selected_unit:
            self.selected_unit.gather_resource(self.resources[0])

    def is_unit_clicked(self, unit, position):
        unit_rect = pygame.Rect(unit.position[0], unit.position[1], 20, 20)
        return unit_rect.collidepoint(position)

    def update(self):
        for unit in self.units:
            # Update unit logic here
            pass

    def draw(self, screen):
        screen.fill((0, 0, 0))
        for unit in self.units:
            pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(unit.position[0], unit.position[1], 20, 20))
        for resource in self.resources:
            pygame.draw.rect(screen, (139, 69, 19), pygame.Rect(300, 300, 20, 20))
