class Anime:
    GENRES = ('comedy', 'Horror', 'Sci-fi', 'Action', 'Romance', 'Mystery')

    def __init__(self, judul_anime, studio):
        self.judul_anime = judul_anime
        self.studio = studio

    def judul_lengkap(self):  
        return "%s by %s" % (self.judul_anime, self.studio)

    @property
    def judul_lengkap2(self):
        return "%s by %s" % (self.judul_anime, self.studio)

    @classmethod
    def allowed_genres_starting_with(cls, letter):
        return [g for g in cls.GENRES if g.startswith(letter)]

    @staticmethod
    def allowed_genres_ending_with(letter):
        return [g for g in Book.GENRES if g.endswith(letter)]


anime = Anime("Assasination Classroom", "Lerche")

print(anime.judul_lengkap())        
print(anime.judul_lengkap2)        

print(anime.allowed_genres_starting_with("F"))     
print(Anime.allowed_genres_starting_with("S"))    

print(anime.allowed_genres_ending_with("e"))     
print(Anime.allowed_genres_ending_with("n"))  
