
 
import pygame

from settings import Settings
from ship import Ship
from pygame.sprite import Group
from alien import Alien
import game_function as gf

def run_game():
	# 初始化游戏并创建一个屏幕对象 #
	pygame.init()
	ai_settings = Settings()

	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("alien invasion")
	#bg_collor = (230,230,230)

	#创建一艘飞船#
	ship = Ship(ai_settings, screen)
	#创建子弹编组
	bullets = Group()
	aliens = Group()

	# #创建一个外星人

	# alien = Alien(ai_settings, screen)
	gf.create_fleet(ai_settings, screen, ship, aliens)


	while True:
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()

		gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
		gf.update_aliens(ai_settings, aliens)



		self.bullet_width = 300


		# screen.fill(ai_settings.bg_color)
		# ship.blitme()
		# 		#让最近的屏幕可见 #
		# pygame.display.flip()

		gf.update_screen(ai_settings, screen, ship, aliens, bullets )
   

run_game()
print(" 游戏首页 ")



