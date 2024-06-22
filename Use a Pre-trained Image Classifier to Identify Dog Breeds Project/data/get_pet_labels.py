#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: HIBAH SINDI
# DATE CREATED: 22/06/2024                                 
# REVISED DATE: 22/06/2024
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """

    ## First, I will create the filenames of the images files with the os library (listdir)
    images_names = listdir(image_dir)
    # print("\nPrints 10 filenames from folder pet_images/")
    # for idx in range(0, 10, 1):
    #   print("{:2d} file: {:>25}".format(idx + 1, images_names[idx]) )


    ## Next, creating an empty dictionary with the name results_dic by using {} which means an empty dictionary
    results_dic = {}

    ## Creating a for loop to loop through each name of images from the file
    
    for i in range(0, len(images_names), 1):
      
      if images_names[i][0] != '.':
        # print(images_names[i])
        # print(images_names[i][0])
        ## Making the names lower and split each word from _
        names_formated = images_names[i].lower().split('_')
        # print(names_formated)

        #Creating an empty variable for pets' names
        pets = ""

        #Looping through each name that I have just formated
        for name in names_formated:
          # print(name)

          #Getting only the names without numbers and the .jpg formate of the images
          if name.isalpha():
            # print(name)

            pets += name + ' '
            # print(pets)
          pets = pets.strip()
          # print(pets)

          if images_names[i] not in results_dic:
            results_dic[images_names[i]] = pets
            # print(results_dic[images_names[i]])
            # print(len(results_dic))
            # print(results_dic)
          
          else: 
            print("** Warning: Key=", images_names[i],  "there is the same value in =", results_dic[images_names[i]], "**")
            print('Please try again later.')





      


    # Replace None with the results_dic dictionary that you created with this
    # function
    return results_dic


##This is just for checking the code     
get_pet_labels("pet_images/")