'''Imagine you have a weather station that measures temperature, humidity, and pressure. You want to notify various 
display devices whenever the weather conditions change. In this scenario, you can apply the Observer design pattern 
to establish a relationship between the weather station and the display devices.'''

class WeatherStation:
    def __init__(self):
        self.temperature = None
        self.humidity = None
        self.pressure = None
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def update_conditions(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.notify_observers()

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)


class DisplayDevice:
    def update(self, temperature, humidity, pressure):
        raise NotImplementedError()


class PhoneDisplay(DisplayDevice):
    def update(self, temperature, humidity, pressure):
        print(f"Phone Display: Temperature - {temperature}, Humidity - {humidity}, Pressure - {pressure}")


class TVDisplay(DisplayDevice):
    def update(self, temperature, humidity, pressure):
        print(f"TV Display: Temperature - {temperature}, Humidity - {humidity}, Pressure - {pressure}")


weather_station = WeatherStation()

phone_display = PhoneDisplay()
tv_display = TVDisplay()

weather_station.add_observer(phone_display)
weather_station.add_observer(tv_display)

weather_station.update_conditions(25, 70, 1013)


'''
In the code above, we have a WeatherStation class representing the subject. It maintains the current weather conditions 
and a list of observers. It provides methods to add and remove observers, as well as update the weather conditions and 
notify all observers.

The DisplayDevice class is an abstract observer class with a update method that will be implemented by concrete 
observer classes.

The PhoneDisplay and TVDisplay classes are concrete observer classes that inherit from the DisplayDevice class. They 
implement the update method, which prints the updated weather conditions specific to each display device.
'''