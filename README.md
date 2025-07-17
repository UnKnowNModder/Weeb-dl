# Weeb Central API Scraper 📚

A powerful, asynchronous-ready Python wrapper for scraping manga data from `weebcentral.com`. This library provides a clean, object-oriented interface to search for manga, retrieve metadata, and download chapters as either individual images or compiled PDFs.

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

## Key Features

* **Advanced Search**: Filter manga by title, genre, status, type, and more.
* **Detailed Metadata**: Fetch all details for a manga series, including description, author, artist, aliases, and related series.
* **Chapter & Page Retrieval**: Easily get lists of all chapters for a manga and all pages for a chapter.
* **Powerful Downloader**:
    * Download a range of chapters for a specific manga.
    * Download chapters as neatly compiled PDF files.
    * Download chapters as raw image files organized in folders.
* **Efficient & Resilient**: Built-in caching, request retries, and threading for fast and reliable performance.
* **Type-Hinted & Easy to Use**: A clean, modern, and fully type-hinted codebase for a great developer experience.

***

## ⚙️ Installation

To install the library and its dependencies, run the following command:

```bash
pip install requests beautifulsoup4 Pillow fpdf2 ua-generator
```

You will also need the `enums.py` file in the same directory as your script to import the necessary filter criteria.

***

## 🚀 Quick Start

Here's a simple example to search for a manga and download the first five chapters as PDFs.

```python
from weeb_central import Weeb, Manga, Chapter, NetworkError, ParsingError

# 1. Initialize the main client
weeb = Weeb()

try:
    # 2. Search for a manga
    print("Searching for 'Solo Leveling'...")
    search_results = weeb.search(query="Solo Leveling")

    if not search_results:
        print("No manga found.")
    else:
        # 3. Select the first result
        my_manga = search_results[0]
        print(f"Found: {my_manga.title}")

        # 4. Fetch the list of all chapters
        print("Fetching chapter list...")
        all_chapters = my_manga.get_chapters()
        print(f"Total chapters found: {len(all_chapters)}")

        # 5. Filter for chapters 1 through 5
        chapters_to_download = my_manga.filter_chapters(all_chapters, start=1, end=5)
        print(f"Preparing to download {len(chapters_to_download)} chapters...")

        # 6. Download the filtered chapters
        # This will create a folder named 'Solo-Leveling' and save PDFs inside.
        my_manga.download(chapters_to_download)

        print("Download complete!")

except (NetworkError, ParsingError) as e:
    print(f"An error occurred: {e}")

```

***

## API Reference & Usage

The library is structured around several core classes: `Weeb`, `Manga`, and `Chapter`.

### The `Weeb` Class

This is the main entry point for the library. It handles high-level actions like searching and discovering manga.

#### `Weeb()`
Initializes the client.

```python
from weeb_central import Weeb
weeb = Weeb()
```

#### `weeb.search(...)`
Performs a comprehensive search for manga with advanced filtering.

**Parameters:**
* `query: str`: The title or keyword to search for.
* `sort: Sort`: How to sort the results. (e.g., `Sort.BEST_MATCH`).
* `order: Order`: `Order.ASCENDING` or `Order.DESCENDING`.
* `official: OfficialTranslation`: Filter by translation status.
* `anime: AnimeAdaptation`: Filter by anime adaptation status.
* `adult: AdultContent`: Filter by adult content.
* `status: List[SeriesStatus]`: A list of statuses to include (e.g., `[SeriesStatus.ONGOING]`).
* `type: List[SeriesType]`: A list of types to include (e.g., `[SeriesType.MANHWA]`).
* `genre: List[Genre]`: A list of genres to include (e.g., `[Genre.ACTION, Genre.FANTASY]`).

**Returns:** `List[Manga]`

**Example:**
```python
from enums import Genre, SeriesStatus, Sort

# Search for ongoing action/fantasy manga, sorted by popularity
results = weeb.search(
    sort=Sort.POPULARITY,
    status=[SeriesStatus.ONGOING],
    genre=[Genre.ACTION, Genre.FANTASY]
)

for manga in results:
    print(manga.title)
```

#### `weeb.recently_added(page=1)`
Retrieves a list of the most recently added manga series.

**Returns:** `List[Manga]`

**Example:**
```python
# Get the second page of recently added manga
new_manga_list = weeb.recently_added(page=2)
for manga in new_manga_list:
    print(manga.title)
```

#### `weeb.latest_updates(page=1)`
Retrieves the most recent chapter updates across all manga.

**Returns:** `Dict[Manga, Chapter]`

**Example:**
```python
latest = weeb.latest_updates()
for manga, chapter in latest.items():
    print(f"'{manga.title}' was updated to Chapter {chapter.index}")
```

#### `weeb.hot_series(sort=HotSeries.WEEKLY)`
Retrieves a list of trending ("hot") series for a given period.

**Parameters:**
* `sort: HotSeries`: The time frame (`HotSeries.WEEKLY`, `HotSeries.MONTHLY`, `HotSeries.ALL_TIME`).

**Returns:** `List[Manga]`

**Example:**
```python
from enums import HotSeries

# Get the hottest series of the month
hot_list = weeb.hot_series(sort=HotSeries.MONTHLY)
for manga in hot_list:
    print(manga.title)
```

#### `weeb.hot_updates()`
Gets the current "hot" chapter updates that are being read the most.

**Returns:** `Dict[Manga, Chapter]`

**Example:**
```python
hot_updates = weeb.hot_updates()
for manga, chapter in hot_updates.items():
    print(f"Trending Update: '{manga.title}' - Chapter {chapter.index}")
```

***

### The `Manga` Class

This class represents a single manga series and is used to fetch its specific data and chapters.

You typically get a `Manga` object from a `weeb.search()` call or other `Weeb` methods.

#### `manga.get_details()`
Fetches and populates the manga's metadata attributes (`.details`, `.description`, `.aliases`, `.related_series`).

**Example:**
```python
a_manga = weeb.search(query="one piece")[0]

# Details are initially empty
print(a_manga.description) #-> ""

# Fetch details
a_manga.get_details()

# Now they are populated
print(f"Title: {a_manga.title}")
print(f"Author: {a_manga.details.get('Author')}")
print(f"Description: {a_manga.description[:100]}...") # Print first 100 chars
print(f"Aliases: {a_manga.aliases}")
```

#### `manga.get_chapters()`
Fetches a complete list of all `Chapter` objects for the manga, sorted chronologically.

**Returns:** `List[Chapter]`

**Example:**
```python
all_chapters = a_manga.get_chapters()
print(f"Total chapters: {len(all_chapters)}")
print(f"Last chapter is: {all_chapters[-1].index}")
```

#### `manga.filter_chapters(...)`
A utility to filter a list of chapters by number or season.

**Parameters:**
* `chapters: List[Chapter]`: The list of chapters to filter (usually from `get_chapters()`).
* `start: float`: The starting chapter number.
* `end: float`: The ending chapter number.
* `season: int`: The specific season to filter by.

**Returns:** `List[Chapter]`

**Example:**
```python
# Get all chapters
all_chapters = a_manga.get_chapters()

# Filter for chapters 100 to 110
chapters_100_to_110 = a_manga.filter_chapters(all_chapters, start=100, end=110)

# Filter for all chapters in Season 2
season_2_chapters = a_manga.filter_chapters(all_chapters, season=2)
```

#### `manga.download(chapters)`
Downloads a list of `Chapter` objects. It creates a directory named after the manga and saves each chapter inside.

**Parameters:**
* `chapters: List[Chapter]`: The list of chapters to download.

**Example:**
```python
chapters_to_download = a_manga.filter_chapters(all_chapters, start=1, end=3)
# This will create a folder like 'One-Piece' and save:
# 1.pdf, 2.pdf, 3.pdf
a_manga.download(chapters_to_download)
```

***

### The `Chapter` Class

This class represents a single manga chapter.

#### `chapter.get_pages()`
Fetches a list of all `Page` objects for the chapter.

**Returns:** `List[Page]`

**Example:**
```python
first_chapter = a_manga.get_chapters()[0]
pages = first_chapter.get_pages()

for page in pages:
    print(f"Page {page.index}: {page.url}")
```

#### `chapter.download(path, download_type=DownloadType.PDF)`
Downloads the single chapter to a specified path.

**Parameters:**
* `path: str`: The directory where the file should be saved.
* `download_type: DownloadType`: The format (`DownloadType.PDF` or `DownloadType.IMAGE`).

**Example:**
```python
import os
from enums import DownloadType

# Get the first chapter
first_chapter = a_manga.get_chapters()[0]

# Create a directory for our single chapter download
output_dir = "single_chapter_download"
os.makedirs(output_dir, exist_ok=True)

# Download as a PDF
first_chapter.download(path=output_dir, download_type=DownloadType.PDF)

# Download as images
# This will create a sub-folder inside `output_dir` named after the chapter index
first_chapter.download(path=output_dir, download_type=DownloadType.IMAGE)
```

***

## 📋 Using Enums

For all filtering and sorting operations, this library uses `Enum` classes for clarity and to prevent errors. You must import them from the `enums.py` file.

**Available Enums:**
* `Sort`: For sorting search results (`BEST_MATCH`, `LATEST_UPDATE`, `POPULARITY`, etc.).
* `Order`: For sort direction (`ASCENDING`, `DESCENDING`).
* `OfficialTranslation`: (`ANY`, `YES`, `NO`).
* `AnimeAdaptation`: (`ANY`, `YES`, `NO`).
* `AdultContent`: (`ANY`, `YES`, `NO`).
* `SeriesStatus`: (`ONGOING`, `COMPLETED`, `HIATUS`, `CANCELLED`).
* `SeriesType`: (`MANGA`, `MANHWA`, `MANHUA`, `ONE_SHOT`, etc.).
* `Genre`: A long list of all available genres (`ACTION`, `ADVENTURE`, `FANTASY`, etc.).
* `HotSeries`: (`DAILY`, `WEEKLY`, `MONTHLY`, `ALL_TIME`).
* `DownloadType`: (`PDF`, `IMAGE`).

**Import Example:**
```python
from enums import Sort, Order, Genre, SeriesStatus, DownloadType
```

***

## ⚠️ Error Handling

The library raises custom exceptions for common issues. It's best practice to wrap your calls in a `try...except` block to handle them gracefully.

* `NetworkError`: Raised if there's a problem with the network connection, a timeout, or a server error (like HTTP 4xx or 5xx).
* `ParsingError`: Raised if the HTML structure of the site changes and the scraper cannot find the expected data.

**Example:**
```python
from weeb_central import NetworkError, ParsingError

try:
    # Attempt to fetch something
    hot_manga = weeb.hot_series()
    for manga in hot_manga:
        manga.get_details()
        print(f"Fetched details for {manga.title}")
except (NetworkError, ParsingError) as e:
    print(f"Could not complete the operation: {e}")
```
