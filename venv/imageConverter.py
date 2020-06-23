import sys,os
from PIL import Image

'''

How to use this script in the comad prompr (or Terminal) : python imageConverter.py input_folder_name/ output_folder_name/  to_which_format

Example: python imageConverter.py images/ new/  png

'''

#handling errors with try and expect
try:


    input_folder = sys.argv[1] #inpt folder
    output_folder = sys.argv[2] #output folder
    new_format = sys.argv[3] #the image new format


    #checking if the destination folder exist
    if not os.path.isdir(output_folder):
        os.makedirs(output_folder)


    #looping, getting files from the input folder
    for file_name in os.listdir(input_folder) :

        #dividing the filename in pairs so that ican be easy to save it
        clean_name = os.path.splitext(file_name)[0]

        #using PiLL module to open and save the image in to output folder
        current_image = Image.open(f'{input_folder}{file_name}')
        if not os.path.isfile(f'{output_folder}{clean_name}.{new_format}') :
            current_image.save(f'{output_folder}{clean_name}.{new_format}', f'{new_format}')
        else:
            print(f'{clean_name}.{new_format} already exist in {output_folder} ')

except (IndexError) as err:
    print('Please recheck your files and folder names and make sure you have 3 arguments after imageConverter.py ')
else:
    print('Files converted, check your destinaion folder please !')


