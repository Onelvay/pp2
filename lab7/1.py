import pygame
import datetime
pygame.init()

def blitRotate(surf, image, pos, originPos, angle):
    image_rect = image.get_rect(topleft = (pos[0] - originPos[0], pos[1]-originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    
    rotated_offset = offset_center_to_pivot.rotate(-angle)

    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)

    surf.blit(rotated_image, rotated_image_rect)

clock = pygame.time.Clock()
screen=pygame.display.set_mode((1280,980))
working=True

hold = datetime.datetime.now()

now_minute=int(hold.strftime("%M"))

now_sec=int(hold.strftime("%S"))
count_sec=0

angle=0
sec_hand=pygame.image.load('C:\\pp2\\lab7\\mouse\\lefthand1.png')
sec_hand=pygame.transform.scale(sec_hand,(400,250))
image=pygame.image.load('C:\\pp2\\lab7\\mouse\\pict.png')
hand=pygame.image.load('C:\\pp2\\lab7\\mouse\\righthand1.png')
hand=pygame.transform.scale(hand,(450,300))

w,h=hand.get_size()
k,l=sec_hand.get_size()
pos = ((screen.get_width()/2), (screen.get_height()/2)-5)
sec_angle=0
print(now_minute)
print(now_sec)
black=(0,0,0)
count_min=0
while working:
    for i in pygame.event.get():
        if i.type== pygame.QUIT:
            working =False
    screen.fill(0)
    screen.blit(image,(0,0))
    blitRotate(screen, hand, pos, (w/2, h/2), angle)
    blitRotate(screen, sec_hand, pos, (k/2, l/2), sec_angle)
    pygame.draw.circle(screen,black,((screen.get_width()/2), (screen.get_height()/2)-13),16)
    if count_sec==0:
        angle-=((3*now_sec*1.2)+10)
        count_sec+=1
    else:
        angle -= 1.2
    if count_min==0:
        sec_angle-=((1.2*5*now_minute)+60)
        count_min=1
    else:
        sec_angle-=0.05
    pygame.display.flip()
    clock.tick(5)
