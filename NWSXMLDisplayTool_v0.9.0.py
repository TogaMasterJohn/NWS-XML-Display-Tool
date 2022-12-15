"""
TogaMasterJohn/StormSpotterJohn, 2022

NWS XML Display Tool, version 0.9.0

This tool displays some NWS Current Observation XML files. Not all stations' files are supported at this time.

"""

# "tkinter" is used for the GUI, "xml.etree.ElementTree" is used for parsing XML data... so nice!
import tkinter.filedialog #MUST be loaded in first!
from tkinter import Canvas
from tkinter import ttk
import tkinter as tk
import xml.etree.ElementTree as et #included with Python
from PIL import ImageTk, Image


#exit the program
def exitProgram():
    main.mainwindow.destroy()


#get the weather picture information and display it
def displayWeatherPic():
    #make the weather icon url/file name a string
    weatherPicName = str(gatherData.obs_weatherpic[0]) #used to store the weather picture's name

    #need to use a GIF version of the file, so we change the extension
    pngToGIFString = "gif" #used to change the extension from PNG to GIF
    weatherPicLocation = "WeatherIconsGIF/" + weatherPicName #used to store the weather graphic's location
    weatherPicLocationSize = len(weatherPicLocation) #stores the length (in characters) of the weather graphic's location path
    weatherPicLocation = weatherPicLocation.replace(weatherPicLocation[weatherPicLocationSize - 3:], pngToGIFString) #now contains the updated location and extension

    #build the weather picture and append it
    weatherPic = Image.open(weatherPicLocation) #opens the weather graphic
    weatherPicImage = ImageTk.PhotoImage(weatherPic) #stores the weather graphic
    weatherPicLabel = tk.Label(
        main.mainwindow,
        text = str(gatherData.obs_weather[0]),
        image = weatherPicImage,
        compound = "top",
        bg = "#EBF7FD"
        ) #stores the necessary values for the weather graphic label
    weatherPicLabel.image = weatherPicImage #attaches the weather graphic to the weather graphic label
    weatherPicLabel.place(x = 120, y = 290) #places the weather graphic in the main.mainwindow
    #0058A6
    #E0F2FB

    

#make the strings, make the labels, make and display the background, and display the labels
def displayValues():
    #make the strings
    obsCurrentConditions = "Current Conditions" #stores the Current Conditions label in a string
    obsLocation = str(gatherData.obs_location[0]) #stores the location in a string
    obsStationIdLatLon = "(" + str(gatherData.obs_stationid[0]) + ")   " + str(gatherData.obs_latitude[0]) + " " + str(gatherData.obs_longitude[0]) #stores the station ID and coordinates in a string
    obsObservationTime = str(gatherData.obs_observationtime[0]) + "   (" + str(gatherData.obs_observationtime_rfc822[0]) + ")" #stores the observation time
    obsWeather = "Weather: " + str(gatherData.obs_weather[0]) #stores the current weather observation in a string
    obsTemperature = "Temperature: " + str(gatherData.obs_temperature[0]) #stores the temperature in a string
    obsDewpoint = "Dewpoint: " + str(gatherData.obs_dewpoint[0]) #stores the dewpoint in a string
    obsRelativeHumidity = "Relative Humidity: " + str(gatherData.obs_relativehumidity[0]) #stores the relative humidity in a string
    obsWindString = "Wind: " + str(gatherData.obs_windstring[0]) #stores the wind information in a string
    obsVisibility = "Visibility: " + str(gatherData.obs_visibility[0]) #stores the visibility information in a string
    obsPressure = "Barometric Pressure: " + str(gatherData.obs_pressure[0]) #stores the barometric pressure in a string

    #make the labels
    obsCurrentConditionsLabel = tk.Label(text = obsCurrentConditions, bg = "#AFDEF7", font = ("Arial, 21")) #current observations label
    obsLocationLabel = tk.Label(text = obsLocation, bg = "#AFDEF7", font = ("Arial, 17")) #location label
    obsStationIdLatLonLabel = tk.Label(text = obsStationIdLatLon, bg = "#AFDEF7", font = ("Arial, 13")) #station ID and coordinates labe;
    obsObservationTimeLabel = tk.Label(text = obsObservationTime, bg = "#AFDEF7", font = ("Arial, 11")) #observation time label
    obsWeatherLabel = tk.Label(text = obsWeather, bg = "#AFDEF7", font = ("Arial, 13")) #weather condition label
    obsTemperatureLabel = tk.Label(text = obsTemperature, bg = "#AFDEF7", font = ("Arial, 13")) #temperature label
    obsDewpointLabel = tk.Label(text = obsDewpoint, bg = "#AFDEF7", font = ("Arial, 13")) #dewpoint label
    obsRelativeHumidityLabel = tk.Label(text = obsRelativeHumidity, bg = "#AFDEF7", font = ("Arial, 13")) #relative humidity label
    obsWindStringLabel = tk.Label(text = obsWindString, bg = "#AFDEF7", font = ("Arial, 13")) #wind information label
    obsVisibilityLabel = tk.Label(text = obsVisibility, bg = "#AFDEF7", font = ("Arial, 13")) #visibility label
    obsPressureLabel = tk.Label(text = obsPressure, bg = "#AFDEF7", font = ("Arial, 13")) #pressure label

    #display the labels
    obsCurrentConditionsLabel.place(x = 90, y = 110)
    obsLocationLabel.place(x = 90, y = 145)
    obsStationIdLatLonLabel.place(x = 90, y = 175)
    obsObservationTimeLabel.place(x = 90, y = 198)
    obsWeatherLabel.place(x = 340, y = 280)
    obsTemperatureLabel.place(x = 340, y = 305)
    obsDewpointLabel.place(x = 340, y = 330)
    obsRelativeHumidityLabel.place(x = 340, y = 355)
    obsWindStringLabel.place(x = 340, y = 380)
    obsVisibilityLabel.place(x = 340, y = 405)
    obsPressureLabel.place(x = 340, y = 430)
    #now display the picture information (icon url/file name)
    displayWeatherPic()



#parse, make the necessary lists, and gather the data
def gatherData():
    #parse!
    tree = et.parse(openFileWindow.filename) #stores the xml file's tree
    root = tree.getroot() #stores the xml file's roots
    
    #define the namespaces from the XML file, as not doing so makes it difficult to parse the data
    et.register_namespace("xsd", "http://www.w3.org/2001/XMLSchema")
    et.register_namespace("xsi", "http://www.w3.org/2001/XMLSchema-instance")
    et.register_namespace("xsi", "http://www.weather.gov/view/current_observation.xsd")
    
    #lists for the values
    gatherData.obs_location = [] #list for location
    gatherData.obs_stationid = [] #list for station ID
    gatherData.obs_latitude = [] #list for latitude
    gatherData.obs_longitude = [] #list for longitude
    gatherData.obs_observationtime = [] #list for observation time
    gatherData.obs_observationtime_rfc822 = [] #list for observation time (rfc822)
    gatherData.obs_weather = [] #list for current weather observation
    gatherData.obs_temperature = [] #list for temperature
    gatherData.obs_relativehumidity = [] #list for relative humidity
    gatherData.obs_windstring = [] #list for wind information
    gatherData.obs_pressure = [] #list for pressure
    gatherData.obs_dewpoint = [] #list for dewpoint
    gatherData.obs_visibility = [] #list for visibility
    gatherData.obs_weatherpic = [] #list for the weather graphic
    
    #get the values and store them in their respective list
    for obslocation in root.iter("location"):
        gatherData.obs_location.append(obslocation.text)
    for obsstationid in root.iter("station_id"):
        gatherData.obs_stationid.append(obsstationid.text)
    for obslatitude in root.iter("latitude"):
        gatherData.obs_latitude.append(obslatitude.text)
    for obslongitude in root.iter("longitude"):
        gatherData.obs_longitude.append(obslongitude.text)
    for obsobservationtime in root.iter("observation_time"):
        gatherData.obs_observationtime.append(obsobservationtime.text)
    for obsobservationtime_rfc822 in root.iter("observation_time_rfc822"):
        gatherData.obs_observationtime_rfc822.append(obsobservationtime_rfc822.text)
    for obsweather in root.iter("weather"):
        gatherData.obs_weather.append(obsweather.text)
    for obstemperature in root.iter("temperature_string"):
        gatherData.obs_temperature.append(obstemperature.text)
    for obsrelativehumidity in root.iter("relative_humidity"):
        gatherData.obs_relativehumidity.append(obsrelativehumidity.text)
    for obswindstring in root.iter("wind_string"):
        gatherData.obs_windstring.append(obswindstring.text)
    for obspressure in root.iter("pressure_in"):
        gatherData.obs_pressure.append(obspressure.text)
    for obsdewpoint in root.iter("dewpoint_string"):
        gatherData.obs_dewpoint.append(obsdewpoint.text)
    for obsvisibility in root.iter("visibility_mi"):
        gatherData.obs_visibility.append(obsvisibility.text)
    #get the weather picture info (icon url/file name)
    for obsweatherpic in root.iter("icon_url_name"):
        gatherData.obs_weatherpic.append(obsweatherpic.text)
    #go to displayValues
    displayValues()



#open a window containing useful links
def openUsefulLinksWindow():
    usefulLinksWindow = tk.Toplevel() #useful links window
    usefulLinksWindow.title("Useful Links")
    usefulLinksWindow.geometry("420x240")
    usefulLinksWindow["background"] = "#AFDEF7"
    usefulLinksNWS1Label = tk.Label(
        master=usefulLinksWindow,
        text = "\n\n\nGet your local forecast from the National Weather Service!",
        font = ("Arial", 10),
        bg = "#AFDEF7"
        ) #label for the NWS forecast message
    usefulLinksNWS1Label.pack()
    usefulLinksNWS1UrlLabel = tk.Label(
        master=usefulLinksWindow,
        text = "https://www.weather.gov",
        font = ("Arial", 10),
        bg = "#AFDEF7"
        ) #label for the NWS's website link/URL
    usefulLinksNWS1UrlLabel.pack()
    usefulLinksNWS2LinkLabel = tk.Label(
        master=usefulLinksWindow,
        text = "\n\n\n\nView the national radar!",
        font = ("Arial", 10),
        bg = "#AFDEF7"
        ) #label for the NWS radar message
    usefulLinksNWS2LinkLabel.pack()
    usefulLinksNWS2UrlLabel = tk.Label(
        master=usefulLinksWindow,
        text = "https://radar.weather.gov/region/conus/standard",
        font = ("Arial", 10),
        bg = "#AFDEF7"
        ) #label for the NWS's radar link/URL
    usefulLinksNWS2UrlLabel.pack()



#open file window so user can select their XML file                                                                                                                                                                                                                                                                                                                                                                          
def openFileWindow():
    openFileWindow.filename = tk.filedialog.askopenfilename(
        title = "Open XML File",
        initialdir = "/",
        filetypes = [("XML files", "*.xml")]
        ) #open file window
    gatherData()



# setup the main window
def main():
    main.mainwindow = tk.Tk() #main window
    main.mainwindow.title("NWS XML Display Tool")
    main.mainwindow.geometry('800x600')
    #main.mainwindow.iconbitmap("ThunderIcon.ico") #does not work for some reason currently
    main.mainwindow["background"] = "#AFDEF7"
    
    #setup the main buttons
    openInfoWindow = tk.Button(
        master = main.mainwindow,
        text = "Useful Links",
        width = 12,
        height = 2,
        bg = "#0058A6",
        fg = "white",
        command=openUsefulLinksWindow
        ) #button - opens the Useful Links window
    openXMLFile = tk.Button(
        master = main.mainwindow,
        text = "Open XML File",
        width = 12,
        height = 2,
        bg = "#0058A6",
        fg = "white",
        command=openFileWindow
        ) #button - opens the Open XML File window
    exitProgramBtn = tk.Button(
        master = main.mainwindow,
        text = "Exit",
        width = 12,
        height = 2,
        bg = "#0058A6",
        fg = "white",
        command=exitProgram
        ) #button - closes the program
    
    #setup the main window buttons
    openInfoWindow.place(x = 90, y = 550)
    openXMLFile.place(x = 350, y = 550)
    exitProgramBtn.place(x = 590, y = 550)
    
    #setup the main window contents
    programNameLabel = tk.Label(
        text = "National Weather Service XML Display Tool",
        font = ("Arial", 27),
        bg = "#AFDEF7"
        ) #label for the program name
    programNameLabel.pack()
    programVersionLabel = tk.Label(
        text = "version 0.9.0 - under construction, please mind the dust!",
        font = ("Arial", 16),
        bg = "#AFDEF7"
        ) #label for the version number and other information
    programVersionLabel.pack()
    programDisclaimerLabel = tk.Label(
        text = "This program is not affiliated with the National Oceanic and Atmospheric Administration or the National Weather Service.",
        font = ("Arial", 8),
        bg = "#AFDEF7"
        ) #label for the disclaimer
    programDisclaimerLabel.pack()

    #build program logo and display it
    programLogo = Image.open("Thunder.gif") #opens the program logo
    programLogoImage = ImageTk.PhotoImage(programLogo) #stores the program logo
    programLogoImageLabel = tk.Label(
        main.mainwindow,
        image = programLogoImage,
        bg = "#AFDEF7"
        ) #program logo label
    programLogoImageLabel.place(x = 30, y = 40)
    
    # run main loop
    main.mainwindow.mainloop()

    

#start program
if __name__ == "__main__":
    main()


