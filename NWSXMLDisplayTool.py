"""
TogaMasterJohn, 2025

NWS XML Display Tool, version 0.11.1

This tool displays most NWS Current Observation XML files.

Not all stations' files are supported at this time, but all files should open.


*TO DO*
- Expand window size (and implement grid placement?)
    - Update label rendering implementations
    - "Beautify" the window
- Implement icon across multiple mlatforms
- Implement file handling across multiple platforms
- Implement access to weather.gov
- Implement access to current observations page at weather.gov
- Implement forecast XML file viewing (?)
- Implement download and viewing of Current Observation XML files (?)
- Implement download and viewing of Forecast XML files (?)

"""

# "tkinter" is used for the GUI, "xml.etree.ElementTree" is used for parsing XML data
import tkinter.filedialog #MUST be loaded in first!
from tkinter import Canvas
from tkinter import ttk
import tkinter as tk
import xml.etree.ElementTree as et
import webbrowser
from PIL import ImageTk, Image


#global variables
filesOpened = 0


#exit the program
def exitProgram():
    main.mainwindow.destroy()



#get the weather picture information and display it
def displayWeatherPic():
    try:
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
    except: #if no "compatible" weather picture is available, do:
        weatherPicName = "unavailable.gif"
        weatherPicLocation = "WeatherIconsGIF/" + weatherPicName #used to store the weather graphic's location

        #build the unavailable weather picture and append it
        weatherPic = Image.open(weatherPicLocation) #opens the weather graphic
        weatherPicImage = ImageTk.PhotoImage(weatherPic) #stores the weather graphic
        weatherPicLabel = tk.Label(
            main.mainwindow,
            text = "Unavailable",
            image = weatherPicImage,
            compound = "top",
            bg = "#EBF7FD"
            ) #stores the necessary values for the weather graphic label
        weatherPicLabel.image = weatherPicImage #attaches the weather graphic to the weather graphic label
        weatherPicLabel.place(x = 120, y = 290) #places the weather graphic in the main.mainwindow

    #display NWS/NOAA logo
    xmllogoPicName = "xml_logo.gif"
    xmllogoPicLocation = "WeatherIconsGIF/" + xmllogoPicName

    #build the NWS/NOAA XML picture and append it
    xmllogoPic = Image.open(xmllogoPicLocation)
    xmllogoPicImage = ImageTk.PhotoImage(xmllogoPic)
    xmllogoLabel = tk.Label(
        main.mainwindow,
        text = " NWS XML ",
        image = xmllogoPicImage,
        compound = "top",
        bg = "#FEFEFE"
        )
    xmllogoLabel.image = xmllogoPicImage
    xmllogoLabel.place(x = 670, y = 132)

    

#make the strings, make the labels, make and display the background, and display the labels
def displayValues():
    #Current Conditions
    obsCurrentConditions = "Current Conditions" #stores the Current Conditions label in a string
    #Location
    obsLocation = str(gatherData.obs_location[0]) #stores the location in a string
    #Latitude and Longitude
    try:
        obsStationIdLatLon = "(" + str(gatherData.obs_stationid[0]) + ")   " + str(gatherData.obs_latitude[0]) + " " + str(gatherData.obs_longitude[0])
    except: #if coordinates are missing, do:
        obsStationIdLatLon = "(" + str(gatherData.obs_stationid[0]) + ")   " + "Latitude and Longitude Unavailable"
    #Observation Time
    try:
        obsObservationTime = str(gatherData.obs_observationtime[0]) + "   (" + str(gatherData.obs_observationtime_rfc822[0]) + ")"
    except: #if observation time is missing, do:
        obsObservationTime = "Time of Observation is Unavailable"
    #Observered Weather
    try:
        obsWeather = "Weather: " + str(gatherData.obs_weather[0])
    except: #if observed weather is missing, do:
        obsWeather = "Weather: Observation Unavailable"
    #Temperature
    try:
        obsTemperature = "Temperature: " + str(gatherData.obs_temperature[0])
    except: #if temperature is missing, do:
        obsTemperature = "Temperature: Unavailable"
    #Dewpoint
    try:
        obsDewpoint = "Dewpoint: " + str(gatherData.obs_dewpoint[0])
    except: #if dewpoint is missing, do:
        obsDewpoint = "Dewpoint: Unavailable"
    #Relative Humidity
    try:
        obsRelativeHumidity = "Relative Humidity: " + str(gatherData.obs_relativehumidity[0]) + "%"
    except: #if relative humidity is missing, do:
        obsRelativeHumidity = "Relative Humidity: Unavailable"
    #Wind
    try:
        obsWindString = "Wind: " + str(gatherData.obs_windstring[0])
    except: #if wind is missing, do:
        obsWindString = "Wind: Direction and Speed Unavailable"
    #Visibility
    try:
        obsVisibility = "Visibility: " + str(gatherData.obs_visibility[0])
    except: #if visibility is missing, do:
        obsVisibility = "Visibility: Unavailable"
    #Barometric Pressure
    try:
        obsPressure = "Barometric Pressure: " + str(gatherData.obs_pressure[0])
    except: #if pressure is missing, do:
        obsPressure = "Barometric Pressure: Unavailable"

    #clear and forget the labels if necessary; this is necessary if another XML file is opened
    global filesOpened
    if filesOpened > 0:
        obsLocationLabel = tk.Label(text = "", bg = "#AFDEF7", font = ("Arial, 17")) #location label
        obsLocationLabel.place_forget()
        obsStationIdLatLonLabel = tk.Label(text = "", bg = "#AFDEF7", font = ("Arial, 13")) #station ID and coordinates labe;
        obsStationIdLatLonLabel.place_forget()
        obsObservationTimeLabel = tk.Label(text = "", bg = "#AFDEF7", font = ("Arial, 11")) #observation time label
        obsObservationTimeLabel.place_forget()
        obsWeatherLabel = tk.Label(text = "", bg = "#AFDEF7", font = ("Arial, 13")) #weather condition label
        obsWeatherLabel.place_forget()
        obsTemperatureLabel = tk.Label(text = "", bg = "#AFDEF7", font = ("Arial, 13")) #temperature label
        obsTemperatureLabel.place_forget()
        obsDewpointLabel = tk.Label(text = "", bg = "#AFDEF7", font = ("Arial, 13")) #dewpoint label
        obsDewpointLabel.place_forget()
        obsRelativeHumidityLabel = tk.Label(text = "", bg = "#AFDEF7", font = ("Arial, 13")) #relative humidity label
        obsRelativeHumidityLabel.place_forget()
        obsWindStringLabel = tk.Label(text = "", bg = "#AFDEF7", font = ("Arial, 13")) #wind information label
        obsWindStringLabel.place_forget()
        obsVisibilityLabel = tk.Label(text = "", bg = "#AFDEF7", font = ("Arial, 13")) #visibility label
        obsVisibilityLabel.place_forget()
        obsPressureLabel = tk.Label(text = "", bg = "#AFDEF7", font = ("Arial, 13")) #pressure label
        obsPressureLabel.place_forget()

    #add a number to the filesOpened counter
    filesOpened = filesOpened + 1

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

    #display the labels with data
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
    #parse
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



#open file window so user can select their XML file                                                                                                                                                                                                                                                                                                                                                                          
def openFileWindow():
    openFileWindow.filename = tk.filedialog.askopenfilename(
        title = "Open XML File...",
        #change variable "initialdir" to your liking! 
        initialdir = "/home",
        filetypes = [("XML files", "*.xml")]
        ) #open file window
    gatherData()



# setup the main window
def main():
    main.mainwindow = tk.Tk() #main window
    main.mainwindow.title("NWS XML Display Tool")
    main.mainwindow.geometry('800x600') #maybe 1024x700 in the future?
    main.mainwindow["background"] = "#AFDEF7"
    
    #setup the main buttons
    openForecastXMLFile = tk.Button(
        master = main.mainwindow,
        text = "Open Forecast XML File",
        width = 18,
        height = 2,
        bg = "#0058A6",
        fg = "white",
        command=openFileWindow
        ) #button - opens the Useful Links window
    openCurrentConditionsXMLFile = tk.Button(
        master = main.mainwindow,
        text = "Open Current Conditions XML File",
        width = 28,
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
    openForecastXMLFile.place(x = 90, y = 540)
    openCurrentConditionsXMLFile.place(x = 300, y = 540)
    exitProgramBtn.place(x = 590, y = 540)
    
    #setup the main window contents
    programNameLabel = tk.Label(
        text = "National Weather Service XML Display Tool",
        font = ("Arial", 27),
        bg = "#AFDEF7"
        ) #label for the program name
    programNameLabel.pack()
    programVersionLabel = tk.Label(
        text = "version 0.11.1 - under construction, please mind the dust!",
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


