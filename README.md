# Rush-Hour-Solver
Rush-Hour-Solver is an interactive Rush Hour logic puzzle solver.

Find the physical game here: https://www.thinkfun.com/products/rush-hour/

#Setup 

1. Select if you want to solve a traditional 6x6 board or an extended one
  
  -enter 't' or 'e' for traditional or extended respectively
  
  result: If 't' is selected, a traditional board will be set up, while if 'e' is selected, inputs to determine an extended board will be added

2a. If traditional, place the red escaping car horizontally in row 2
  
  -enter an integer 1-5 to indicate the red car's left bumper position
  
  result: the red car is placed horizontally in row 2 of the board where indicated
  
2b. If extended, indicate the dimension, red escaping car row, and red escaping car horizontal position
  
  -enter an integer 5-10 to indicate the dimensions of the board
  
  -enter an integer 1-dimension to indicate the red car's row
  
  -enter an integer 1-(dimension-1) to indicate the red car's left bumper position
  
  result: the board is extended as indicated,and the red car is placed on the row and horizontal position indicated

3. Place remaining cars and trucks
  
  -enter 'c' or 't' to place a car or truck respectively - hit enter
  
  -enter an integer 1-6 to indicate the horizontal positon of the left/top bumper depending what the orientation will be - hit enter 
  
  -enter an integer 1-6 to indicate the vertical positon of the left/top bumper depending what the orientation will be - hit enter
  
  -enter 'h' or 'v' to indicate horizontal or vertical orientation of the car respectively - hit enter
  
  -enter an integer according to the displayed listing corresponding to the color of the car or truck being placed - hit enter
  
  result: the car or truck is placed on the board as indicated
 
 Repeat step 2 until all cars and trucks have been placed
 
 #Run
 
 1. Run the board solver
  
  -enter 'p' - hit enter
 
 2. Follow the instructions to solve your board - Instructions include both step by step text instructions and board snapshots
