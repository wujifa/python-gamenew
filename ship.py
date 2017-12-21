import pygame

class Ship():
	"""docstring for Ship"""
	def __init__(self, ai_settings, screen):
		self.screen = screen
		self.ai_settings = ai_settings
		self.image = pygame.image.load('images/hm.png')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#将 每艘飞船放在屏幕中央#
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		#center中存储最小数值

		self.center = float(self.rect.centerx)





		# 移动标志
		self.moving_right = False
		self.moving_left = False


	def update(self):
		""" 限制速度 """

		# if self.moving_right:
		# 	#self.rect.centerx += 1
		# 	self.center += self.ai_settings.ship_speed_factor

		# if self.moving_left:
		# 	#self.rect.centerx -= 1

		# 	self.center -= self.ai_settings.ship_speed_factor
		""" 限制不让走出屏幕  """

		if self.moving_right and self.rect.right < self.screen_rect.right:
			#self.rect.centerx += 1
			self.center += self.ai_settings.ship_speed_factor

		if self.moving_left and self.rect.left > 0:
			#self.rect.centerx -= 1

			self.center -= self.ai_settings.ship_speed_factor



		self.rect.centerx = self.center


	def blitme(self):
		#在底部位置绘制飞船#
		self.screen.blit(self.image,self.rect)
print("1111")

