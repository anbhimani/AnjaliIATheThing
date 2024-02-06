#creating Music class
class Music:
    #constructor to instantiate music object
    #declaring instance variables
    def __init__(self, name, artist, zeroCrossingRate, tempo, spectralCentroid, contrast, flatness):
        self.zeroCrossingRate = zeroCrossingRate
        self.tempo = tempo
        self.spectralCentroid = spectralCentroid
        self.name = name
        self.artist = artist
        self.contrast = contrast
        self.flatness = flatness



