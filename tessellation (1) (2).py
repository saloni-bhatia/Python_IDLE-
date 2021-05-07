
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: N10337032
#    Student name:Saloni Bhatia
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  TESSELLATION
#
#  This assignment tests your skills at processing data stored in
#  lists, creating reusable code and following instructions to display
#  a complex visual image.  The incomplete Python program below is
#  missing a crucial function, "tessellate".  You are required to
#  complete this function so that when the program is run it fills
#  a rectangular space with differently-shaped tiles, using data
#  stored in a list to determine which tiles to place and where.
#  See the instruction sheet accompanying this file for full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  your final solution as a single Python 3 file, whether or not you
#  complete both parts of the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.  In
# particular, your solution must not rely on any non-standard Python
# modules that need to be downloaded and installed separately,
# because the markers will not have access to such modules.

from turtle import *
from math import *
from random import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

cell_size = 100 # pixels (default is 100)
grid_width = 10 # squares (default is 10)
grid_height = 7 # squares (default is 7)
x_margin = cell_size * 2.75 # pixels, the size of the margin left/right of the grid
y_margin = cell_size // 2 # pixels, the size of the margin below/above the grid
window_height = grid_height * cell_size + y_margin * 2
window_width = grid_width * cell_size + x_margin * 2
small_font = ('Arial', 18, 'normal') # font for the coords
big_font = ('Arial', 24, 'normal') # font for any other text

# Validity checks on grid size - do not change this code
assert cell_size >= 80, 'Cells must be at least 80x80 pixels in size'
assert grid_width >= 8, 'Grid must be at least 8 squares wide'
assert grid_height >= 6, 'Grid must be at least 6 squares high'

#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# manage the drawing canvas for your image.  You should not change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image
def create_drawing_canvas(bg_colour = 'light grey',
                          line_colour = 'slate grey',
                          draw_grid = True, mark_legend = True):
    
    # Set up the drawing canvas with enough space for the grid and
    # legend
    setup(window_width, window_height)
    bgcolor(bg_colour)

    # Draw as quickly as possible
    tracer(False)

    # Get ready to draw the grid
    penup()
    color(line_colour)
    width(2)

    # Determine the left-bottom coords of the grid
    left_edge = -(grid_width * cell_size) // 2 
    bottom_edge = -(grid_height * cell_size) // 2

    # Optionally draw the grid
    if draw_grid:

        # Draw the horizontal grid lines
        setheading(0) # face east
        for line_no in range(0, grid_height + 1):
            penup()
            goto(left_edge, bottom_edge + line_no * cell_size)
            pendown()
            forward(grid_width * cell_size)
            
        # Draw the vertical grid lines
        setheading(90) # face north
        for line_no in range(0, grid_width + 1):
            penup()
            goto(left_edge + line_no * cell_size, bottom_edge)
            pendown()
            forward(grid_height * cell_size)

        # Draw each of the labels on the x axis
        penup()
        y_offset = 27 # pixels
        for x_label in range(0, grid_width):
            goto(left_edge + (x_label * cell_size) + (cell_size // 2), bottom_edge - y_offset)
            write(chr(x_label + ord('A')), align = 'center', font = small_font)

        # Draw each of the labels on the y axis
        penup()
        x_offset, y_offset = 7, 10 # pixels
        for y_label in range(0, grid_height):
            goto(left_edge - x_offset, bottom_edge + (y_label * cell_size) + (cell_size // 2) - y_offset)
            write(str(y_label + 1), align = 'right', font = small_font)

        # Mark centre coordinate (0, 0)
        home()
        dot(15)

    # Optionally mark the spaces for drawing the legend
    #if mark_legend:
        # Left side
        ##goto(-(grid_width * cell_size) // 2 - 75, -25)
        #write('Put your\nlegend here', align = 'right', font = big_font)    
        # Right side
        #goto((grid_width * cell_size) // 2 + 75, -25)
        #write('Put your\nlegend here', align = 'left', font = big_font)    

    # Reset everything ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas to the operating
# system.  By default the cursor (turtle) is hidden when the
# program ends - call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor = True):
    tracer(True) # ensure any drawing still in progress is displayed
    if hide_cursor:
        hideturtle()
    done()
    
#
#--------------------------------------------------------------------#



#-----Test Data for Use During Code Development----------------------#
#
# The "fixed" data sets in this section are provided to help you
# develop and test your code.  You can use them as the argument to
# the "tesselate" function while perfecting your solution.  However,
# they will NOT be used to assess your program.  Your solution will
# be assessed using the "random_pattern" function appearing below.
# Your program must work correctly for any data set that can be
# generated by the random_pattern function.
#
# Each of the data sets is a list of instructions, each specifying
# where to place a particular tile.  The general form of each
# instruction is
#
#     [squares, mystery_value]
#
# where there may be one, two or four squares in the grid listed
# at the beginning.  This tells us which grid squares must be
# filled by this particular tile.  This information also tells
# us which shape of tile to produce.  A "big" tile will occupy
# four grid squares, a "small" tile will occupy one square, a
# "wide" tile will occupy two squares in the same row, and a
# "tall" tile will occupy two squares in the same column.  The
# purpose of the "mystery value" will be revealed in Part B of
# the assignment.
#
# Note that the fixed patterns below assume the grid has its
# default size of 10x7 squares.
#

# Some starting points - the following fixed patterns place
# just a single tile in the grid, in one of the corners.

# Small tile
fixed_pattern_0 = [['A1', 'O']] 
fixed_pattern_1 = [['J7', 'X']]

# Wide tile
fixed_pattern_2 = [['A7', 'B7', 'O']] 
fixed_pattern_3 = [['I1', 'J1', 'X']]

# Tall tile
fixed_pattern_4 = [['A1', 'A2', 'O']] 
fixed_pattern_5 = [['J6', 'J7', 'X']]

# Big tile
fixed_pattern_6 = [['A6', 'B6', 'A7', 'B7', 'O']] 
fixed_pattern_7 = [['I1', 'J1', 'I2', 'J2', 'X']]

# Each of these patterns puts multiple copies of the same
# type of tile in the grid.

# Small tiles
fixed_pattern_8 = [['E1', 'O'],
                   ['J4', 'O'],
                   ['C5', 'O'],
                   ['B1', 'O'],
                   ['I1', 'O']] 
fixed_pattern_9 = [['C6', 'X'],
                   ['I4', 'X'],
                   ['D6', 'X'],
                   ['J5', 'X'],
                   ['F6', 'X'],
                   ['F7', 'X']]

# Wide tiles
fixed_pattern_10 = [['A4', 'B4', 'O'],
                    ['C1', 'D1', 'O'],
                    ['C7', 'D7', 'O'],
                    ['A7', 'B7', 'O'],
                    ['D4', 'E4', 'O']] 
fixed_pattern_11 = [['D7', 'E7', 'X'],
                    ['G7', 'H7', 'X'],
                    ['H5', 'I5', 'X'],
                    ['B3', 'C3', 'X']]

# Tall tiles
fixed_pattern_12 = [['J2', 'J3', 'O'],
                    ['E5', 'E6', 'O'],
                    ['I1', 'I2', 'O'],
                    ['E1', 'E2', 'O'],
                    ['D3', 'D4', 'O']] 
fixed_pattern_13 = [['H4', 'H5', 'X'],
                    ['F1', 'F2', 'X'],
                    ['E2', 'E3', 'X'],
                    ['C4', 'C5', 'X']]

# Big tiles
fixed_pattern_14 = [['E5', 'F5', 'E6', 'F6', 'O'],
                    ['I5', 'J5', 'I6', 'J6', 'O'],
                    ['C2', 'D2', 'C3', 'D3', 'O'],
                    ['H2', 'I2', 'H3', 'I3', 'O'],
                    ['A3', 'B3', 'A4', 'B4', 'O']] 
fixed_pattern_15 = [['G2', 'H2', 'G3', 'H3', 'X'],
                    ['E5', 'F5', 'E6', 'F6', 'X'],
                    ['E3', 'F3', 'E4', 'F4', 'X'],
                    ['B3', 'C3', 'B4', 'C4', 'X']]

# Each of these patterns puts one instance of each type
# of tile in the grid.
fixed_pattern_16 = [['I5', 'O'],
                    ['E1', 'F1', 'E2', 'F2', 'O'],
                    ['J5', 'J6', 'O'],
                    ['G6', 'H6', 'O']]
fixed_pattern_17 = [['G7', 'H7', 'X'],
                    ['B7', 'X'],
                    ['A5', 'B5', 'A6', 'B6', 'X'],
                    ['D2', 'D3', 'X']]

# If you want to create your own test data sets put them here,
# otherwise call function random_pattern to obtain data sets
# that fill the entire grid with tiles.
 
#
#--------------------------------------------------------------------#



#-----Function for Assessing Your Solution---------------------------#
#
# The function in this section will be used to assess your solution.
# Do not change any of the code in this section.
#
# The following function creates a random data set specifying a
# tessellation to draw.  Your program must work for any data set that
# can be returned by this function.  The results returned by calling
# this function will be used as the argument to your "tessellate"
# function during marking.  For convenience during code development
# and marking this function also prints the pattern to be drawn to the
# shell window.  NB: Your solution should not print anything else to
# the shell.  Make sure any debugging calls to the "print" function
# are disabled before you submit your solution.
#
# This function attempts to place tiles using a largest-to-smallest
# greedy algorithm.  However, it randomises the placement of the
# tiles and makes no attempt to avoid trying the same location more
# than once, so it's not very efficient and doesn't maximise the
# number of larger tiles placed.  In the worst case, only one big
# tile will be placed in the grid (but this is very unlikely)!
#
# As well as the coordinates for each tile, an additional value which
# is either an 'O' or 'X' accompanies each one.  The purpose of this
# "mystery" value will be revealed in Part B of the assignment.
#
def random_pattern(print_pattern = True):
    # Keep track of squares already occupied
    been_there = []
    # Initialise the pattern
    pattern = []
    # Percent chance of the mystery value being an X
    mystery_probability = 8

    # Attempt to place as many 2x2 tiles as possible, up to a fixed limit
    attempts = 10
    while attempts > 0:
        # Choose a random bottom-left location
        column = randint(0, grid_width - 2)
        row = randint(0, grid_height - 2)
        # Try to place the tile there, provided the spaces are all free
        if (not [column, row] in been_there) and \
           (not [column, row + 1] in been_there) and \
           (not [column + 1, row] in been_there) and \
           (not [column + 1, row + 1] in been_there):
            been_there = been_there + [[column, row], [column, row + 1],
                                       [column + 1, row], [column + 1, row + 1]]
            # Append the tile's coords to the pattern, plus the mystery value
            pattern.append([chr(column + ord('A')) + str(row + 1),
                            chr(column + ord('A') + 1) + str(row + 1),
                            chr(column + ord('A')) + str(row + 2),
                            chr(column + ord('A') + 1) + str(row + 2),
                            'X' if randint(1, 100) <= mystery_probability else 'O'])
        # Keep track of the number of attempts
        attempts = attempts - 1

    # Attempt to place as many 1x2 tiles as possible, up to a fixed limit
    attempts = 15
    while attempts > 0:
        # Choose a random bottom-left location
        column = randint(0, grid_width - 1)
        row = randint(0, grid_height - 2)
        # Try to place the tile there, provided the spaces are both free
        if (not [column, row] in been_there) and \
           (not [column, row + 1] in been_there):
            been_there = been_there + [[column, row], [column, row + 1]]
            # Append the tile's coords to the pattern, plus the mystery value
            pattern.append([chr(column + ord('A')) + str(row + 1),
                            chr(column + ord('A')) + str(row + 2),
                            'X' if randint(1, 100) <= mystery_probability else 'O'])
        # Keep track of the number of attempts
        attempts = attempts - 1
        
    # Attempt to place as many 2x1 tiles as possible, up to a fixed limit
    attempts = 20
    while attempts > 0:
        # Choose a random bottom-left location
        column = randint(0, grid_width - 2)
        row = randint(0, grid_height - 1)
        # Try to place the tile there, provided the spaces are both free
        if (not [column, row] in been_there) and \
           (not [column + 1, row] in been_there):
            been_there = been_there + [[column, row], [column + 1, row]]
            # Append the tile's coords to the pattern, plus the mystery value
            pattern.append([chr(column + ord('A')) + str(row + 1),
                            chr(column + ord('A') + 1) + str(row + 1),
                            'X' if randint(1, 100) <= mystery_probability else 'O'])
        # Keep track of the number of attempts
        attempts = attempts - 1
        
    # Fill all remaining spaces with 1x1 tiles
    for column in range(0, grid_width):
        for row in range(0, grid_height):
            if not [column, row] in been_there:
                been_there.append([column, row])
                # Append the tile's coords to the pattern, plus the mystery value
                pattern.append([chr(column + ord('A')) + str(row + 1),
                                'X' if randint(1, 100) <= mystery_probability else 'O'])

    # Remove any residual structure in the pattern
    shuffle(pattern)
    # Print the pattern to the shell window, nicely laid out
    print('Draw the tiles in this sequence:')
    print(str(pattern).replace('],', '],\n'))
    # Return the tessellation pattern
    return pattern

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "tessellate" function.
#



# Fill the grid with tiles as per the provided dataset

def tessellate(given_pattern=[]):

    # Defining global variables : to be used through out the function
    global x_cor
    global y_cor
    global diagonal


    ## defining tile function
    
                  #--------- DEFINING SMALL TILE -----------#

    
    def small_tile():
        
        pendown()
        width(2)
        pencolor('black')
        setheading(0)#face east
        fillcolor('ivory2')
        begin_fill()
        for boundary in range (4):
            forward(cell_size)
            right(90)
        end_fill()

        ## Going to the location
        penup()
        setheading(270)#face south
        forward(cell_size-15)
        setheading(0)
        forward(30)

        ## Assigning reusable variables
        gatelength=40 # length of the gate's structure 
        gatewidth=45 # length of the top coloumn
        length_gate=25 # length of the gate's opening
        distance_between=10 #distance between the opening and the structure 
        circle_radius=10 # radius of the gate's opening
        

        # Making the gate
        fillcolor('dark salmon')
        begin_fill()
        pendown()
        pencolor('indian red')
        width(2)
        setheading(90)
        forward(gatelength)
        left(30)
        forward(5)
        setheading(0)
        forward(gatewidth)
        left(-110)
        forward(6)
        setheading(180)
        forward(gatewidth-5)
        penup()
        back(gatewidth-5)
        pendown()
        setheading(270)
        forward(gatelength)

        # Drawing the gate's opening

        setheading(180)#face west
        forward(distance_between)
        right(90)
        forward(length_gate)
        

        circle(circle_radius,180)
        setheading(270)
        forward(length_gate)
            
        
        setheading(180)
        forward(distance_between)
        end_fill()

        ## Making the top 3 pedestals

        # Going to the location
        penup()
        setheading(90)# face North
        forward(gatelength+5)
        setheading(0)
        forward(2)
        setheading(90)

         
         # using 'while' loop to construct the pedestal with decreasing length
         
         # Assigning variable
        ped_length=gatelength-4 # length of the first pedestal 
        ped_width=5 #width of pedestals
        pedestal=3 # number of iteration for 'while' loop

        while pedestal>0:
            fillcolor('dark salmon')
            begin_fill()
            pendown()
            if pedestal==1:
                ped_width=ped_width+3 # the last one has a bigger size
            forward(ped_width)
            right(90)
            forward(ped_length)
            right(90)

            forward(ped_width)
            right(90)
            forward(ped_length)
            right(90)
            end_fill()
                 
            ped_length=ped_length-4 # decreasing the length
            pedestal=pedestal-1 # decreasing the number of iteration to meet condition 
            penup()
            setheading(90)
            forward(ped_width)
            setheading(0)
            forward(2)
            setheading(90)

        ## Inscribing INDIA

        setheading(0)
        forward(ped_length/3)
        setheading(270)
        forward(ped_width/1.5)
        setheading(0)
        pencolor('maroon')
        write('INDIA',font=('Times New Roman',4))
        
       ### Creating the top dome
        
        pencolor('indian red')
        penup()
        setheading(180)
        forward(5)
        setheading(90)
        forward(8)
        pendown()
        fillcolor('dark salmon')
        begin_fill()
        forward(2)
        right(60)
        forward(5)
        setheading(0)
        forward(8)
        right(10)
        forward(2)
        setheading(0)
        right(30)
        forward(5)
        setheading(270)
        forward(3)
        setheading(180)
        penup()
        forward(20)
        end_fill()

        
       #### Detailing the gate 
        
        penup()
        setheading(180)
        forward(2)
        setheading(270)
        forward(25)
        pendown()
        pencolor('indian red')
        forward(gatelength-2)
        back(gatelength-2)
        setheading(0)
        forward(gatewidth-(2*distance_between))
        setheading(270)
        forward(gatelength-2)

        # Making the base
        
        penup()
        setheading(270)
        forward(2)
        setheading(180)
        forward(gatelength+20)
        pendown()
        setheading(0)
        forward(cell_size-2)
     
        
        
         
                         #--------- DEFINING TALL TILE -----------#    
 
    def tall_tile():
    
     
        
        pendown()   
        setheading(0)
        width(2)
        pencolor('dim grey')
        fillcolor('lavender blush')
        begin_fill()
        
       
        # forming the boundary and background
        for boundary in range (2):
            forward(cell_size)
            right(90)
            forward(cell_size*2)
            right(90)
        end_fill()

        # Going to the location to draw  
        penup()
        setheading(270)
        forward(175)
        setheading(0)
        forward(5)
        setheading(0)
        width(2)

        # Making the base of the eiffel tower
        width(3)
        pendown()
        forward(10)
        left(60)
        circle(-40,120) # curved base 
        left(60)
        forward(10)
        left(120)
        forward(30)
        left(60)
        forward(60)
        left(60)
        forward(30)
        right(180)
        forward(30)
         
        # Drawing the second level
        right(60)
        left(60)
        forward(15)
        right(60)
        forward(45)
        right(60)
        forward(15)
        penup()
        right(120)
        forward(60)
        left(60)
        forward(20)

        # Drawing the third level
        penup()
        right(180)
        forward(35)
        right(70) 
        pendown()
        right(-80)
        forward(45)
        right(70)
        forward(20)
        left(-75)
        forward(45)
        left(-110)
        forward(15)
        left(-80)
        forward(40)
        left(80)
        forward(5)
        left(85)
        forward(40)
        right(75)
        forward(18)
        
        # Drawing the top pillar    
        penup()
        right(115)
        forward(45)
        left(10)
        pendown() 
        forward(55)
        left(100)
        forward(5)
        right(90)
        forward(5)
        right(90)
        forward(7)
        left(90)
        
        forward(10)
        
        back(10)

        #drawing the top box
        for box in range(3):
            right(90)
            forward(5)
       # Finishing the tower
        setheading(0)
        right(80)
        forward(55)

        ## Detailing with trusses
          ### Defining the function for first_trusses 
     
        def first_trusses(angle,angle1,angle2,distance,add,no_of_times=2):
                
            width(2)
            for trusses in range(no_of_times):
                        
                setheading(angle)
                right(angle1)
                forward(distance)
                right(angle2)
                distance=distance+add
                forward(distance)
          
        ## The trusses in the top tower

        first_trusses(180,45,90,20,-5,2)
        ## Going to the location
        setheading(180)
        forward(5)
          
         # Calling the function
        first_trusses(0,45,90,10,5,2)
      ## Detailing the base beneath the tower
        
        width(5)
        setheading(0)
        forward(15)
        setheading(180)
        forward(15)



       # Second truss : Cannot use the function defined ; as requirenments are different

        width(2)
        for secondtruss in range(5):         
             if secondtruss>=3:
                distance=distance+2
             else:
                 distance=10
             setheading(0)
             right(45)
             forward(distance)
             setheading(180)
             forward(distance)




        ## defining functions for trusses
        def trusses(no_of_times,angle,angle1,angle2,distance1,distance2,add1,add2):
              for trussess in range (no_of_times):
                  
                  setheading(angle)
                  right(angle1)
                  forward(distance1)
                  distance1=distance1+add1
                  setheading(angle2)
                  forward(distance2)
                  distance2=distance2+add2

        ## Trusss for the bases
     
           ## Third truss
        penup()
        setheading(90)
        forward(40)
        setheading(0)
        forward(30)
        pendown()

        # Calling the function

        trusses(4,0,45,180,9,7,4,2)

        
        # Fourth truss
        penup()
        setheading(0)
        forward(15)
        pendown()

        # Cannot use the function (trusses) defined ; as requirenments are different 
        
        for truss_4 in range(2):  
            pendown()
            setheading(180)
            left(45)
            forward(15)
            right(90)
            forward(15)

        # Fifth truss
        
        penup()
        left(90)
        forward(15)
        pendown()

        ##Calling the function

        trusses(3,0,45,180,15,15,-3,-2)

        # Sixth truss
        penup()
        setheading(90)
        forward(25)
        setheading(0)
        forward(70)
        pendown()

        ## Calling the function

       
        trusses(3,180,-45,0,14,14,-3,-2)

         # Making the base
        penup()
        setheading(180)
        forward(cell_size-10)
        setheading(270)
        forward(5)
        pendown()
        setheading(0)
        forward(cell_size)
       


         
                                      #--------- DEFINING WIDE TILE -----------#

    def wide_tile():
        
        pendown()
        width(2)
        pencolor('black')
        fillcolor('azure')
        begin_fill()
        setheading(0)

        # Forming the boundary
        
        for boundary in range (2):
             forward(cell_size*2)
             right(90)
             forward(cell_size)
             right(90)
        end_fill()
        
        pencolor("black")
        penup()
        right(90)
        forward(70)
        left(90)
        pendown()
        forward(30)
        right(-90)
        width(2)
        forward(30)
      
        # Drawing the two pillars for the bridge 
        
        right(180)
        forward(35)
        right(45)
        pendown()
        pencolor("black")
        fillcolor("black")
        begin_fill()
        forward(5)
        left(135)
        forward(10)
        left(130)
        forward(5)
        right(40)
        forward(35)
        left(90)
        forward(2)
        end_fill()
        penup()
        right(180)
        forward(2)
        right(90)
        forward(30)
        left(90)
        forward(5)
        pendown()
        width(2)
    
        fillcolor("black")
        begin_fill()
        left(90)
        forward(30)
        right(90)
        forward(3)
        right(90)
        forward(35)
        left(50)
        forward(6)
        right(140)
        forward(10)
        right(120)
        forward(5)
        left(35)
        forward(5)
        end_fill()

        # Going to location for making he bridge's suspension
        penup()
        right(180)
        forward(1)
        setheading(0)
        forward(2)
        pendown()
        width(0)
        forward(30)

        #settingnup variables
        distance=40;

        ## Using the 'for' loop to for triangles - wires of the bridge
        
        for triangles in range (4):
            penup()
            setheading(180)
            forward(3)
            right(30)
            pendown()
            forward(distance)
            left(60)
            forward(distance)
            distance=distance-5;
            penup()
                ## SECOND TRIANGLE
            setheading(0)
            forward(3)
            left(30)
            pendown()
            forward(distance)
            right(60)
            forward(distance)
            distance=distance-5;

        # Drawing the buildings

        ## The first building
        
        setheading(0)
        forward(20)
        pendown()
        fillcolor("black")
        begin_fill()
        forward(10)
        left(90)
        forward(5)
        right(90)
        forward(5)
        right(90)
        forward(2)
        left(120)
        forward(5)
        setheading(90)
        forward(20)
        right(90)
        forward(2)
        left(90)
        forward(2)
        right(90)
        forward(2)
        right(90)
        forward(20)
        left(50)
        forward(5)
        setheading(0)
        left(10)
        forward(10)
        setheading(0)
        right(90)
        forward(10)
        right(90)
        forward(45)
        right(140)
        forward(5)
            
        end_fill()

        # The second building

        penup()
        setheading(0)
        forward(35)
        right(90)
        forward(10)
        left(90)
        forward(1)
        pendown()
        setheading(90)
        fillcolor("black")
        begin_fill()

        # Using loops to form squares
        # The third building
        
        for buildingsquare in range (2):
            forward(40)
            right(90)
            forward(10)
            right(90)
        end_fill()
        penup()
        right(90)
        forward(12)
        setheading(90)
        
        begin_fill()
        
        for buildingsquare in range (2):
            forward(45)
            right(90)
            forward(10)
            right(90)
        end_fill()


        # The fourth building
        
        begin_fill()
        penup()
        right(90)
        forward(12)
        setheading(90)
        pendown()
        forward(40)
       
        circle(-5,180) # Making the top of the building
        setheading(90)
        circle(-5,180)
        setheading(270)
        forward(40)
        left(-90)
        
        end_fill()
        pendown()
        right(90)
        forward(40)
        setheading(270)
        
        pencolor('white') # Detailing the top of the building
        circle(-10,160)
        penup()
        setheading(0)
        forward(10)
        setheading(90)
        pendown()
        forward(5)
        right(180)
        forward(10)
        right(180)
        forward(10)
        
        pencolor('black')
        forward(10)
        

        # The fifth building
        
        penup()
        setheading(270)
        forward(45)
        setheading(0)
        forward(12)
        pendown()
        begin_fill()
        setheading(90)
        forward(50)
        right(45)
        forward(15)
        setheading(270)
        forward(68)
        right(90)
        forward(10)
        end_fill()

        # The sixth building
        
        penup()
        setheading(0)
        forward(12)
        setheading(90)
        pendown()
        begin_fill()
        forward(50)
        right(90)
        forward(10)
        right(90)
        forward(50)
        right(90)
        forward(10)
        end_fill()

        # The seventh building
        penup()
        setheading(0)
        forward(12)
        setheading(90)
        pendown()
        begin_fill()
        begin_fill()
        forward(40)
        
        circle(-5,180)
        setheading(270)
        forward(40)
        right(90)
        forward(10)
        end_fill()

         # The small buildings
         
       # The eigth building ( First small building)

        width(2)
        pencolor('white')
        forward(20)
        right(90)
        forward(5)
        right(90)
        forward(15)
        setheading(90)
        circle(-5,95)
        setheading(90)
        forward(5)
        right(180)
        forward(5)
        setheading(0)
        circle(-5,110)
        left(110)
        forward(5)
        
         # The ninth building ( Second small building)
         
        penup()
        forward(2)
        left(90)
        begin_fill()
        pencolor('black')
        pendown()
        forward(30)
        right(90)
        forward(5)

        # Drawing the top of the building
        
        for spikers in range(2):
           left(45)
           forward(5)
           right(90)
           forward(5)
                
        forward(28)
        right(90)
        forward(15)
        right(90)
        forward(2)
        end_fill()

        
        # The two white small buildings
        
        fillcolor('black')
        begin_fill()
        pencolor('white')
        width(2)
        right(45)
        forward(5)
        setheading(0)
        forward(5)
        right(90)
        forward(2)
        left(90)
      
        forward(5)
        left(90)
        forward(2)
        right(120)
        forward(12)
        penup()
        setheading(180)
        forward(20)
        end_fill()

    
        penup()
        fillcolor('black')
        
        pencolor('black')
        forward(120)
        right(90)
        forward(5)
        right(100)
        right(90)
        forward(5)


                                #--------- DEFINING BIG TILE -----------#
        
    def big_tile():

            pendown()
            width(2)
            pencolor('black')
            setheading(0)
            
            fillcolor('white')
            begin_fill()
            ## Making the boundary
            for boundary in range(4):
                forward(cell_size*2)
                right(90)
            end_fill()

           # --------  -------  -------- #
            
            # Going to a location
            
            penup()
            setheading(270)
            forward(cell_size*1.5)
            setheading(0)
            forward(15)
            

            
            # Taj mahal
            
            def taj(angle1,angle2,angle3,angle4,angle5,angle6,angle7,radius1,radius2,radius3,radius4):
                
                pendown()
                
                forward(10)
                setheading(90)
                forward(50)
                width(0) 
                forward(20)
                back(20)
                right(angle1)
                width(2) # changing width for detailing 
                forward(5)
                setheading(90)
                width(0)
                forward(20)
                back(20)
                setheading(angle2)
                width(2)
                forward(10)
                left(angle3)
                forward(10)
                setheading(angle4)
                forward(2)
                setheading(90)

                # drawing the first half of the first dome 
                
                circle(radius1,90)
                setheading(90)
                forward(5)
                back(5)
                setheading(angle5)
                # drwaing the second half of the first dome
                circle(radius2,90)
                
                #larger dome  
                setheading(angle6)
                forward(5)
                setheading(90)
                forward(5)
                # turning for better shape 
                left(angle7)
                
                pendown()
                # DRAWING THE LARGER DOME 
                circle(radius3,80)
                    
                circle(radius4,80)

                  #--------- ----------------- -----------#


                
                        
            # Calling the function to draw the first half
            fillcolor('black')
            begin_fill()
            taj(90,0,90,0,0,0,5,-10,-10,-30,10)
            
            penup()
            setheading(270)
            forward(cell_size+7)
            left(90)
            forward(cell_size-18)
            setheading(180)
            end_fill()
            
            # Calling the funtion to create the second half
            begin_fill()
            taj(-90,180,-90,180,180,180,-5,10,10,30,-10)

            # TOP DETAILS 
            setheading(90)
            forward(5)
            right(90)
            forward(2)
            back(4)
            forward(2)
            setheading(90)
            forward(5)
            right(90)
            forward(2)
            back(4)
            forward(2)
            setheading(90)
            forward(5)
           
            # going back to the base to fill the section
            
            back(cell_size+22) ## The total length of the structure : figured out by hit and trial 
            setheading(0)
            forward(cell_size-18) ## half of the width of the structure 
            end_fill()

            ## Adding the base
            
            pendown()
            forward(10)
            begin_fill()
            
            for base in range(2):
                
                right(90)
                forward(10)
                right(90)
                forward(2*(cell_size-18)+20)
            end_fill()

             ## Adding gates and windows
            
            pencolor('white')
            penup()
            back(cell_size-20)
            setheading(90)
            
            
            # adding gates and windows
            
            def gate_window(radius,length_gate,width_gate):

                fillcolor('white')
                begin_fill()
                pendown()
                forward(length_gate)
                circle(radius,80)
                penup()
                setheading(180)
                left(5)
                pendown()
                circle(radius,80)
                setheading(270)
                forward(length_gate+2)
                setheading(0)
                forward(width_gate)
                end_fill()
                penup()

                # ---------- ------- ------ #


            
           ## Calling functions for -  Main gate and windows
            
            gate_window(15,30,25) # The main gate
            
            penup()
            setheading(90)
            forward(25)
            setheading(0)
            forward(30)
            setheading(90)


            # The windows
            gate_window(5,10,8) 

            # Going to the location
            penup()
            forward(25)
            setheading(90)
            forward(2)
            
            gate_window(5,8,8)
            
            penup()
            setheading(90)
            back(20)

            gate_window(5,8,8)

            penup()
            back(25)
            setheading(90)

            gate_window(5,8,8)

            penup()
            back(70)
            setheading(90)

            gate_window(5,8,8)

            back(20)
            setheading(90)
            forward(2)
            gate_window(5,8,8)

            setheading(90)
            forward(30)

            gate_window(5,8,8)

            forward(25)
            setheading(90)
            forward(2)
            gate_window(5,8,8)


         #--------- ----------------- -----------#

     ## Defining a function to restore everything back to original
            
    def restore_settings():
        penup()
        pencolor('black')
        width(0)
        
        #--------- ----------------- -----------#

    # functions of broken tiles
    
    def small_tile_B():
        diagonal=sqrt(2)*cell_size #setting the diagonal using pythagorean theorem
        restore_settings()
        width(3)
        goto(x_cor,y_cor-cell_size)
        setheading(45)
        pendown()
        forward(diagonal)
        back(diagonal/4)

        fillcolor('light grey')
        begin_fill()
        
        goto(x_cor+(cell_size-50),y_cor-cell_size)
        goto(x_cor+12,y_cor-90)

        end_fill()
        
        #--------- ----------------- -----------#

    def tall_tile_B():
        
        diagonal=sqrt((pow(cell_size,2)+pow(2*cell_size,2)))
        restore_settings()
        width(3)
        goto(x_cor,y_cor-cell_size)
        setheading(65)
        pendown()
        forward(diagonal)
               
        fillcolor('light grey')
        begin_fill()
        goto(x_cor+(cell_size-20),y_cor-(cell_size-cell_size/2))
       
        penup()
        setheading(180)
        
        pendown()
        setheading(180)
        forward(30)
        
        goto(x_cor+7,y_cor-90)
        end_fill()
        penup()
        goto(x_cor+cell_size,y_cor-(cell_size))
        pendown()
        goto(x_cor+(cell_size-20),y_cor-(cell_size-cell_size/2))
        
        #--------- ----------------- -----------#

    def wide_tile_B():
        restore_settings()
        width(3)
        goto(x_cor,y_cor-cell_size)
        pendown()
        goto(x_cor+2*cell_size,y_cor)
        penup()
        
        fillcolor('light grey')
        begin_fill()
        pendown()
        goto(x_cor+(cell_size*1.25),y_cor-(cell_size-cell_size/3))
        setheading(0)
        forward(70)
        goto(x_cor+25,y_cor-90)
        end_fill()
        #--------- ----------------- -----------#

    def big_tile_B():
        
        diagonal=sqrt(2)*(2*cell_size)
        restore_settings()
        width(3)
        goto(x_cor,y_cor-cell_size)
        setheading(45)
        pendown()
        forward(diagonal)
        back(diagonal/4)

       
        fillcolor('light grey')
        begin_fill()
        goto(x_cor+(2*cell_size-50),y_cor-cell_size)
       
        penup()
        
        pendown()
        setheading(180)

        
        goto(x_cor+30,y_cor-70)
        end_fill()
        
        #--------- ----------------- -----------#


    ## Defining a function for making the legends
        
    def legends():

        # small tile ( India gate)
         penup()
         goto(-700,100)
         small_tile()
         
        # wide tile (Brisbane skyline)
         penup()
         goto(600,100)
         wide_tile()
         

        # tall tile (Eifell tower)
         penup()
         goto(-700,-100)
         tall_tile()

        
        # Big tile ()
         penup()
         goto(600,-100)
         big_tile()

         # Labelling the legends 
         restore_settings()

         goto(-650,-320)
         write('Eiffel Tower',align='center',font=('Times New Roman',12))

         goto(700,-20)
         write('Brisbane skyline',align='center',font=('Times New Roman',12))

         goto(-650,-20)
         write('India Gate',align='center',font=('Times New Roman',12))

         goto(700,-320)
         write('Taj Mahal',align='center',font=('Times New Roman',12))
         
                
        #--------- ------------ ------------- ------------ ------------- #
        
   ## decoding the canvas -
         
    for tile in range(len(given_pattern)):
        
        width(0)
        the_exact=given_pattern[tile] # reading the pattern

        # detailing x and y co-ordinates
        x=[-500,-400,-300,-200,-100,0,100,200,300,400] 
        y=[-250,-150,-50,50,150,250,350]

        # using the canvas to form lists 
        num=['1','2','3','4','5','6','7']
        alphabet=['A','B','C','D','E','F','G','H','I','J']

        # looping till the end of the given pattern

        for cord in range(len(alphabet)):

            # reading and assigning the given pattern co-ordinates from the list

            if the_exact[0][0]==alphabet[cord]:
                x_cor=x[cord]
               
        for co_ord in range(len(num)):
            if the_exact[0][1]==num[co_ord]:     
                y_cor=y[co_ord]

            # looking what size tile is  to be drawn based on the length of the item in the list index

                
        if len(the_exact)==2  : #samll tile
            penup()
            goto(x_cor,y_cor)
            small_tile()
            if the_exact[len(the_exact)-1]=='X':# checking if the tile is broken or not 
                small_tile_B()
            
            
        if len(the_exact)==3:   
            tall=the_exact[1][0]

        # differentiating between tall and wide tile 
            
            if the_exact[0][0]==tall: #tall tile
                penup()
                goto(x_cor,y_cor+cell_size)
                tall_tile()
                if the_exact[len(the_exact)-1]=='X':
                    tall_tile_B()
                    
                
            else: # Wide tile
               
                penup()
                
                goto(x_cor,y_cor)
                setheading(0)
                wide_tile()
                if the_exact[len(the_exact)-1]=='X':
                    wide_tile_B()
                
            
        if len(the_exact)==5: # Big tile
            penup()
            
            goto(x_cor,y_cor+cell_size)
            setheading(0)
            big_tile()
            if the_exact[len(the_exact)-1]=='X':
                big_tile_B()


               #--------- ----------------- -----------#


    penup()
    
   # calling the function to form the legends 
    legends()
        
    
    


#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing your solution.  Do not change any of this code except
# as indicated by the comments marked '*****'.
#

# Set up the drawing canvas
# ***** You can change the background and line colours, and choose
# ***** whether or not to draw the grid and mark the places for the
# ***** legend, by providing arguments to this function call
create_drawing_canvas()

# Control the drawing speed
# ***** Change the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** forever while the cursor moves slowly around the screen
tracer(False)

# Give the drawing canvas a title
# ***** Replace this title with a description of your solution's theme
# ***** and its tiles
title("STRUCTURES : Appreciating architects and engineers")

### Call the student's function to follow the path
### ***** While developing your program you can call the tessellate
### ***** function with one of the "fixed" data sets, but your
### ***** final solution must work with "random_pattern()" as the
### ***** argument.  Your tessellate function must work for any data
### ***** set that can be returned by the random_pattern function.
#tessellate() # <-- used for code development only, not marking
tessellate(random_pattern()) # <-- used for assessment

# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible at the end of the
# ***** program as a debugging aid
release_drawing_canvas()

#
#--------------------------------------------------------------------#
