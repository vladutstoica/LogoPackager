# File name convention
#
# BrandName_VERSION_ColorProfiles_Color_optionals
#
# (ex. "Hotshot_HorizontalLogo_RGB_FullColor_1200.jpg")
#
# VERSION : "HorizontalLogo",
#           "HorizontalLogoNoTagLine",
#           "VerticalLogo",
#           "VerticalLogoNoTagLine",
#           "Logomark",
#           "Wordmark",
#           "WordmarkNoTagLine",
#           "TagLine"
#
# COLORPROFILES : "RGB",
#                 "CMYK"
#
# COLOR : "FullColor",
#         "Black",
#         "White",
#         "Inverted"
#
# optionals  (ex. "Hotshot_HorizontalLogo_RGB_FullColor_1200.jpg")

# import the os module
import os
import re
import shutil

# detect the current working directory and print it
path = os.getcwd()
print('\n The current working directory is %s \n' % path)

brand = 'none'
version = 'none'
colorProfiles = 'none'
color = 'none'

cmykFolderName = 'Print'
artboardsFolderName = 'Artboards'

success = 0
failed = 0

entries = os.listdir()


def splitName():
    global filename

    global brand
    global version
    global colorProfiles
    global color

    if extension != '.py':
        filename = re.split(r'[_.]', entry)
        brand = filename[0]
        if len(filename) == 5:
            version = filename[1]
            colorProfiles = filename[2]
            color = filename[3]


def createDir():
    global success
    global failed

    if not os.path.exists(cmykPath) and colorProfiles == 'CMYK':
        try:
            os.makedirs(cmykPath)
        except OSError:
            print('Creation of the directory %s failed' % cmykPath)
            failed = failed + 1
        else:
            print('Successfully created the directory \%s' % cmykPath)
            success = success + 1


def createArtboardsDir():
    global success
    global failed

    if not os.path.exists(artboardsPath):
        try:
            os.makedirs(artboardsPath)
        except OSError:
            print('Creation of the directory %s failed' % artboardsPath)
            failed = failed + 1
        else:
            print('Successfully created the directory \%s' % artboardsPath)
            success = success + 1


def moveFiles():
    if colorProfiles == 'CMYK':
        shutil.move(entry, cmykPath)


def moveArtboards():
    shutil.move(entry, artboardsPath)


for entry in entries:
    root, extension = os.path.splitext(entry)
    splitName()

    cmykPath = cmykFolderName + '\\' + version + '\\' + color
    artboardsPath = cmykFolderName + '\\' + artboardsFolderName

    if extension != '.py':
        if len(filename) == 2:
            print("to be continued")
            # RGB and CMYK artboards have the same name!!!!
            createArtboardsDir()
            moveArtboards()

        if version != 'none' and colorProfiles != 'none' and color != 'none':
            createDir()
            moveFiles()

    print(brand, version, colorProfiles, color)

# final statistics
print('\n Statistics: \n')
print('Successfully created %d folders!' % success)
print('%d fails creating folders!' % failed)
