import sys

import pygame

from ship import Ship
from settings import Settings
from bullet import Bullet
from alien import Alien



def check_keydown_events(event, ai_settings, screen, ship, bullets):
	""" 响应按键 """
	if event.key == pygame.K_RIGHT:
				ship.moving_right = True

	elif event.key == pygame.K_LEFT:
				ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets)


		#退出游戏

	elif event.key == pygame.K_q:
		sys.exit()
		

def check_keyup_events(event, ship):
	""" 响应松开 """	
	if event.key == pygame.K_RIGHT:
				ship.moving_right = False

	elif event.key == pygame.K_LEFT:
				ship.moving_left = False			


def check_events(ai_settings, screen, ship, bullets):



	""" 响应键盘鼠标事件 """
	# 监听键盘鼠标事件 #
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)
			#check_keydown_events(event,ship)

		elif event.type == pygame.KEYUP:
			
			check_keyup_events(event,ship)
			




def update_screen(ai_settings, screen, ship, aliens, bullets):
	screen.fill(ai_settings.bg_color)

	for bullet in bullets.sprites():
		bullet.draw_bullet()

	ship.blitme()
	#aliens.blitme()
	aliens.draw(screen)
				#让最近的屏幕可见 #
	pygame.display.flip()


def update_bullets(ai_settings, screen, ship, aliens, bullets):
	bullets.update()

		#删除已消失的子弹

	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

			print(len(bullets))

	#检查是否有子弹击中外星人
	#删除外星人和子弹

	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

	if len(aliens) == 0:
		#删除现有子弹并新建一群外星人
		bullets.empty()
		create_fleet(ai_settings, screen, ship, aliens)



def fire_bullet(ai_settings, screen, ship, bullets):
	if len(bullets) < ai_settings.bullets_allowed:

			new_bullet = Bullet(ai_settings, screen, ship)
			bullets.add(new_bullet)


	




def create_fleet(ai_settings, screen, ship, aliens):
	#创建外星人群

	#创建一个 ，并计算一行可容纳多少外星人
	alien = Alien(ai_settings, screen)
	number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)

	number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

	#创建第一行外星人

	for row_number in range(number_rows):


		for alien_number in range(number_aliens_x):
			create_alien(ai_settings, screen, aliens, alien_number, row_number)



def get_number_aliens_x(ai_settings, alien_width):
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
	#创建一个外星人加入当前行
		alien = Alien(ai_settings, screen)
		alien_width = alien.rect.width
		alien.x = alien_width + 2 * alien_width * alien_number
		alien.rect.x = alien.x
		alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number

		aliens.add(alien)
	




def get_number_rows(ai_settings, ship_height, alien_height):
	# 计算屏幕可容纳多少行外星人
	available_space_y = (ai_settings.screen_height - ( 3 * alien_height) - ship_height)
	number_rows = int(available_space_y / (2 * alien_height))
	return number_rows

def check_fleet_edges(ai_settings, aliens):
	""" 外星人到达边缘采取相应措施 """
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings, aliens)
			break


def change_fleet_direction(ai_settings, aliens):

	""" 将整群外星人下移，并改变他们的方向 """
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed

	ai_settings.fleet_direction *= -1




def update_aliens(ai_settings, aliens):
	#检查是否有 外星人 位于屏幕边缘 。并更新外星人位置

	check_fleet_edges(ai_settings, aliens)


	""" 更新外星人群中所有外星人的位置 """
	aliens.update()

