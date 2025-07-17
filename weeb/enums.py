from enum import Enum

class Sort(Enum):
    BEST_MATCH = "Best Match"
    ALPHABET = "Alphabet"
    POPULARITY = "Popularity"
    SUBSCRIBERS = "Subscribers"
    RECENTLY_ADDED = "Recently Added"
    LATEST_UPDATES = "Latest Updates"

    def __str__(self):
        return self.value

class Order(Enum):
    ASCENDING = "Ascending"
    DESCENDING = "Descending"

    def __str__(self):
        return self.value

class OfficialTranslation(Enum):
    ANY = "Any"
    TRUE = "True"
    FALSE = "False"

    def __str__(self):
        return self.value

class AnimeAdaptation(Enum):
    ANY = "Any"
    TRUE = "True"
    FALSE = "False"

    def __str__(self):
        return self.value

class AdultContent(Enum):
    ANY = "Any"
    TRUE = "True"
    FALSE = "False"

    def __str__(self):
        return self.value

class SeriesStatus(Enum):
    ONGOING = "Ongoing"
    COMPLETE = "Complete"
    HIATUS = "Hiatus"
    CANCELED = "Canceled"

    def __str__(self):
        return self.value

class SeriesType(Enum):
    MANGA = "Manga"
    MANHWA = "Manhwa"
    MANHUA = "Manhua"
    OEL = "OEL"

    def __str__(self):
        return self.value

class Genre(Enum):
    ACTION = "Action"
    ADULT = "Adult"
    ADVENTURE = "Adventure"
    COMEDY = "Comedy"
    DOUJINSHI = "Doujinshi"
    DRAMA = "Drama"
    ECCHI = "Ecchi"
    FANTASY = "Fantasy"
    GENDER_BENDER = "Gender Bender"
    HAREM = "Harem"
    HENTAI = "Hentai"
    HISTORICAL = "Historical"
    HORROR = "Horror"
    ISEKAI = "Isekai"
    JOSEI = "Josei"
    LOLICON = "Lolicon"
    MARTIAL_ARTS = "Martial Arts"
    MATURE = "Mature"
    MECHA = "Mecha"
    MYSTERY = "Mystery"
    PSYCHOLOGICAL = "Psychological"
    ROMANCE = "Romance"
    SCHOOL_LIFE = "School Life"
    SCI_FI = "Sci-fi"
    SEINEN = "Seinen"
    SHOTACON = "Shotacon"
    SHOUJO = "Shoujo"
    SHOUJO_AI = "Shoujo Ai"
    SHOUNEN = "Shounen"
    SHOUNEN_AI = "Shounen Ai"
    SLICE_OF_LIFE = "Slice of Life"
    SMUT = "Smut"
    SPORTS = "Sports"
    SUPERNATURAL = "Supernatural"
    TRAGEDY = "Tragedy"
    YAOI = "Yaoi"
    YURI = "Yuri"
    OTHER = "Other"

    def __str__(self):
        return self.value

class HotSeries:
	WEEKLY = "weekly_views"
	MONTHLY = "monthly_views"
	ALL_TIME = "total_views"
	
	def __str__(self):
		return self.value

class DownloadType:
	PDF = "pdf"
	IMAGE = "image"