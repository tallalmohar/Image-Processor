# CMPT 120 Yet Another Image Processer
# Starter code for cmpt120imageManip.py
# Author(s): Tallal Mohar,Brandon wan 
# Date: 
# Description:

import cmpt120imageProjHelper
import numpy



### red filter
def applyRedFilter(pixels):
  height = len(pixels)
  width = len(pixels[0])
  for row in range(height):
    for column in range(width):
      ### sets every color other then red to 0 
      pixels[row][column][1] = 0
      pixels[row][column][2] = 0
  return pixels

### green filter
def applyGreenFilter(pixels):
  height = len(pixels)
  width = len(pixels[0])
  for row in range(height):
    for column in range(width):
       ### sets every color other then green to 0 
      pixels[row][column][0]=0
      pixels[row][column][2]= 0
  return pixels

### blue filter
def applyBlueFilter(pixels):
  height = len(pixels)
  width = len(pixels[0])
  for row in range(height):
    for column in range(width):
      pixels[row][column][0]=0
      pixels[row][column][1]=0
  return pixels


###Sepia color 
def applySepiaFilter(pixels):
  height = len(pixels)
  width = len(pixels[0])
  for row in range(height):
    for column in range(width):
      red = pixels[row][column][0]
      green = pixels[row][column][1]
      blue = pixels[row][column][2]

      SepiaRed = (red * .393) + (green *.769) + (blue * .189)
      SepiaGreen = (red * .349) + (green *.686) + (blue * .168)
      SepiaBlue = (red * .272) + (green *.534) + (blue * .131)  

      if SepiaRed > 255:
        SepiaRed = min(255,SepiaRed)
      if SepiaGreen > 255:
        SepiaGreen = min(255,SepiaGreen)
      if SepiaBlue > 255:
        SepiaBlue = min(255,SepiaBlue)
      
      pixels[row][column][0] = SepiaRed
      pixels[row][column][2]=SepiaBlue
      pixels[row][column][1]= SepiaGreen
  return pixels

###Warm Filter
def applyWarmFilter(pixels):
  height = len(pixels)
  width = len(pixels[0])
  for row in range(height):
    for column in range(width):
      red = pixels[row][column][0]
      green = pixels[row][column][1]
      blue = pixels[row][column][2]

      if red < 64:
        scaledup_red = int(red/(64*80))
      elif red >= red and red < 128:
        scaledup_red = int(((red-64)/(128-64))*((160-80))+80)
      else:
        scaledup_red= int(((red-128)/(255-128))*((255-160))+160)
      
      if blue < 64:
        scaleddown_blue = int(blue/(64*50))
      elif blue >= blue and blue < 128:
        scaleddown_blue = int(((blue-64)/(128-64))*((100-50))+50)
      else:
        scaleddown_blue = int(((blue-128)/(255-128))*((255-100))+100)

      pixels[row][column]=[scaledup_red,green,scaleddown_blue]
      
###scale up / scale down values for cold filter
def scaleup(num):
  if num < 64:
      return int(num/(64*80))
  elif num >= 64 and num < 128:
    return int(((num-64)/(128-64))*((160-80))+80)
  else:
     return int(((num-128)/(255-128))*((255-160))+160)

def scaledown(num):
  if num < 64:
    return int(num/(64*50))
  elif num >= 64 and num < 128:
    return  int(((num-64)/(128-64))*((100-50))+50)
  else:
    return int(((num-128)/(255-128))*((255-100))+100)


def applyColdFilter(pixels):
  height = len(pixels)
  width = len(pixels[0])
  for row in range(height):
    for column in range(width):
      pixels[row][column][0]=scaleup(pixels[row][column][0])
      pixels[row][column][2]=scaledown(pixels[row][column][2])
  return pixels

### rotate left
def rotate_left(pixels):
  height = len(pixels)
  width = len(pixels[0])
  black_box = cmpt120imageProjHelper.getBlackImage(height,len(pixels[0]) )
  for row in range(height):
    for column in range(len(pixels[0])):
      width = len(pixels[0]) - 1
      black_box[column][row] = pixels[row][width-column]
  return black_box

### rotate right
def rotate_right(pixels):
  height = len(pixels)
  width = len(pixels[0])
  black_box = cmpt120imageProjHelper.getBlackImage(len(pixels),width)
  for row in range(len(pixels)):
    for column in range(width):
      height = len(pixels) - 1
      black_box[column][row] = pixels[height-row][column]
  return black_box

### double up the size
def double_image(pixels):
  height = len(pixels)
  width = len(pixels[0])
  black_box = cmpt120imageProjHelper.getBlackImage(width*2,height*2)
  for row in range(height):
    for column in range(width):
      black_box[row*2][column*2]=pixels[row][column]
      black_box[row*2+1][column*2]=pixels[row][column]
      black_box[row*2][column*2+1]=pixels[row][column]
      black_box[row*2+1][column*2+1]=pixels[row][column]
  return black_box

###half the size
def halfsize_image(pixels):
  height = len(pixels)
  width = len(pixels[0])
 
  black_box = cmpt120imageProjHelper.getBlackImage(int(width/2),int(height/2))
  for row in range(0,height,2):
    for column in range(0,width,2):
      average_red = (pixels[row][column][0] + pixels[row+1][column][0] + pixels[row][column+1][0] + pixels[row+1][column+1][0])/4
      average_green=(pixels[row][column][1] + pixels[row+1][column][1] + pixels[row][column+1][1] + pixels[row+1][column+1][1])/4
      average_blue = (pixels[row][column][2] + pixels[row+1][column][2] + pixels[row][column+1][2] + pixels[row+1][column+1][2])/4
      black_box[int(row/2)][int(column/2)] = [average_red, average_green, average_blue]
  return black_box

### locate fish
def locatefish(pixels):
  height = len(pixels)
  width = len(pixels[0])
  base_row = []
  base_column = []
  for row in range(height):
    for column in range(width):
      r,g,b = pixels[row][column]
      h,s,v = cmpt120imageProjHelper.rgb_to_hsv(r,g,b)
      mh,ms,mv = int(h),int(s),int(v)
      if mh in range(51,95) and ms in range(40,60) and mv in range(49,100):
        base_row.append(row)
        base_column.append(column)
  min_column = min(base_column)
  max_column = max(base_column)
  min_row = min(base_row)
  max_row = max(base_row)
  for mcolumn in range(min_column, max_column):
    pixels[min_row][mcolumn] = [0,255,0]
    pixels[max_row][mcolumn] = [0,255,0]
  for crow in range(min_row,max_row):
    pixels[crow][min_column] = [0,255,0]
    pixels[crow][max_column] = [0,255,0]
  return pixels

        
  