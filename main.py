import pygame

loop = True
janela = pygame.display.set_mode([800, 600])
pygame.display.set_caption("Primeiro Game")

#Carrega e redefine o tamanho da imagem
new_width, new_height = 100, 100
player = pygame.transform.scale(pygame.image.load("C:/Users/Yuri/Desktop/game/pngwing.com.png"), (new_width, new_height))

#Posição player
pos_x_player = 300
pos_y_player = 200
speed_player = 800

# Configura a taxa de quadros
clock = pygame.time.Clock()
fps = 60

while loop:
   
   for events in pygame.event.get():
      #Ao clicar no botao X fecha a janela
      if events.type==pygame.QUIT:
         loop=False
   
   # Obtém o tempo desde o último quadro
   delta_time = clock.tick(fps) / 1000  # delta_time em segundos

   #Captação das teclas precionadas
   teclas = pygame.key.get_pressed()

   # Movimentação do player
   if teclas[pygame.K_UP]:
      pos_y_player -= speed_player * delta_time
   if teclas[pygame.K_DOWN]:
      pos_y_player += speed_player * delta_time
   if teclas[pygame.K_LEFT]:
      pos_x_player -= speed_player * delta_time
   if teclas[pygame.K_RIGHT]:
      pos_x_player += speed_player * delta_time

   #Desenhando o fundo
   janela.fill((0, 0, 0))

   janela.blit(player, (pos_x_player, pos_y_player))

   pygame.display.update()

pygame.quit()