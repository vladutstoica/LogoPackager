# LogoPackager
Auto generate logo end-files for clients. 

## NAME CONVENTION

```
BRANDNAME_VERSION_COLORPROFILES_COLOR_optionals
```

```
VERSION : "HorizontalLogo",
          "HorizontalLogoNoTagLine",
          "VerticalLogo",
          "VerticalLogoNoTagLine",
          "Logomark",
          "Wordmark",
          "WordmarkNoTagLine",
          "TagLine"
```

```
COLORPROFILES : "RGB",
                "CMYK"
```

```
COLOR : "FullColor",
        "Black",
        "White",
        "Inverted"
```

optionals  (ex. "BRANDNAME_HorizontalLogo_RGB_FullColor_1200.jpg")

(ex. "LogoPackager_HorizontalLogo_RGB_FullColor_1200.jpg")

## QUICK GUIDE
1. Create logo design in Illustrator;
2. Open "Logo_ExportTemplate_RGB.ait" OR "Logo_ExportTemplate_CMYK.ait" and place all logo variants you need;
4. In Illustrator, File > Scripts > Other script... > "ArtboardCleaner.jsx"
5. Export logo variants into a empty folder (Ex. Digital: .JPG, .PNG, .AI, .EPS, .PDF, .SVG; Print: .AI, .EPS, .PDF); 
6. Execute "Logo_Sorting_RGB" OR "Logo_Sorting_CMYK".

#### :warning::warning::warning: IF YOU EXPORT ASSETS FOR BOTH RGB & CMYK, THEN YOU WILL HAVE TO MANUALLY MOVE THE ARTBOARDS FILE (NAMED "CompanyName.ai" for both RGB & CMYK) TO THE DESIRED FOLDER LOCATION.

FOR DETAILED STEPS PLEASE FOLLOW THE GUIDE BELOW:arrow_down::arrow_down::arrow_down:

## STEP-BY-STEP GUIDE

1. Here's an example of a logo with Logomark, Wordmark and TagLine;<br/><br/>
![image](https://user-images.githubusercontent.com/23508982/128331677-51c360ad-f7af-4d54-b5bf-9c5762ba832a.png)

2. Open "Logo_ExportTemplate_RGB.ait" and place the logo in the correct artboard, then create variants; (empty artboards will be automatically deleted on the future steps);<br/><br/>
![image](https://user-images.githubusercontent.com/23508982/128331432-4834d953-632e-4892-bd37-55590270a218.png)

3. In Illustrator, File > Scripts > Other script... > "ArtboardCleaner.jsx". This will crop artboards and delete empty ones.<br/><br/>
![image](https://user-images.githubusercontent.com/23508982/128331842-73f07bbb-96e6-4177-b1ad-e3bf3d859ad4.png)

4. On the export window, uncheck "Create subfolders", complete the brand name in the "Prefix:" field followed by an underscore (ex. "BrandName_"). "Suffix:" field represents logo optional settings and should start with an underscore followed by the setting name (ex. if we need a dedicated 1200px width for a cover placeholder, we can use optionals to export it: "_1200"). Export all artboards to an empty folder;<br/><br/>
(ex. "BRANDNAME_HorizontalLogo_RGB_FullColor_1200.jpg")
![image](https://user-images.githubusercontent.com/23508982/128333498-a7f5d356-0100-4d66-bf54-0faa294f3b46.png)

5. Place "Logo_Sorting_RGB.py" in the folder where you exported the artboards and run the .py file;<br/><br/>
![image](https://user-images.githubusercontent.com/23508982/128333210-7fa4adc3-acc0-464f-8a98-b46fec00498c.png)

6. Delete the .py file after the program end executing;<br/><br/>
![image](https://user-images.githubusercontent.com/23508982/128333311-ced9f8a3-62b7-409c-bb6c-813947fdcb4d.png)

7. Folder structure;<br/><br/>
![image](https://user-images.githubusercontent.com/23508982/128333647-78cfea75-2644-404b-8784-fb5f4990e29a.png)

8. Repeat the process for CMYK; You can export the artboards in the same folder where you exported the RGB artboards.

### TODO:
- make UI
- make name convention for artboards: BRANDNAME_ARTBOARD & BRANDNAME_ARTBOARD_EDITABLE
