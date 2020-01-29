# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE 
class LatLon():
  def __init__(self, lat, lon):
    self.lat = lat
    self.lon = lon

  def __str__(self):
    return '''
    lat:{self.lat}, 
    lon:{self.lon}'''.format(self=self)

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE 
class WayPoint(LatLon):
  def __init__(self, name, lat, lon):
    super().__init__(lat, lon)
    self.name = name

  def __str__(self):
    return '''
    name: {self.name}, 
    lat: {self.lat}, 
    lon:{self.lon}'''.format(self=self)

    
# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE 
class Geocache(WayPoint):
  def __init__(self, name, diff, size, lat, lon):
    super().__init__(name, lat, lon)
    self.diff = diff
    self.size = size

  def __str__(self):
    return '''
    name: {self.name}, 
    diff: {self.diff}, 
    size: {self.size}, 
    lat: {self.lat}, 
    lon: {self.lon}
    '''.format(self=self)
# Make a new waypoint and print it out: "Catacombs", 41.70505, 41.70505

# YOUR CODE HERE   
waypoint = WayPoint('Catacombs', 41.70505, -121.51521)


# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556 
geocache = Geocache("Newberry Views" , float(1.5) , 2 , 44.052137, -121.41556 )

# YOUR CODE HERE

# Print it--also make this print more nicely
print(geocache)
