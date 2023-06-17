import pygame as pg

from controller.keyboard_controller import KeyboardController
from controller.mouse_controller import MouseController

class EventManager:

    def __init__(self,game) -> None:
        self.keyboard_controller = KeyboardController(game)
        self.mouse_contoller = MouseController(game)

    def check_event_type(self,event_list):
        for event in event_list:
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            elif  event.type == pg.KEYDOWN:
                self.keyboard_controller.manage_event(event)
            elif  event.type == pg.MOUSEBUTTONDOWN:
                self.mouse_contoller.manage_event(event)

        