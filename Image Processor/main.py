# Author(s): Tallal Mohar, Brandon Wan
# Date:
# Description:

import cmpt120imageProjHelper
import cmpt120imageManip
import tkinter.filedialog
import pygame
pygame.init()

# list of system options
# ***TO-DO: populate it to provide more functionalities***
system = [
            "Q: Quit",
            "O: Open Image",
            "S: Save Current Image",
            "R: Reload Original Image"
         ]

# list of basic operation options
# ***TO-DO: populate it to provide more functionalities***
basic = [
          
          "1: Apply Red Filter",
          "2: Apply Green Filter",
          "3: Apply Blue Filter",
          "4: Apply Sepia Filter",
          "5: Apply Warm Filter",
          "6: Apply Cold Filter",
          "7: Switch to Advanced Functions"
         ]

# list of advanced operation options
# ***TO-DO: populate it to provide more functionalities***
advanced = [
                "1: Rotate Left",
                "2: Rotate Right",
                "3: Double Size",
                "4: Half Size",
                "5: Locate Fish",
                "6: Switch to Basic Functions"
             ]

# a helper function that generates a list of strings to be displayed in the interface
def generateMenu(state):
    """
    Input:  state - a dictionary containing the state values of the application
    Returns: a list of strings, each element represets a line in the interface
    """
    menuString = ["Welcome to Image Processer!"]
    menuString.append("") # an empty line
    menuString.append("Choose the following options:")
    menuString.append("") # an empty line
    menuString += system
    menuString.append("") # an empty line

    # build the list differently depending on the mode attribute
    if state["mode"] == "basic":
        menuString.append("--Basic Mode--")
        menuString += basic
        menuString.append("")
        menuString.append("Enter your choice Q/O/S/R or 1-7")
    elif state["mode"] == "advanced":
        menuString.append("--Advanced Mode--")
        menuString += advanced
        menuString.append("")
        menuString.append("Enter your choice Q/O/S/R or 1-7")
    else:
        menuString.append("Error: Unknown mode!")

    return menuString

# a helper function that returns the result image as a result of the operation chosen by the user
# it also updates the state values when necessary (e.g, the mode attribute if the user switches mode)
def handleUserInput(state, image):
    """
    Input:  state - a dictionary containing the state values of the application
            img - the 2d array of RGB values to be operated on
    Returns: the 2d array of RGB vales of the result image of an operation chosen by the user
    """
    userInput = state["lastUserInput"].upper()
    # handle the system functionalities
    if userInput.isalpha(): # check if the input is an alphabet
        print("Log: Doing system functionalities " + userInput)
        if userInput == "Q": # this case actually won't happen, it's here as an example
            print("Log: Quitting...")
        # ***TO-DO: add the rest to handle other system functionalities***
        elif userInput == "O":
          print("Open Image")
          tkinter.Tk().withdraw()
          Open_Filename = tkinter.filedialog.askopenfilename()
          image = cmpt120imageProjHelper.getImage(Open_Filename)
          cmpt120imageProjHelper.showInterface(image,Open_Filename,generateMenu(state))
        elif userInput == "S":
          print("Save Image")
          tkinter.Tk().withdraw()
          Save_Filename = tkinter.filedialog.asksaveasfilename()
          cmpt120imageProjHelper.saveImage(image,Save_Filename)
        elif userInput == "R":
          print("Reload Original Image")
          image = cmpt120imageProjHelper.getImage("project-photo.jpg")
          cmpt120imageProjHelper.showInterface(image, "Reload Image",generateMenu(state))

    # or handle the manipulation functionalities based on which mode the application is in
    elif userInput.isdigit(): # has to be a digit for manipulation options
        print("Log: Doing manipulation functionalities " + userInput)
        # ***TO-DO: add the rest to handle other manipulation functionalities***
        if state["mode"] == "basic":
            if userInput == "1":
                print("Log: Performing " + basic[int(userInput)-1])
                cmpt120imageManip.applyRedFilter(image)
                cmpt120imageProjHelper.showInterface(image,"Apply Red Filter",generateMenu(state))
            elif userInput == "2":
              print("Log: Performing " + basic[int(userInput)-1])
              cmpt120imageManip.applyGreenFilter(image)
              cmpt120imageProjHelper.showInterface(image,"Apply Green Filter", generateMenu(state))
            elif userInput == "3":
              print("Log: Performing " + basic[int(userInput)-1])
              cmpt120imageManip.applyBlueFilter(image)
              cmpt120imageProjHelper.showInterface(image,"Apply Blue Filter", generateMenu(state))
            elif userInput == "4":
              print("Log: Performing " + basic[int(userInput)-1])
              cmpt120imageManip.applySepiaFilter(image)
              cmpt120imageProjHelper.showInterface(image,"Apply Sepia Filter", generateMenu(state))
            elif userInput == "5":
              print("Log: Performing " + basic[int(userInput)-1])
              cmpt120imageManip.applyWarmFilter(image)
              cmpt120imageProjHelper.showInterface(image,"Apply Warm Filter", generateMenu(state))
            elif userInput == "6":
              print("Log: Performing " + basic[int(userInput)-1])
              cmpt120imageManip.applyColdFilter(image)
              cmpt120imageProjHelper.showInterface(image,"Apply Cold Filter", generateMenu(state))
            elif userInput == "7":
              print("Log: Performing " + basic[int(userInput)-1])
              state["mode"] = "advanced"
              cmpt120imageProjHelper.showInterface(image,"Advanced Mode", generateMenu(state))

        if state["mode"] == "advanced":
            if userInput == "1":
              print("Log: Preforming " + advanced[int(userInput)-1])
              image = cmpt120imageManip.rotate_left(image)
              cmpt120imageProjHelper.showInterface(image, "Rotate Left",generateMenu(state))
            elif userInput == "2":
              print("Log: Preforming " + advanced[int(userInput)-1])
              image = cmpt120imageManip.rotate_right(image)
              cmpt120imageProjHelper.showInterface(image, "Rotate Right",generateMenu(state))
            elif userInput == "3":
              print("Log: Preforming " + advanced[int(userInput)-1])
              image = cmpt120imageManip.double_image(image)
              cmpt120imageProjHelper.showInterface(image, "Double-Size",generateMenu(state))
            elif userInput == "4":
              print("Log: Preforming " + advanced[int(userInput)-1])
              image = cmpt120imageManip.halfsize_image(image)
              cmpt120imageProjHelper.showInterface(image, "Half-Size",generateMenu(state))
            elif userInput == "5":
              print("Log: Performing " + advanced[int(userInput)-1])
              cmpt120imageManip.locatefish(image)
              cmpt120imageProjHelper.showInterface(image,"Fish",generateMenu(state))
            elif userInput == "6":
              print("Log: Performing " + advanced[int(userInput)-1])
              state["mode"] = "basic"
              cmpt120imageProjHelper.showInterface(image,"Basic Mode",generateMenu(state))
                # ***TO-DO: use this format when you add the manipulation functionalities***
                # ***instead of setting the value of state["mode"]***
                # ***it is ok to go a bit beyond 100 characters when calling the showUserInterface***
                #img = cmpt120imageManip.applyRedFilter(img)
                #cmpt120imageProjHelper.showUserInterface(img, "Apply Red Filter ", generateMenu(state))

    else: # unrecognized user input
        print("Log: Unrecognized user input: " + userInput)
    return image

# *** DO NOT change any of the code below this point ***

# use a dictionary to remember several state values of the application
appStateValues = {
                    "mode": "basic",
                    "lastOpenFilename": "",
                    "lastSaveFilename": "",
                    "lastUserInput": ""
                 }

currentImg = cmpt120imageProjHelper.getBlackImage(300, 200) # create a default 300 x 200 black image
cmpt120imageProjHelper.showInterface(currentImg, "No Image", generateMenu(appStateValues)) # note how it is used

# ***this is the event-loop of the application. Keep the remainder of the code unmodified***
keepRunning = True
# a while-loop getting events from pygame
while keepRunning:
    ### use the pygame event handling system ###
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            appStateValues["lastUserInput"] = pygame.key.name(event.key)
            # prepare to quit the loop if user inputs "q" or "Q"
            if appStateValues["lastUserInput"].upper() == "Q":
                keepRunning = False
            # otherwise let the helper function handle the input
            else:
                currentImg = handleUserInput(appStateValues, currentImg)
        elif event.type == pygame.QUIT: #another way to quit the program is to click the close botton
            keepRunning = False

# shutdown everything from the pygame package
pygame.quit()

print("Log: Program Quit")