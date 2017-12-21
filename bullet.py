import pygame

from pygame.sprite import Sprite
from settings import Settings
class Bullet(Sprite):
	"""docstring for Bullet"""

	def __init__(self, ai_settings, screen, ship):
		super().__init__()
		self.screen = screen
		self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top

		#存储小数子弹位置
		self.y = float(self.rect.y)
		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor



	def update(self):
		""" 向上移动子弹 """
		#更新表示子弹位置的小数值
		self.y -= self.speed_factor

		self.rect.y = self.y

	def draw_bullet(self):
		""" 在屏幕上绘制子弹头 """
		pygame.draw.rect(self.screen, self.color, self.rect)
		