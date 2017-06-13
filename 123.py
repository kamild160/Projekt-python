import random, pygame, sys,time
from pygame.locals import *
from livewires import games, color


screen_width=800
screen_height=600
games.init(screen_width , screen_height , fps = 50)

global zegar_fps, mapa, czcionka
pygame.init()
pygame.display()
pygame.display.set_caption('Faling stars ')
gameDisplay=pygame.display.set_mode((screen_width , screen_height))
	







class Pan(games.Sprite):

    """

    kosz sterowana przez gracza służąca do łapania spadających pizz.

    """

    image = games.load_image("patelnia.bmp")



    def __init__(self):

        

        super(Pan, self).__init__(image = Pan.image,

                                  x = games.mouse.x,

                                  bottom = games.screen.height)

        

        self.score = games.Text(value = 0, size = 30, color = color.white,

                                top = 5, right = games.screen.width - 10)

        games.screen.add(self.score)



    def update(self):

        """ Zmień pozycję na wyznaczoną przez współrzędną x myszy. """

        self.x = games.mouse.x

        

        if self.left < 0:

            self.left = 0

            

        if self.right > games.screen.width:

            self.right = games.screen.width

            

        self.check_catch()



    def check_catch(self):

        """ Sprawdź, czy nie zostały złapane jakieś gwiazdy. """
        

        for pizza in self.overlapping_sprites:
         
            self.score.value += 10          
            self.score.right = games.screen.width - 10 
            
            
            pizza.handle_caught()
            
            if self.score.value == 200:

                self.win()

    
    def win(self):
		            
           

             end_message = games.Message(value = "wygrana",
						 size = 90,
						 color = color.red,
						 x = games.screen.width/2,
						 y = games.screen.height/2,
						 lifetime = 1 * games.screen.fps,
						 after_death = games.screen.quit)
             games.screen.add(end_message)

            
            
        
          
      
class Pizza(games.Sprite):

    """

    gwiazda, która spada na ziemię.

    """ 

    image = games.load_image("pizza.bmp")

    speed = 1.5 
     
   
				
        
       
       
    def __init__(self, x, y = 90):

        """ Inicjalizuj obiekt klasy Pizza. """

        super(Pizza, self).__init__(image = Pizza.image,

                                    x = x, y = y,

                                    dy = Pizza.speed)



    def update(self):

        """ Sprawdź, czy dolny brzeg pizzy dosięgnął dołu ekranu. """

        if self.bottom > games.screen.height:

            self.end_game()

            self.destroy()



    def handle_caught(self):

        """ zniszcz jeśli złapane. """

        self.destroy()



    def end_game(self):
		
		

        
        end_message = games.Message(value = "Koniec gry",

                                    size = 90,

                                    color = color.red,

                                    x = games.screen.width/2,

                                    y = games.screen.height/2,

                                    lifetime = 1 * games.screen.fps,

                                    after_death = games.screen.quit)

        games.screen.add(end_message)
	



	

class box(games.Sprite):

    """

    pudełko, który porusza się w lewo i w prawo, zrzucając gwiazde.

    """

    image = games.load_image("pudlo.bmp")



    def __init__(self, y = 55, speed = 2, odds_change = 200):

      

        super(box, self).__init__(image = box.image,

                                   x = games.screen.width / 2,

                                   y = y,

                                   dx = speed)

        

        self.odds_change = odds_change

        self.time_til_drop = 0



    def update(self):

        """ Ustal, czy kierunek ruchu musi zostać zmieniony na przeciwny. """

        if self.left < 0 or self.right > games.screen.width:

            self.dx = -self.dx

        elif random.randrange(self.odds_change) == 0:

           self.dx = -self.dx

                

        self.check_drop()





    def check_drop(self):

        """ Zmniejsz licznik odliczający czas lub zrzuć gwiazde i zresetuj odliczanie. """

        if self.time_til_drop > 0:

            self.time_til_drop -= 1

        else:

            new_pizza = Pizza(x = self.x)

            games.screen.add(new_pizza)



            

            self.time_til_drop = int(new_pizza.height * 1.3 / Pizza.speed) + 1      


def button(msg, x, y, w, h, inact, act, action = None):
 mouse = pygame.mouse.get_pos()
 click = pygame.mouse.get_pressed()

 if x + w > mouse[0] > x and  y + h > mouse[1] > y:
  pygame.draw.rect(gameDisplay, act, (x, y, w, h))
  if click[0] == 1 and action != None:
   if action == "play":
    main()
 
  
   
 else:
  pygame.draw.rect(gameDisplay, inact, (x, y, w, h))
   
 smallText = pygame.font.Font("freesansbold.ttf", 32)
 textSurf, textRect = text_objects(msg, smallText)  
 textRect.center = ( (x + (w/2)), (y + (h/2)))
 gameDisplay.blit(textSurf, textRect)

 def game_menu():#klasa menu
 
  
  menu = True
 
  while menu:
   for event in pygame.event.get():
    if event.type == pygame.QUIT:
     quit()
   gameDisplay.blit(menu_image, [0,0])

   button("START", 40, 124, 350, 40, color.red, color.green, "play")
  
   pygame.display.update()
   clock.tick(15)
def main():

    """ Uruchom grę. """
   
   
  
 
    wall_image = games.load_image("sciana.jpg", transparent = False)
    
 

	

    games.screen.background = wall_image
    
    
    the_box = box()

    games.screen.add(the_box)



    the_pan = Pan()

    games.screen.add(the_pan)



    games.mouse.is_visible = False

   

    games.screen.event_grab = True

    games.screen.mainloop()


game_menu()
main()

pygame.quit()


