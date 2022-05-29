# weather forecast
# pip install pyowm
# docs - https://github.com/csparpa/pyowm

#-----weather-forecast-----#
from pyowm import OWM
import math

#---------settings---------#
owm = OWM('25c2b543381b027be11917003d8f93df')
mgr = owm.weather_manager()
observation = mgr.weather_at_place('Minsk,BY')
w = observation.weather
temp = w.temperature('celsius')

#-----------main-----------#
ti = temp['temp']
a = math.ceil(ti)
b = math.floor(ti)

#----------result----------#
print (str(a)+'/'+str(b)+'°С')
