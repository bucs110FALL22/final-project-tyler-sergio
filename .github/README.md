:warning: Everything between << >> needs to be replaced (remove << >> after replacing)
# CS110 Project Proposal
# Alien Running
## CS 110 Final Project
### Fall Semester, 2022
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit?usp=sharing)


https://replit.com/join/ztakfmmctz-tylermoy

(https://docs.google.com/presentation/d/1ANzWox7AkampWhrQUmIXnRSgKLYriFsnhs9rqwUT-PA/edit?usp=sharing)

### Team: Tyler & Sergio  - (S&T Studios)
#### Tyler Moy & Sergio Soria

***

## Project Description

The game has a surviving and a focus mechanic, where the user needs to avoid enemies in the space field with the support of arrow keys. Considering the maximum punctuation that you may got shown in the Score. And having the possibility to try improving your record anytime.   

***    

## User Interface Design

- **Initial Concept**
  - Concept Art: [Concept Art:](assets/OutputScreen.jpg)
    
  - Game screen: The first interaction of the game starts ahead with a soft and basic control to go little by little to understand the game.

  - Game Over Screen: Once enemiesreched to touch the player, there will appear a decision to the user, either be to restart the game to play again or exit. 
      
    
- **Final GUI**
  - Game Screen: [Game Screen:](assets/Screenshot_game.png)
  - Game Over Screen:  [Game Over Screen:](assets/Screenshot_gameover.png)


***        

## Program Design

* Non-Standard libraries
    * Pygame: A module to set functions to develop games into Python.
      
    * Random: A module to prepare random numbers for different distributions. 



* Class Interface Design
     
    * ![class diagram](assets/class_diagram.jpg)
    * ![Classes:](assets/classes.png)
    * ![Classes:](assets/SecondClasses.png)
      



* Classes
    * Class Squid: A class that execute the way of motion, appareance, size of the player through a picture of a  squid, and being controlled by the arrows keys, having account the boundaries of the output.  
      
    * Class Enemy: This class is responsible for most functions related to the spawning of enemies and management of enemy data.
      
    * Class Text: A class that present and personifies the characteristics of the displays of text in the Output. It makes the displaying of text easier to do (kind of).
      
    * Class Controller: A class that set and apply the functions to the user and all elements in the program, even the settings to restart or exit the game. 



## Project Structure and File List

The Project is broken down into the following file structure:


* main.py
* src
    * << all of your python files should go here >> 
* assets
    * << all of your media, i.e. images, font files, etc, should go here) >>


***



## Tasks and Responsibilities 

   * Sergio Soria was responsible to the ellaboration of the Squid Class, and the space environment and the main controls of the player. 

   * Tyler Moy was responsible to the Enemies and Text Class and organize their functions to the Control Class. 


## Testing

* We used to check the program during each time that we analyze all classes. Besides, we always run the program to verify since the beginning to the final that every code is succesfully organized and placed.
* To iron out all of the bugs, we ran the program periodically to see if things were working correctly. When errors came up, we would look at what line the error occured at and then figure out why it happened and how to fix it.




## ATP

| Step |Procedure                            |Expected Results                                                                    |
|------|:-----------------------------------:|-----------------------------------------------------------------------------------:|
|  1   | Start program along with the window | GUI Program appears without problem.                                              |
|  2   | Run and check controllers           | Player starts to move around the background exported.                             |
|  3   | Enemies appears                     | Amount of enemies increases to have difficulty in the gameplay.                   |
|  4   | Score acts raising numbers          | Balanced reaction at time to avoid enemies.                                       |
|  5   | Game Over text appears              | Game stop when player is in contact with an enemy and respective score is visible.|
