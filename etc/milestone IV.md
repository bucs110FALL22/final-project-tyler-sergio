
## Controller

Answer the following questions about your controller class

1. do you have a mainloop?
    * if you have sub loops, are they exclusive? i.e. only 1 will ever run at a time
    
    Yes, we have a loop to the main controls supported by a while loop inside the class of 
    the Game.  

2. Are you responding to events first in your loop?

   Yes, for all loops of the controllers we are using the pygame.events.keys. Specifically 
   to use the arrow keys.

3. Are you updating models after events?

   Yes, we are updating models after the events. 

4. Are you re-drawing the background, THEN each screen element every frame?

   At measure, we make and adding codes to the project, then we will try to every element 
   run appropiate. 
    
5. Are you calling pygame.flip() or pygame.update() at the end of your mainloop
   Yes we are finish pygame.flip() and pygame.update() to the running of the codes in the 
   loops and avoid complications.




