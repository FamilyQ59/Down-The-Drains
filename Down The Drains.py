# Initiate pygame
import pygame
import sys
import os
import random

pygame.init()
pygame.mixer.init()
SC_width, SC_height = 800, 600
SC = pygame.display.set_mode((SC_width, SC_height))
clock = pygame.time.Clock()
Music = True

# Colors
white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
light_blue = pygame.Color(69, 139, 116)
gray = pygame.Color(127, 127, 127)


    #Control Game
#Attacks
enemiesOn = True
projectile_damage = 3
mag_size = 21

#Size
stillX = 40
stillY = 70
walkX = 50
walkY = 70
reloadX = 40
reloadY = 70
crouch_slideX = 43
crouch_slideY = 45
enemyX = 60
enemyY = 70
cannonX = 55
cannonY = 60
cannonBallXY = 50
shieldXY = 60
bulletXY = 7

#Position
player_x = 150
player_y = 290
cannonV_X = 440
cannonV_Y = 0
cannonH_X = 740
cannonH_Y = 250
enemyLeft_x = 750
enemyLeft_Y = 290
enemyRight_X = 0
enemyRight_Y = 290

#Boundaries
CN2_boundaryTop = 200
CN2_boundaryBottom = 350
shield_boundary = 290

# import images
bulletImg = pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "Bullet2.png")).convert_alpha(), (bulletXY, bulletXY))
shieldImg = pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "shield_powerup.png")).convert_alpha(), (shieldXY, shieldXY))
shielded_HB = pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "Shielded_healthbar.png")).convert_alpha(), (300, 35))

still = pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "character_right.png")).convert_alpha(), (stillX, stillY))
still2 = pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "character_left.png")).convert_alpha(), (stillX, stillY))
shield_still = pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "Shield_right.png")).convert_alpha(), (stillX, stillY))
shield_still2 = pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "Shield_left.png")).convert_alpha(), (stillX, stillY))

left = [pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "Run4.png")).convert_alpha(),(walkX,walkY)),
        pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "Run5.png")).convert_alpha(),(walkX,walkY)),
        pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "Run6.png")).convert_alpha(),(walkX,walkY))
        ]

right =[pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "Run1.png")).convert_alpha(),(walkX,walkY)),
        pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "Run2.png")).convert_alpha(),(walkX,walkY)),
        pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "Run3.png")).convert_alpha(),(walkX,walkY))
        ]

Shield_left =[pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "Shield_run4.png")).convert_alpha(),(walkX,walkY)),
        pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "Shield_run5.png")).convert_alpha(),(walkX,walkY)),
        pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "Shield_run6.png")).convert_alpha(),(walkX,walkY))
        ]

Shield_right =[pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "Shield_run1.png")).convert_alpha(),(walkX,walkY)),
        pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "Shield_run2.png")).convert_alpha(),(walkX,walkY)),
        pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "Shield_run3.png")).convert_alpha(),(walkX,walkY))
        ]

reload_left = [pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "left_reload1.png")).convert_alpha(),(reloadX,reloadY)),
               pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "left_reload1.png")).convert_alpha(),(reloadX,reloadY)),
               pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "left_reload2.png")).convert_alpha(),(reloadX,reloadY)),
               pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "left_reload2.png")).convert_alpha(),(reloadX,reloadY)),
               pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "left_reload3.png")).convert_alpha(),(reloadX,reloadY)),
               pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "left_reload3.png")).convert_alpha(),(reloadX,reloadY)),
               pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "left_reload4.png")).convert_alpha(),(reloadX,reloadY)),
               pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "left_reload4.png")).convert_alpha(),(reloadX,reloadY)),
               pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "left_reload5.png")).convert_alpha(),(reloadX,reloadY)),
               pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "left_reload5.png")).convert_alpha(),(reloadX,reloadY)),
               pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "left_reload6.png")).convert_alpha(),(reloadX,reloadY)),
               pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "left_reload6.png")).convert_alpha(),(reloadX,reloadY)),
               pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "left_reload7.png")).convert_alpha(),(reloadX,reloadY)),
               pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "left_reload7.png")).convert_alpha(),(reloadX,reloadY)),
               pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "left_reload8.png")).convert_alpha(),(reloadX,reloadY)),
               pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "left_reload8.png")).convert_alpha(),(reloadX,reloadY))
            ]

reload_right = [pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "right_reload1.png")).convert_alpha(),(reloadX,reloadY)),
                pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "right_reload1.png")).convert_alpha(),(reloadX,reloadY)),
                pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "right_reload2.png")).convert_alpha(),(reloadX,reloadY)),
                pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "right_reload2.png")).convert_alpha(),(reloadX,reloadY)),
                pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "right_reload3.png")).convert_alpha(),(reloadX,reloadY)),
                pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "right_reload3.png")).convert_alpha(),(reloadX,reloadY)),
                pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "right_reload4.png")).convert_alpha(),(reloadX,reloadY)),
                pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "right_reload4.png")).convert_alpha(),(reloadX,reloadY)),
                pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "right_reload5.png")).convert_alpha(),(reloadX,reloadY)),
                pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "right_reload5.png")).convert_alpha(),(reloadX,reloadY)),
                pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "right_reload6.png")).convert_alpha(),(reloadX,reloadY)),
                pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "right_reload6.png")).convert_alpha(),(reloadX,reloadY)),
                pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "right_reload7.png")).convert_alpha(),(reloadX,reloadY)),
                pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "right_reload7.png")).convert_alpha(),(reloadX,reloadY)),
                pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "right_reload8.png")).convert_alpha(),(reloadX,reloadY)),
                pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "right_reload8.png")).convert_alpha(),(reloadX,reloadY))
                ]

Crouch_right = pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "Crouch_right.png")).convert_alpha(),(crouch_slideX,crouch_slideY))
Crouch_left = pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "Crouch_left.png")).convert_alpha(),(crouch_slideX,crouch_slideY))
SH_crouch_right = pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "Shield_crouch_right.png")).convert_alpha(),(crouch_slideX,crouch_slideY))
SH_crouch_left = pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "Shield_crouch_left.png")).convert_alpha(), (crouch_slideX,crouch_slideY))

Slide_right = pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "Slide_right.png")).convert_alpha(),(crouch_slideX,crouch_slideY))
Slide_left = pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "Slide_left.png")).convert_alpha(),(crouch_slideX,crouch_slideY))
SH_slide_right = pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "Shield_slide_right.png")).convert_alpha(),(crouch_slideX,crouch_slideY))
SH_slide_left = pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "Shield_slide_left.png")).convert_alpha(), (crouch_slideX,crouch_slideY))


enemy_left = [pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "Enemy_left.png")).convert_alpha(), (enemyX, enemyY)),
              pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "Enemyleft_death1.png")).convert_alpha(), (enemyX, enemyY)),
              pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "Enemyleft_death2.png")).convert_alpha(), (enemyX, enemyY)),
              pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "Enemyleft_death3.png")).convert_alpha(), (enemyX, enemyY)),
              pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "Enemyleft_death4.png")).convert_alpha(), (enemyX, enemyY)),
              ]
enemy_right = [pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "Enemy_right.png")).convert_alpha(), (enemyX, enemyY)),
              pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "Enemyright_death1.png")).convert_alpha(), (enemyX, enemyY)),
              pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "Enemyright_death2.png")).convert_alpha(), (enemyX, enemyY)),
              pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "Enemyright_death3.png")).convert_alpha(), (enemyX, enemyY)),
              pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "Enemyright_death4.png")).convert_alpha(), (enemyX, enemyY)),
              ]
cannon_imgV = pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "CannonV.png")).convert_alpha(), (cannonY, cannonX))
cannon_imgH = pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "CannonH.png")).convert_alpha(), (cannonX, cannonY))

cannon_ball = pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "CannonBall.png")).convert_alpha(), (cannonBallXY, cannonBallXY))

BG = pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "Background.png")).convert(), (SC_width, SC_height))
Menu = [pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "Menu1.png")).convert_alpha(),(SC_width,SC_height)),
        pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "Menu2.png")).convert_alpha(),(SC_width,SC_height)),
        pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "Menu3.png")).convert_alpha(),(SC_width,SC_height))
        ]
OptionsMenu = pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "OptionsMenu.png")).convert(), (SC_width, SC_height))
LoadingScreen = pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "LoadingScreen.png")).convert(),(SC_width, SC_height))

DeathScreen = [pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "blood1.png")).convert_alpha(),(SC_width, SC_height)),
               pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "blood2.png")).convert_alpha(),(SC_width, SC_height)),
               pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "blood3.png")).convert_alpha(),(SC_width, SC_height)),
               pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "blood4.png")).convert_alpha(),(SC_width, SC_height)),
               pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "blood5.png")).convert_alpha(),(SC_width, SC_height)),
               pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "DeathScreen.png")).convert_alpha(),(SC_width, SC_height))
               ]
ControlsInfo = pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "ControlsInfo.png")).convert(),(SC_width, SC_height))
InfoScreen = pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "InfoScreen.png")).convert(),(SC_width, SC_height))

ScreenTransition1 = [pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "SCTransition1.png")).convert_alpha(), (SC_width, SC_height)),
                pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "SCTransition2.png")).convert_alpha(), (SC_width, SC_height)),
                pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "SCTransition3.png")).convert_alpha(), (SC_width, SC_height)),
                pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "SCTransition4.png")).convert_alpha(), (SC_width, SC_height)),
                pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "SCTransition5.png")).convert_alpha(), (SC_width, SC_height)),
                pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "SCTransition6.png")).convert_alpha(), (SC_width, SC_height)),
                pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "SCTransition7.png")).convert_alpha(), (SC_width, SC_height)),
                pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "SCTransition8.png")).convert_alpha(), (SC_width, SC_height))
                ]

HealingItem = pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "Healing_Item.png")).convert_alpha(), (50, 35))

HealingProcess = [pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "Healing1.png")).convert_alpha(), (SC_width, SC_height)),
                  pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "Healing2.png")).convert_alpha(), (SC_width, SC_height)),
                  pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "Healing3.png")).convert_alpha(), (SC_width, SC_height)),
                  pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "Healing4.png")).convert_alpha(), (SC_width, SC_height)),
                  pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "Healing5.png")).convert_alpha(), (SC_width, SC_height)),
                  pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "Healing6.png")).convert_alpha(), (SC_width, SC_height)),
                  pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "Healing7.png")).convert_alpha(), (SC_width, SC_height)),
                  ]

BulletShield = pygame.transform.scale(pygame.image.load(os.path.join("MainGame images", "BulletShield.png")).convert_alpha(), (35, 35))

GunShot = pygame.mixer.Sound(os.path.join("MainGame sounds", "GunShot.wav"))
Reload = pygame.mixer.Sound(os.path.join("MainGame sounds", "Reload.wav"))
Kill = pygame.mixer.Sound(os.path.join("MainGame sounds", "EnemyDeath.wav"))
Death = pygame.mixer.Sound(os.path.join("MainGame sounds", "PlayerDeath.wav"))
Shotgun = pygame.mixer.Sound(os.path.join("MainGame sounds", "Shotgun.wav"))
Healing = pygame.mixer.Sound(os.path.join("MainGame sounds", "Healing.wav"))
Shielding = pygame.mixer.Sound(os.path.join("MainGame sounds", "Shielding.wav"))

# Define classes
def main():
    crouch = False
    show_hitbox = False
    time = 0
    enemyAppearRate = 100
    bloodIndex = 0
    healthIndex = 0
    once = False

    class MainCharacter:

        def __init__(self, x, y):

            # Walking
            self.x = x
            self.y = y
            self.xvel = 10
            self.yvel = 10
            self.face_right = True
            self.face_left = False
            self.stepIndex = 0
            self.stay = False
            self.run = False

            #Slide
            self.time = 0
            self.slideReady = False
            self.slide = False
            self.distance = 0
            self.slideVel = 15

            # Jump
            self.jump = False

            # Bullets and reload
            self.bullets = []
            self.cooldown_count = 0
            self.cooldown_count2 = 0
            self.bulletAD = 0
            self.bulletAD2 =0
            self.mag = mag_size
            self.reload = False
            self.reloadIndex = 0
            self.rifle = True
            self.shotgun = False
            self.Bdistance = 0

            #Health
            self.health = 15
            self.lives = 1
            self.alive = True
            self.healing = False

            #Hitbox
            self.hitbox = (self.x, self.y, 64, 64)
            self.HB_AD = 0
            self.HB_AD2 = 0

            #shield
            self.shield= (self.x,self.y,64,64)
            self.inmune = False

            #enemy
            self.score = 0

        def move_MC(self, key):
            # Move left and Right
            if self.slide == False:
                if key[pygame.K_d] and crouch == True:
                    self.face_right = True
                    self.face_left = False
                if key[pygame.K_a] and crouch == True:
                    self.face_right = False
                    self.face_left = True

                if key[pygame.K_d] and self.x <= SC_width - 43 and crouch == False:
                    self.x += self.xvel
                    self.face_left = False
                    self.face_right = True
                    self.stay = False
                elif key[pygame.K_a] and self.x >= 0 and crouch == False:
                    self.x -= self.xvel
                    self.face_right = False
                    self.face_left = True
                    self.stay = False

                else:
                    self.stay = True

                if self.y > player_y:
                    self.y = player_y

            if self.slide == True:
                if self.face_right is True and self.x <= SC_width - 43:
                    self.x += self.slideVel
                if self.face_left is True and self.x >= 0:
                    self.x -= self.slideVel

        def drawMC(self, SC):
            # character
            if self.inmune == False:
                if self.slide == False:
                    if self.stepIndex >= 3:
                        self.stepIndex = 0
                    if crouch == False:
                        if self.stay == True and self.reload == False:
                            if self.face_right == True:
                                SC.blit(still,(self.x,self.y))
                            if self.face_left == True:
                                SC.blit(still2,(self.x,self.y))

                        if self.stay == False:
                            if self.face_left == True:
                                SC.blit(left[self.stepIndex], (self.x, self.y))
                                self.stepIndex += 1
                            if self.face_right == True:
                                SC.blit(right[self.stepIndex], (self.x, self.y))
                                self.stepIndex += 1

                    if crouch == True:
                        if self.stay == True:
                            if self.face_right == True:
                                SC.blit(Crouch_right,(self.x,self.y + 20))
                            if self.face_left == True:
                                SC.blit(Crouch_left, (self.x, self.y + 20))

                if self.slide == True:
                    if player.face_right is True:
                        SC.blit(Slide_right,(self.x,self.y + 20))
                    if player.face_left is True:
                        SC.blit(Slide_left,(self.x,self.y + 20))

                #Reload
                if self.stay == True and self.reload == True and crouch == False:
                    self.reloadIndex += 1
                    if self.reloadIndex >= 16:
                        self.reloadIndex = 0
                        self.mag = mag_size
                        self.reload = False
                    if self.face_right is True:
                        SC.blit(reload_right[self.reloadIndex],(self.x,self.y))
                    if self.face_left is True:
                        SC.blit(reload_left[self.reloadIndex],(self.x,self.y))
                if self.stay == False or crouch == True:
                    self.reload = False
                    self.reloadIndex = 0

            # hitbox
            if crouch == False:
                self.HB_AD = 0
                self.HB_AD2 = 60
            if crouch == True or self.slide == True:
                self.HB_AD = 20
                self.HB_AD2 = 40

            self.hitbox = (self.x + 10, self.y + self.HB_AD + 5, 30, self.HB_AD2)
            if show_hitbox == True:
                pygame.draw.rect(SC, (black), self.hitbox, 1)

            # Shield
            self.shield = (self.x + 10, self.y + 5, 35, 65)
            if self.inmune == True:
                if self.slide == False:
                    if self.stepIndex >= 3:
                        self.stepIndex = 0
                    if crouch == False:
                        if self.stay == True:
                            if self.face_right == True:
                                SC.blit(shield_still, (self.x, self.y))
                            if self.face_left == True:
                                SC.blit(shield_still2, (self.x, self.y))

                        if self.stay == False:
                            if self.face_left == True:
                                SC.blit(Shield_left[self.stepIndex], (self.x, self.y))
                                self.stepIndex += 1
                            if self.face_right == True:
                                SC.blit(Shield_right[self.stepIndex], (self.x, self.y))
                                self.stepIndex += 1

                    if crouch == True:
                        if self.stay == True:
                            if self.face_right == True:
                                SC.blit(SH_crouch_right, (self.x, self.y + 20))
                            if self.face_left == True:
                                SC.blit(SH_crouch_left, (self.x, self.y + 20))

                if self.slide == True:
                    if player.face_right is True:
                        SC.blit(SH_slide_right, (self.x, self.y + 20))
                    if player.face_left is True:
                        SC.blit(SH_slide_left, (self.x, self.y + 20))

        def slide_motion(self):
            if self.stay is True:
                self.time = 0
            if self.stay is False:
                self.time += 1
            if self.time >= 10:
                self.slideReady = True
            if self.time < 10:
                self.slideReady = False

            if self.slide == False:
                self.distance = 0
                self.slideVel = 15
            if self.slide == True:
                self.distance += 1
            if self.distance >= 10:
                self.slideVel -= 1
            if self.slideVel <= 0:
                self.slide = False

        def jump_motion(self, key):
            if self.jump is False and key[pygame.K_SPACE] and crouch == False and self.slide == False:
                self.jump = True
            if self.jump is True:
                self.y -= self.yvel * 3.5
                self.yvel -= 2
            if self.yvel < -10:
                self.jump = False
                self.yvel = 10

        def direction(self):
            if self.face_right == True:
                return 1
            if self.face_left:
                return -1

        def cooldown(self):
            if self.rifle == True:
                if self.cooldown_count >= 5:
                    self.cooldown_count = 0
                elif self.cooldown_count > 0:
                    self.cooldown_count += 1
            if self.shotgun == True:
                if self.cooldown_count >= 10:
                    self.cooldown_count = 0
                elif self.cooldown_count > 0:
                    self.cooldown_count += 1

        def shoot(self):
            self.hit()
            self.cooldown()
            if self.face_right == True:
                self.bulletAD = 7
            if self.face_left == True:
                self.bulletAD = 0
            if crouch == False or self.slide == False:
                self.bulletAD2 = 11
            if crouch == True:
                self.bulletAD2 = 20
            if self.slide == True:
                self.bulletAD2 = 15

            if self.rifle == True:
                if (key[pygame.K_p] and self.cooldown_count == 0):
                    if self.mag > 0:
                        if self.inmune is False:
                            bullet = Bullet.RifleWeapon(self.x + self.bulletAD, self.y + self.bulletAD2, self.direction())
                            self.bullets.append(bullet)
                            GunShot.play()
                            self.mag -= 1
                            self.cooldown_count = 1
                        if self.inmune is True:
                            bullet = Bullet.RifleWeapon(self.x + self.bulletAD, self.y + self.bulletAD2, self.direction())
                            self.bullets.append(bullet)
                            GunShot.play()
                            self.cooldown_count = 1

            elif self.shotgun == True:
                if (key[pygame.K_p] and self.cooldown_count == 0):
                    if self.inmune is False:
                        cartridge1 = Bullet.cartridge1(self.x + self.bulletAD, self.y + self.bulletAD2, self.direction())
                        cartridge2 = Bullet.cartridge2(self.x + self.bulletAD, self.y + self.bulletAD2, self.direction())
                        cartridge3 = Bullet.cartridge3(self.x + self.bulletAD, self.y + self.bulletAD2, self.direction())
                        if self.mag >= 3:
                            self.bullets.append(cartridge1)
                            self.bullets.append(cartridge2)
                            self.bullets.append(cartridge3)
                            Shotgun.play()
                            self.mag -= 3
                            self.cooldown_count = 1
                        elif self.mag == 2:
                            self.bullets.append(cartridge1)
                            self.bullets.append(cartridge2)
                            Shotgun.play()
                            self.mag -= 2
                            self.cooldown_count = 1
                        elif self.mag == 1:
                            self.bullets.append(cartridge1)
                            Shotgun.play()
                            self.mag -= 1
                            self.cooldown_count = 1
                    if self.inmune is True:
                        cartridge1 = Bullet.cartridge1(self.x + self.bulletAD, self.y + self.bulletAD2, self.direction())
                        cartridge2 = Bullet.cartridge2(self.x + self.bulletAD, self.y + self.bulletAD2, self.direction())
                        cartridge3 = Bullet.cartridge3(self.x + self.bulletAD, self.y + self.bulletAD2, self.direction())
                        self.bullets.append(cartridge1)
                        self.bullets.append(cartridge2)
                        self.bullets.append(cartridge3)
                        Shotgun.play()
                        self.cooldown_count = 1
            for bullet in self.bullets:
                bullet.move()
                if bullet.off_screen():
                    self.bullets.remove(bullet)
            if self.mag <= 0:
                if self.inmune is True:
                    self.mag = mag_size
                    Reload.play()

        def hit(self):
            for enemy in enemies:
                if self.rifle == True:
                    for bullet in self.bullets:
                        if enemy.hitbox[0] < bullet.x < enemy.hitbox[0] + enemy.hitbox[2] and enemy.hitbox[1] < bullet.y < \
                                enemy.hitbox[1] + enemy.hitbox[3]:
                            if enemy.health > 0:
                                enemy.health -= 5
                            player.bullets.remove(bullet)
                    if enemy.health <= 0:
                        enemy.deathIndex += 1
                        if enemy.deathIndex >= 5:
                            enemies.remove(enemy)
                            Kill.play()
                            self.score += 1
                if self.shotgun == True:
                    for cartridge1 in self.bullets:
                        if enemy.hitbox[0] < cartridge1.x < enemy.hitbox[0] + enemy.hitbox[2] and enemy.hitbox[1] < cartridge1.y < \
                                enemy.hitbox[1] + enemy.hitbox[3]:
                            if enemy.health > 0:
                                enemy.health -= 5
                            player.bullets.remove(cartridge1)

                    for cartridge2 in self.bullets:
                        if enemy.hitbox[0] < cartridge2.x < enemy.hitbox[0] + enemy.hitbox[2] and enemy.hitbox[1] < cartridge2.y < \
                                enemy.hitbox[1] + enemy.hitbox[3]:
                            if enemy.health > 0:
                                enemy.health -= 5
                            player.bullets.remove(cartridge2)

                    for cartridge3 in self.bullets:
                        if enemy.hitbox[0] < cartridge3.x < enemy.hitbox[0] + enemy.hitbox[2] and enemy.hitbox[1] < cartridge3.y < \
                                enemy.hitbox[1] + enemy.hitbox[3]:
                            if enemy.health > 0:
                                enemy.health -= 5
                            player.bullets.remove(cartridge3)

                    if enemy.health <= 0:
                        enemy.deathIndex += 1
                        if enemy.deathIndex >= 5:
                            enemies.remove(enemy)
                            Kill.play()
                            self.score += 1

            for shield in powerup:
                if player.hitbox[0] < shield.x + 30 < player.hitbox[0] + shield.hitbox[2] and player.hitbox[1] < shield.y < player.hitbox[1] + shield.hitbox[3]:
                    shield.collision = True
                    Shielding.play()
                    self.inmune = True

            for health in Medkit:
                if player.hitbox[0] < health.x + 25 < player.hitbox [0] + health.hitbox[2] and player.hitbox[1] < health.y < player.hitbox[1] + health.hitbox[3]:
                    health.collision = True
                    self.healing = True
                    Healing.play()
                    if self.health < 12:
                        self.health += 3
                    if self.health >= 12:
                        self.health = 15

            if player.hitbox[0] < cannonH.x + 50 < player.hitbox[0] + player.hitbox[2] and player.hitbox[1] < cannonH.y + 50 < \
                    player.hitbox[1] + player.hitbox[3]:
                if player.health > 0:
                    player.health -= 15
                if player.health <= 0:
                    player.alive = False
            if player.hitbox[0] < cannonH.x + 20 < player.hitbox[0] + player.hitbox[2] and player.hitbox[1] < cannonH.y + 15 < \
                    player.hitbox[1] + player.hitbox[3]:
                if player.health > 0:
                    player.health -= 3
                if player.health <= 0:
                    player.alive = False

    class Bullet:
        class RifleWeapon:
            def __init__(self,x,y,direction):
                self.x = x + 10
                self.y = y + 15
                self.direction = direction
            def draw_bullet(self):
                SC.blit(bulletImg, (self.x, self.y))

            def move(self):
                if self.direction == 1:
                    self.x += 20

                if self.direction == -1:
                    self.x -= 20

            def off_screen(self):
                return not (self.x >= 0 and self.x <= SC_width)

        class cartridge1:
            def __init__(self, x, y, direction):
                self.x = x + 10
                self.y = y + 15
                self.direction = direction

            def draw_bullet(self):
                SC.blit(bulletImg, (self.x, self.y))

            def move(self):
                if self.direction == 1:
                    self.x += 20

                if self.direction == -1:
                    self.x -= 20

            def off_screen(self):
                return not (self.x >= 0 and self.x <= SC_width)

        class cartridge2:
            def __init__(self,x, y, direction):
                self.x = x + 10
                self.y = y + 15
                self.direction = direction
            def draw_bullet(self):
                SC.blit(bulletImg, (self.x, self.y))

            def move(self):
                if self.direction == 1:
                    self.x += 20
                    self.y += 2

                if self.direction == -1:
                    self.x -= 20
                    self.y += 2

            def off_screen(self):
                return not (self.x >= 0 and self.x <= SC_width)

        class cartridge3:
            def __init__(self, x, y, direction):
                self.x = x + 10
                self.y = y + 15
                self.direction = direction

            def draw_bullet(self):
                SC.blit(bulletImg, (self.x, self.y))

            def move(self):
                if self.direction == 1:
                    self.x += 20
                    self.y -= 1

                if self.direction == -1:
                    self.x -= 20
                    self.y -= 2

            def off_screen(self):
                return not (self.x >= 0 and self.x <= SC_width)

    class Enemy:
        def __init__(self, x, y, direction):
            # Movement
            self.x = x
            self.y = y
            self.direction = direction
            self.deathIndex = 0
            # Health
            self.hitbox = (self.x, self.y, 64, 64)
            self.hitbox_adjustment = 5
            if self.direction == left:
                self.hitbox_adjustment = 0
            self.health = 15
            self.cooldown = 0

        def draw(self, SC):
            if enemiesOn == True:
                # hitbox
                self.hitbox = (self.x + 25, self.y + 5, 30, 60)
                if show_hitbox == True:
                    pygame.draw.rect(SC, (black), self.hitbox, 1)
                # health bar
                pygame.draw.rect(SC, (red), (self.x + 15, self.y, 30, 10))
                if self.health > 0:
                    pygame.draw.rect(SC, (green), (self.x + 15, self.y, self.health * 2, 10))
                # draw enemy
                if self.direction == left:
                    SC.blit(enemy_left[self.deathIndex], (self.x, self.y))
                if self.direction == right:
                    SC.blit(enemy_right[self.deathIndex], (self.x, self.y))

        def move(self):
            if enemiesOn == True:
                if self.direction == left:
                    self.x -= 3
                if self.direction == right:
                    self.x += 3

        def offscreen(self):
            self.hit()
            return not (self.x >= -50 and self.x <= SC_width + 50)

        def hit(self):
            if enemiesOn == True:
                if player.hitbox[0] < enemy.x + 32 < player.hitbox[0] + player.hitbox[2] and player.hitbox[1] < enemy.y + 32 < \
                        player.hitbox[1] + player.hitbox[3]:
                    if player.inmune == False:
                        if player.health > 0:
                            player.health -= 1
                        if player.health <= 0:
                            player.alive = False

    class Powerup:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.collision = False

        def draw(self,SC):
            self.hitbox = (self.x, self.y, 40, 35)
            SC.blit(shieldImg,(self.x,self.y))

        def movement(self):
            if self.y < shield_boundary + 30:
                self.y += 3

    class HealthPowerup:
        def __init__(self, x, y):
            self.x  = x
            self.y = y
            self.collision = False

        def draw(self,SC):
            self.hitbox = (self.x, self.y, 50, 35)
            SC.blit(HealingItem, (self.x, self.y))

        def movement(self):
            if self.y < 290 + 30:
                self.y += 3

    class Cannon1:
        def __init__(self,x,y):
            self.x= x
            self.y= y
            self.xvel= 3
            self.yvel= 2
            self.CB=[]
            self.CC = 0
            self.right = True
            self.left = False
            self.adjustment = 0


        def cooldown(self):
            if player.score < 30:
                if self.CC >= 30:
                    self.CC = 0

                elif self.CC > 30:
                    self.CC += 1

            if player.score > 1:
                if self.CC >= 15:
                    self.CC = 0
                elif self.CC > 0:
                    self.CC += 1

        def move(self):
            self.x += self.xvel
            if self.x + 60 > SC_width:
                self.xvel *= -1
                self.left = True
                self.right = False
            if self.x < 0:
                self.xvel *= -1
                self.right = True
                self.left = False

        def draw(self,SC):
            SC.blit(cannon_imgV, (self.x, self.y))
            if self.right == True:
                self.adjustment = 10

            if self.left == True:
                self.adjustment = 0

        def shoot(self):
            self.cooldown()
            if self.CC == 0:
                ball = Cannon_ball_vertical(self.x + self.adjustment, self.y)
                self.CB.append(ball)
                self.CC = 1
            for ball in self.CB:
                ball.move()
                if ball.y > 290 + 45:
                    self.CB.remove(ball)

            #HIT
            for ball in self.CB:
                if player.hitbox[0] < ball.x + 25 < player.hitbox[0] + player.hitbox[2] and player.hitbox[1] < ball.y + 50 < player.hitbox[1] + player.hitbox[3]:
                    if player.inmune == False:
                        if player.health > 0:
                            player.health -= projectile_damage
                        if player.health <= 0:
                            player.alive = False

                        self.CB.remove(ball)

    class Cannon2:
        def __init__(self,x,y):
            self.x= x
            self.y= y
            self.xvel= 3
            self.yvel= 2
            self.CB=[]
            self.CC = 0

        def cooldown(self):
            if player.score < 30:
                if self.CC >= 30:
                    self.CC = 0

                elif self.CC > 0:
                    self.CC += 1

            if player.score > 30:
                if self.CC >= 15:
                    self.CC = 0
                elif self.CC > 0:
                    self.CC += 1

        def move(self):
            self.y += self.yvel
            if self.y + 50 > CN2_boundaryBottom:
                self.yvel *= -1
            if self.y < CN2_boundaryTop:
                self.yvel *= -1

        def draw(self,SC):
            SC.blit(cannon_imgH, (self.x, self.y))

        def shoot(self):
            self.cooldown()
            if self.CC == 0:
                ball = Cannon_ball_right(self.x - 35, self.y)
                self.CB.append(ball)
                self.CC = 1
            for ball in self.CB:
                ball.move()
                if ball.x <= 0:
                    self.CB.remove(ball)

            #HIT
            for ball in self.CB:
                if player.hitbox[0] < ball.x < player.hitbox[0] + player.hitbox[2] and player.hitbox[1] < ball.y + 25 < player.hitbox[1] + player.hitbox[3]:
                    if player.inmune == False:
                        if player.health > 0:
                            player.health -= projectile_damage
                        if player.health <= 0:
                            player.alive = False

                        self.CB.remove(ball)

    class Cannon_ball_vertical:
        def __init__(self,x,y):
            self.x= x + 12
            self.y= y + 45

        def draw(self):
            SC.blit(cannon_ball, (self.x,self.y))

        def move(self):
            self.y += 20

    class Cannon_ball_right:
        def __init__(self,x,y):
            self.x= x + 45
            self.y= y + 12

        def draw(self):
            SC.blit(cannon_ball, (self.x,self.y))

        def move(self):
            self.x -= 20

    def draw():
        # Draw screen
        global enemy, shield, randNB, health
        SC.fill(white)
        SC.blit(BG,(0,0))

        #Draw player
        player.drawMC(SC)

        # Draw bullets
        for bullet in player.bullets:
            bullet.draw_bullet()

        #Draw Enemies
        for enemy in enemies:
            enemy.draw(SC)

        #Draw Powerup
        for shield in powerup:
            shield.draw(SC)

        for health in Medkit:
            health.draw(SC)

        #Draw Ball
        for ball in cannonV.CB:
            ball.draw()
        for ball in cannonH.CB:
            ball.draw()

        # Draw Cannon
        cannonV.draw(SC)
        cannonH.draw(SC)

        # Draw "Score" on screen
        font = pygame.font.SysFont("arial", 32)
        score_text = font.render('Score:' + str(player.score), True, white)
        SC.blit(score_text, (650, 520))

        #Draw "Mag" on screen
        mag_text = font.render('Mag:' + str(player.mag), True, white)
        SC.blit(mag_text,(650,552))

        #Draw "Slide" on screen
        slide_text = font.render('Slide',True,white)
        SC.blit(slide_text,(60,520))
        if player.slideReady is False:
            pygame.draw.circle(SC,red,[30,535],20,0)
        if player.slideReady is True:
            pygame.draw.circle(SC,green,[30,535],20,0)
        pygame.draw.circle(SC,gray,[30,535],20,3)

        #Draw Health Bar on screen
        pygame.draw.rect(SC,red,(250,523,300,26 ))
        if player.health >= 0:
            pygame.draw.rect(SC,green,(250,520,player.health * 20,30))
        if player.inmune is True:
            SC.blit(shielded_HB,(250,520))
            SC.blit(BulletShield, (728, 552))

        #Draw weapon used on screen
        weapon_text1 = font.render('Shotgun', True, white)
        weapon_text2 = font.render('Rifle', True, white)

        if player.shotgun == True:
            SC.blit(weapon_text1, (350, 560))
        elif player.rifle == True:
            SC.blit(weapon_text2, (350, 560))

        #Draw Healing process on Screen
        if player.healing == True:
            SC.blit(HealingProcess[healthIndex], (0, 0))

        # Draw game over screen
        if player.alive == False:
            SC.blit(DeathScreen[bloodIndex], (0, 0))
            player.x = 150
            player.y = 390

            # Reset
            if key[pygame.K_f]:
                player.x = player_x
                player.y = player_y
                player.mag = mag_size
                player.alive = True
                player.face_right = True
                player.inmune = False

                if enemiesOn == True:
                    enemies.clear()
                if len(powerup) == 1:
                    powerup.remove(shield)

                if len(Medkit) == 1:
                    Medkit.remove(health)
                cannonV.x = cannonV_X
                cannonH.y = cannonH_Y
                player.health = 15
                player.score = 0

        # Delay and Update
        pygame.display.update()
        clock.tick(30)

    # Instance of MC class
    player = MainCharacter(player_x, player_y)
    # Instance of enemy class
    enemies = []
    #Instance of powerup class
    powerup= []
    Medkit = []
    #Instance of cannon class
    cannonV = Cannon1(cannonV_X, cannonV_Y)
    cannonH = Cannon2(cannonH_X, cannonH_Y)

    run = True
    while run == True:
        # Quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    menu()

            #pause
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m and player.alive == True:
                    pause()

            #hitbox
                if event.key == pygame.K_h:
                    show_hitbox = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_h:
                    show_hitbox = False

            #Reload
                if event.key == pygame.K_r and player.inmune == False:
                    if player.mag < mag_size:
                        player.reload = True
                        Reload.play()

            #Crouch and Slide
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_l and player.slideReady == True:
                    player.slide = True
                if event.key == pygame.K_s:
                    crouch = True
                    player.stay = True


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_l:
                    if player.slide is True:
                        player.slide = False
                        player.time = 0
                if event.key == pygame.K_s:
                    crouch = False
                    player.stay = False

            #Change weapon
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    player.rifle = True
                    player.shotgun = False
                if event.key == pygame.K_2:
                    player.shotgun = True
                    player.rifle = False

        #Death Sound
        if once == False and player.alive == False:
            Death.play()
            once = True


        # Keys
        key = pygame.key.get_pressed()

        # Shoot
        player.shoot()
        cannonV.shoot()
        cannonH.shoot()

        # Enemy
        if player.score > 10 and player.score < 20:
            enemyAppearRate = 75
        if player.score > 20 and player.score < 40:
            enemyAppearRate = 60
        elif player.score > 40:
            enemyAppearRate = 50

        enemiesAppear = random.randint(0, enemyAppearRate)

        if enemiesAppear  == 1:
            randNb = random.randint(0, 1)
            if randNb == 1:
                enemy = Enemy(enemyLeft_x, enemyLeft_Y, left)
                enemies.append(enemy)

            if randNb == 0:
                enemy = Enemy(enemyRight_X, enemyRight_Y, right)
                enemies.append(enemy)
        for enemy in enemies:
            enemy.move()
            if enemy.offscreen():
                enemies.remove(enemy)
            if enemiesOn == False:
                enemies.remove(enemy)

            # clock
        if player.inmune == True:
            time += 1
            if time > 100:
                player.inmune = False
                time = 0

        #powerup
        if len(powerup) == 0:
            randNb = random.randint(0, 200)
            if randNb == 1 and player.inmune == False:
                shield = Powerup(random.randint(0,SC_width - 60),0)
                powerup.append(shield)

        for shield in powerup:
            shield.movement()
            if shield.collision==True:
                powerup.remove(shield)
                shield.collision = False

        if len(Medkit) == 0:
            randNB = random.randint(0, 200)
            if randNB == 1 and player.health < 15:
                health = HealthPowerup(random.randint(0, SC_width - 50), 0)
                Medkit.append(health)

        for health in Medkit:
            health.movement()
            if health.collision == True:
                Medkit.remove(health)
                health.collision = False

        #Blood Animation
        if bloodIndex < 5 and player.alive == False:
            bloodIndex += 1
        if player.alive == True:
            bloodIndex = 0

        if healthIndex < 7 and player.healing == True:
            healthIndex += 1
        if healthIndex >= 7:
            healthIndex = 0
            player.healing = False

        # Movement
        player.slide_motion()
        player.move_MC(key)
        cannonV.move()
        cannonH.move()
        player.jump_motion(key)

        # Draw
        draw()

def pause():
    loop = 1

    font = pygame.font.Font('freesansbold.ttf', 150)
    Pause_text = font.render('Paused', True, black)
    SC.blit(Pause_text, (150, 200))
    
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    loop = 0

        pygame.display.update()
        clock.tick(60)

def ScreenChangeClosing():
    screenIndex = 0

    run = True
    while run:
        screenIndex += 1

        if screenIndex >= 7:
            run = False

        SC.blit(ScreenTransition1[screenIndex], (0, 0))
        pygame.display.update()
        clock.tick(35)

def menu():
    menuIndex = 0
    pygame.mixer.music.load(os.path.join("MainGame sounds", "MenuMusic2.wav"))
    if Music == True:
        pygame.mixer.music.play(-1)
    def screen():
        #Draw Menu
        SC.fill(white)
        SC.blit(Menu[menuIndex], (0, 0))
        #Sound
        # Delay and Update
        pygame.display.update()
        clock.tick(10)
    run= True
    while run == True:
        menuIndex += 1
        if menuIndex >= 3:
            menuIndex = 0
        screen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    loadscreen()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_o:
                    ScreenChangeClosing()
                    options()

def loadscreen():
    loadingbar = 0
    def loading():
        #Draw Menu
        SC.fill(black)
        SC.blit(LoadingScreen,(0, 0))
        #Loading Bar
        pygame.draw.rect(SC, green, (0, 550, loadingbar, 50))

        # Delay and Update
        pygame.display.update()
        clock.tick(60)

    run = True
    while run == True:
        loading()
        if loadingbar < SC_width:
            loadingbar += 2
        if loadingbar >= SC_width:
            run = False
            main()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run = False
                    main()

def options():

    global Music

    def optionMenu():
        #Draw Menu
        SC.fill(black)
        SC.blit(OptionsMenu,(0,0))
        # Delay and Update
        pygame.display.update()
        clock.tick(15)

    run = True
    while run == True:
        optionMenu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    ScreenChangeClosing()
                    menu()
                if event.key == pygame.K_o:
                    run = False
                    ScreenChangeClosing()
                    menu()
                if event.key == pygame.K_c:
                    ScreenChangeClosing()
                    ControlInfo()
                if event.key == pygame.K_i:
                    ScreenChangeClosing()
                    Info()
                if event.key == pygame.K_m:
                    if Music == False:
                        pygame.mixer.music.load(os.path.join("MainGame sounds", "MenuMusic2.wav"))
                        pygame.mixer.music.play(-1)
                        Music = True
                    elif Music == True:
                        pygame.mixer.music.stop()
                        Music = False

def ControlInfo():
    def MainScreen():
        #Draw Menu
        SC.fill(black)
        SC.blit(ControlsInfo,(0, 0))
        # Delay and Update
        pygame.display.update()
        clock.tick(60)

    run = True
    while run == True:
        MainScreen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    ScreenChangeClosing()
                    run = False

def Info():
    def MainScreen2():
        #Draw Menu
        SC.fill(black)
        SC.blit(InfoScreen,(0, 0))
        # Delay and Update
        pygame.display.update()
        clock.tick(60)

    run = True
    while run == True:
        MainScreen2()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    ScreenChangeClosing()
                    run = False

menu()

