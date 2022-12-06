"""
TogaMasterJohn/StormSpotterJohn - John Spangle, 2022

NWS XML Display Tool, version 0.8.0

This tool displays some NWS Current Observation XML files. Not all stations' files are supported at this time.

"""

# "tkinter" is used for the GUI, "xml.etree.ElementTree" is used for parsing XML data... so nice!
import tkinter.filedialog
from tkinter import Canvas
import tkinter as tk
import xml.etree.ElementTree as et #included with Python



#make the strings, make the labels, make and display the background, and display the labels
def displayValues():
    #make the strings
    obsCurrentConditions = "Current Conditions"
    obsLocation = str(gatherData.obs_location[0])
    obsStationIdLatLon = "(" + str(gatherData.obs_stationid[0]) + ")   " + str(gatherData.obs_latitude[0]) + " " + str(gatherData.obs_longitude[0])
    obsObservationTime = str(gatherData.obs_observationtime[0]) + "   (" + str(gatherData.obs_observationtime_rfc822[0]) + ")"
    obsWeather = "Weather: " + str(gatherData.obs_weather[0])
    obsTemperature = "Temperature: " + str(gatherData.obs_temperature[0])
    obsDewpoint = "Dewpoint: " + str(gatherData.obs_dewpoint[0])
    obsRelativeHumidity = "Relative Humidity: " + str(gatherData.obs_relativehumidity[0])
    obsWindString = "Wind: " + str(gatherData.obs_windstring[0])
    obsVisibility = "Visibility: " + str(gatherData.obs_visibility[0])
    obsPressure = "Altimeter: " + str(gatherData.obs_pressure[0])
    #make the labels
    obsCurrentConditionsLabel = tk.Label(text = obsCurrentConditions, bg = "#AFDEF7", font = ("Arial, 20"))
    obsLocationLabel = tk.Label(text = obsLocation, bg = "#AFDEF7")
    obsStationIdLatLonLabel = tk.Label(text = obsStationIdLatLon, bg = "#AFDEF7")
    obsObservationTimeLabel = tk.Label(text = obsObservationTime, bg = "#AFDEF7")
    obsWeatherLabel = tk.Label(text = obsWeather, bg = "#AFDEF7")
    obsTemperatureLabel = tk.Label(text = obsTemperature, bg = "#AFDEF7")
    obsDewpointLabel = tk.Label(text = obsDewpoint, bg = "#AFDEF7")
    obsRelativeHumidityLabel = tk.Label(text = obsRelativeHumidity, bg = "#AFDEF7")
    obsWindStringLabel = tk.Label(text = obsWindString, bg = "#AFDEF7")
    obsVisibilityLabel = tk.Label(text = obsVisibility, bg = "#AFDEF7")
    obsPressureLabel = tk.Label(text = obsPressure, bg = "#AFDEF7")
    #display the labels
    obsCurrentConditionsLabel.place(x = 90, y = 120)
    obsLocationLabel.place(x = 90, y = 160)
    obsStationIdLatLonLabel.place(x = 90, y = 180)
    obsObservationTimeLabel.place(x = 90, y = 200)
    obsWeatherLabel.place(x = 90, y = 240)
    obsTemperatureLabel.place(x = 90, y = 260)
    obsDewpointLabel.place(x = 90, y = 280)
    obsRelativeHumidityLabel.place(x = 90, y = 300)
    obsWindStringLabel.place(x = 90, y = 320)
    obsVisibilityLabel.place(x = 90, y = 340)
    



#parse, make the necessary lists, and gather the data
def gatherData():
    #parse!
    tree = et.parse(openFileWindow.filename)
    root = tree.getroot()
    #define the namespaces from the XML file, as not doing so makes it difficult to parse the data
    et.register_namespace("xsd", "http://www.w3.org/2001/XMLSchema")
    et.register_namespace("xsi", "http://www.w3.org/2001/XMLSchema-instance")
    et.register_namespace("xsi", "http://www.weather.gov/view/current_observation.xsd")
    #lists for the values
    gatherData.obs_location = []
    gatherData.obs_stationid = []
    gatherData.obs_latitude = []
    gatherData.obs_longitude = []
    gatherData.obs_observationtime = []
    gatherData.obs_observationtime_rfc822 = []
    gatherData.obs_weather = []
    gatherData.obs_temperature = []
    gatherData.obs_relativehumidity = []
    gatherData.obs_windstring = []
    gatherData.obs_pressure = []
    gatherData.obs_dewpoint = []
    gatherData.obs_visibility = []
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
    #go to displayValues
    displayValues()



#open a window containing useful links
def openUsefulLinksWindow():
    usefulLinksWindow = tk.Toplevel()
    usefulLinksWindow.title("Useful Links")
    usefulLinksWindow.geometry("420x240")
    usefulLinksWindow["background"] = "#AFDEF7"
    usefulLinksNWS1Label = tk.Label(
        master=usefulLinksWindow,
        text = "Get your local forecast from the National Weather Service!",
        font = ("Arial", 10),
        bg = "#AFDEF7"
        )
    usefulLinksNWS1Label.pack()
    usefulLinksNWS1LinkLabel = tk.Label(
        master=usefulLinksWindow,
        text = "https://www.weather.gov",
        font = ("Arial", 10),
        bg = "#AFDEF7"
        )
    usefulLinksNWS1LinkLabel.pack()



#open file window so user can select their XML file                                                                                                                                                                                                                                                                                                                                                                          
def openFileWindow():
    openFileWindow.filename = tk.filedialog.askopenfilename(
        title = "Open XML File",
        initialdir = "/",
        filetypes = [("XML files", "*.xml")]
        )
    gatherData()



# setup the main window
def main():
    mainwindow = tk.Tk()
    mainwindow.title("NWS XML Display Tool")
    mainwindow.geometry('800x600')
    mainwindow["background"] = "#AFDEF7"
    #setup the main buttons
    openInfoWindow = tk.Button(
        master = mainwindow,
        text = "Useful Links",
        width = 12,
        height = 2,
        bg = "#0058A6",
        fg = "white",
        command=openUsefulLinksWindow
        )
    openXMLFile = tk.Button(
        master = mainwindow,
        text = "Open XML File",
        width = 12,
        height = 2,
        bg = "#0058A6",
        fg = "white",
        command=openFileWindow
        )
    #setup the main window buttons
    openInfoWindow.place(x = 90, y = 550)
    openXMLFile.place(x = 360, y = 550)
    #setup the main window contents
    programNameLabel = tk.Label(
        text = "National Weather Service XML Display Tool",
        font = ("Arial", 25),
        bg = "#AFDEF7"
        )
    programNameLabel.pack()
    programVersionLabel = tk.Label(
        text = "version 0.8.0 - under construction, please mind the dust!",
        font = ("Arial", 16),
        bg = "#AFDEF7"
        )
    programVersionLabel.pack()
    programDisclaimerLabel = tk.Label(
        text = "This program is not affiliated with the National Oceanic and Atmospheric Administration or the National Weather Service.",
        font = ("Arial", 8),
        bg = "#AFDEF7"
        )
    programDisclaimerLabel.pack()
    # run main loop
    mainwindow.mainloop()

    

#start program
if __name__ == "__main__":
    main()


