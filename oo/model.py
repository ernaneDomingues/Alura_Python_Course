class Generic:
    def __int__(self, name, year):
        self._name = name.title()
        self.year = year
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def put_like(self):
        self._likes += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    def __str__(self):
        return f'Name: {self._name} - Year: {self.year} - Likes: {self._likes}'


class Movie(Generic):
    def __int__(self, name, year, lifetime):
        super().__int__(name, year)
        self.lifetime = lifetime

    def __str__(self):
        return f'Name: {self._name} - Year: {self.year} - {self.lifetime} min - Likes: {self._likes}'

class Series(Generic):
    def __int__(self, name, year, season):
        super().__int__(name, year)
        self.season = season

    def __str__(self):
        return f'Name: {self._name} - Year: {self.year} - {self.season} season - Likes: {self._likes}'


class Playlist(list):
    def __int__(self, name, movie_and_series):
        self.name = name
        self._movie_and_series = movie_and_series

    def __getitem__(self, item):
        return self._movie_and_series[item]

    def __len__(self):
        return len(self._movie_and_series)

    @property
    def movie_and_series(self):
        return self._movie_and_series

if __name__ == '__main__':
    sonic = Movie('sonic the hedgehog', 2020, 101)
    one_piece = Movie('one piece film z', 2012, 108)
    stranger_things = Series('stranger things', 2016, 4)
    the_crown = Series('the crown', 2016, 4)

    movie_and_series = [one_piece, sonic, stranger_things, the_crown]
    my_playlist = Playlist('My playlist', movie_and_series)
    for item in my_playlist:
        print(item)