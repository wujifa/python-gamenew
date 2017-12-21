class Settings(object):
	"""存储《外星人入侵》的所有设置的类"""
	def __init__(self):
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (130,230,230)
		self.ship_speed_factor = 5

		#子弹设置
		self.bullet_speed_factor = 10
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60,60,60)
		self.bullets_allowed = 6
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 10
		# fleet_direction  1 像右移动 -1向左
		self.fleet_direction = 1



