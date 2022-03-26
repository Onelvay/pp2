import pygame

pygame.init()
index=0
memory={
    0:'acolytewhat3.mp3',
    1:'arthasyes4.mp3',
    2:'druidoftheclawready1.mp3',
    3:'gruntherodies1.mp3',
    4:'gruntready1.mp3',
    5:'gryphonriderwhat5.mp3',
    6:'necromancernogold1.mp3',
    7:'peasantwhat3.mp3',
    8:'peonwhat4.mp3',
    9:'sorceresswhat4.mp3'
}

screen = pygame.display.set_mode((400, 300))
done = False

clock = pygame.time.Clock()
check=False

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_RIGHT:
                        if index<9:
                            index+=1
                            pygame.mixer.music.load('C:\\pp2\\lab7\\sounds\\'+memory[index])
                            pygame.mixer.music.play(0)
                    if event.key == pygame.K_LEFT:
                        if index!=0:
                            index-=1
                            pygame.mixer.music.load('C:\\pp2\\lab7\\sounds\\'+memory[index])
                            pygame.mixer.music.play(0)
                    if event.key == pygame.K_SPACE:
                 
                        pygame.mixer.music.pause()
                    if  event.key == pygame.K_TAB:
                      
                        pygame.mixer.music.unpause()
                        
pygame.exit()
