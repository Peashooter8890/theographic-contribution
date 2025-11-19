# Theographic Bible Metadata - JSON Fields Documentation
This documentation provides a comprehensive reference for the structure and fields of JSON files within the Theographic Bible Metadata dataset.

### Dataset Overview
The JSON files are located in the `json/` directory of the root repository. These files were generated through a Python ETL script from Airtable, where the original data was inputted and continues to be updated. Because of this Airtable origin, you may encounter peculiarities in data structure and field name inconsistencies. Throughout this documentation, JSON files are referred to as "tables" since they directly represent tabular data exported from Airtable.

### Standard JSON Entity Structure
All Theographic JSON entities have three root fields:
- `id` - A 14-character alphanumeric case-sensitive unique record identifier (e.g., `recRAcqtgn28zXm1a`)
- `createdTime` - An ISO 8601/RFC 3339 formatted timestamp (e.g., `2018-06-01T13:12:45.000Z`)
- `fields` - A nested object containing entity-specific data

This documentation focuses exclusively on the fields contained within the `fields` object. Each section below corresponds to a specific JSON file, detailing its field names, data types, and relationships with other JSON files.

## Books
This table contains high-level metadata for each of the 66 books in the Protestant Bible canon. It includes various naming conventions (e.g. `osisName`, `bookName`, `shortName`), canonical divisions (`testament`, `bookDiv`), and structural information like chapter and verse counts. It also serves as a sort of central hub, linking to the chapters, verses, writers, people, and places associated with each book.

### Fields Reference (16 Fields)

| Field | Type | Status | Description |
|-------|------|--------|-------------|
| `osisName` | string | Validated | Abbreviation matching the Open Scriptural Information Standard. |
| `bookName` | string | Validated | Full name of the book |
| `chapterCount` | integer | Validated | Total chapters |
| `bookDiv` | string | Validated | High-level divisions of the Bible |
| `shortName` | string | Validated | Shortest abbreviation, useful for small labels |
| `bookOrder` | integer | Validated | Order of books in the traditional Protestant canon, excluding Apocrypha. |
| `verses` | array | Validated | Links to records in the "verses" table. |
| `yearWritten` | array | Incomplete | Approximate year written, if known. |
| `placeWritten` | array | Incomplete | Place the book was written, if known. |
| `verseCount` | integer | Validated | Total verses |
| `chapters` | array | Validated | Links to records in the "chapters" table. |
| `writers` | array | Validated | Roll-up from Chapter-level writer assignment |
| `testament` | string | Validated | Old or New Testament identifier |
| `slug` | string | Validated | Lowercase, url-friendly version of Osis Name |
| `peopleCount` | integer | Validated | Number of people mentioned by name within the book |
| `placeCount` | integer | Validated | Number of places mentioned by name within the book |

### Relationships
- `verses` → References field `id` of `verses` table records
- `yearWritten` → References field `id` of `periods` table
- `placeWritten` → References field `id` `places` table
- `chapters` → References field `id` of `chapters` table records
- `writers` → References subfield `personLookup` of field `fields` of `people` table records

### Example
```json
{
  "id": "recyvIyxRMFob6SoM",
  "createdTime": "2018-05-13T17:19:17.000Z",
  "fields": {
    "osisName": "Rom",
    "bookName": "Romans",
    "chapterCount": 16,
    "bookDiv": "Pauline Epistles",
    "shortName": "Ro",
    "bookOrder": 45,
    "verses": [
      "recld8Sxx8yDn1Ik8"
    ],
    "yearWritten": [
      "recvOFi9OkrgM1IAO"
    ],
    "placeWritten": [
      "recpmPd6JhbqhqA0Q"
    ],
    "verseCount": 433,
    "chapters": [
      "recMCMGLnVg4olx48"
    ],
    "writers": [
      "paul_2479"
    ],
    "testament": "New Testament",
    "slug": "rom",
    "peopleCount": 238,
    "placeCount": 13
  }
}
```
## Chapters
This table defines every chapter in the Bible. Each record links to its parent `book` and lists all the `verses` it contains. It also identifies the traditional `writer` of the chapter and provides counts of the distinct people and places mentioned within it.

### Fields Reference (10 Fields)

| Field | Type | Status | Description |
|-------|------|--------|-------------|
| `osisRef` | string | Validated | Unique identifier using book.chapter |
| `book` | array | Validated | Links to records in the "book" table. |
| `chapterNum` | integer | Validated | |
| `writer` | array | Validated | Links to a person record, based on traditional understandings of authorship. |
| `verses` | array | Validated | Links to verse records of all verses within the chapter. |
| `slug` | string | Validated | Lowercase, url-friendly version of Osis Ref |
| `peopleCount` | integer | Validated | Number of people mentioned by name within the chapter |
| `placesCount` | integer | Validated | Number of places mentioned by name within the chapter |
| `modified` | string | Unknown | Last modified date and time |
| `writer count`| integer | Validated | Total number of writers for the chapter |

### Relationships
- `book` → References field `id` of `books` table records
- `writer` → References field `id` of `people` table records
- `verses` → References field `id` of `verses` table records

### Example
```json
{
  "osisRef": "1Chr.1",
  "book": [
    "rec2ZFQHqI4eUjhqX"
  ],
  "chapterNum": 1,
  "writer": [
    "recKCifIYcTXovrF4"
  ],
  "verses": [
    "recIJ14BlamQIvokW",
    "recMeUNvOQWjYQOFE",
    ...
  ],
  "slug": "1chr_1",
  "peopleCount": 54,
  "placesCount": 8,
  "modified": "2019-08-08T01:43:21.000Z",
  "writer count": 1
}
```
## Easton
This table contains parsed entries from the 1897 Easton's Bible Dictionary. Each record represents a single dictionary term, providing its label, definition text (`dictText`), and metadata extracted from the source XML at http://www.ccel.org/ccel/easton/ebd2.xml. Crucially, it links dictionary entries to corresponding records in the `people` and `places` tables, enriching the dataset with historical and theological context.

### Fields Reference (12 Fields)

| Field | Type | Status | Description |
|-------|------|--------|-------------|
| `dictLookup` | string | Validated | Unique string for a dictionary entry, split out by sub-paragraphs |
| `termID` | string | Unknown | The id attribute of the <term> tag in the source XML. This ID indicates the location of the term within the original document's structure. For example, "a-p1.11" signifies that the term is in the "a" section, and within that section, it is associated with the paragraph block indexed as "p1" and is the 11th tagged element within that block. |
| `termLabel` | string | Validated | Title of the original entry |
| `def_id` | string | Unknown | The id attribute of the <def> tag in the source XML. This ID directly corresponds to the termID and points to the definition block for that specific term. For example, if the termID is "a-p1.11", the corresponding def_id will be "a-p1.12". |
| `has_list` | string | Unknown | A boolean field ("True" or "False") that indicates whether the definition text contains a numbered or itemized list. This is derived from the structure of the source XML, though not explicitly shown in the provided snippet. |
| `itemNum` | integer | Validated | Sub-section number, if multiple sections are listed in one entry |
| `matchType` | string | Temporary | Used to validate scripts which automatically match entities. |
| `matchSlugs` | string | Temporary | Used to check automatically matched slugs of entities in other tables |
| `dictText` | string | Validated | Text of the dictionary entry |
| `index` | integer | Validated | Unique identifier |
| `personLookup` | array | Populated | Links to the "people" table |
| `placeLookup` | array | Populated | Links to the "places" table |

### Relationships
- `personLookup` → References field `id` of `people` table records
- `placeLookup` → References field `id` of `places` table records

### Example
```json
{
  "dictLookup": "Abdon 4",
  "termID": "a-p21.2",
  "termLabel": "Abdon",
  "def_id": "a-p21.3",
  "has_list": "True",
  "itemNum": 4,
  "matchType": "multi",
  "matchSlugs": "['abdon_3', 'abdon_11']",
  "dictText": "One of the “sons” of Shashak ([1 Chr. 8:23](/1chr#1Chr.8.23)).\n\n This is the name also of a Levitical town of the Gershonites, in the tribe of Asher ([Josh. 21:30](/josh#Josh.21.30); [1 Chr. 6:74](/1chr#1Chr.6.74)). The ruins of Abdeh, some 8 miles north-east of Accho, probably mark its site.",
  "personLookup": [
    "recJoOUIhbhMXSf5Y"
  ],
  "placeLookup": [
    "recPdJgyI1kRUNw35"
  ],
  "index": 21
}
```

## Events
This table chronicles the timeline of Biblical events. Each record details a specific event with a `title`, chronological data (e.g. `startDate`), and its relationship to other events (`predecessor`, `partOf`). It connects each event to its `participants` (people), `locations` (places), and the narrative `verses` that describe it.

### Fields Reference (19 Fields)

| Field | Type | Status | Description |
|-------|------|--------|-------------|
| `title` | string | Incomplete | Unique title for an event |
| `startDate` | string | Incomplete | ISO formatted date to identify calendar dates where known |
| `duration` | string | Incomplete | Event length in days, years, etc. for use in end date calculations |
| `participants` | array | Incomplete | Links people involved in the event |
| `verses` | array | Incomplete | Verses which serve as an original narrative for the event |
| `verseSort` | string | Unknown | The `verseID` of the first verse in the `verses` field of this event. |
| `modified` | string | Unknown | Last modified date and time |
| `sortKey` | float | Incomplete | Uses a combination of year and verseSort to sort all events chronolgically. The calculation formula, originated in airtable, is `INT(IF(LEFT(startDate,1)='-',LEFT(startDate,5),LEFT(startDate,4))) + INT(verseSort)/100000000`|
| `people (from verses)` | array | Unknown | People who are mentioned in the verses associated with the event. |
| `eventID` | integer | Unknown | Unique identifier |
| `locations` | array | Incomplete | Links to place records where the event took place |
| `partOf` | array | Unknown | Links an event to a larger event that it is a part of. |
| `places (from verses)` | array | Unknown | Locations that are mentioned in the verses associated with the event. |
| `predecessor` | array | Incomplete | Establishes predecessor-successor constraints if applicable |
| `rangeFlag` | boolean | Unknown | |
| `lag` | string | Unknown | The time elapsed between the predecessor event and the current event. |
| `lagType` | string | Unknown | The type of predecessor relationship - either Start-to-Start (SS) or Finish-to-Start (FS). For example, for an event with lag of 130Y, lagType `FS` means that the event started 130 years after the predecessor event finished, whereas lagType `SS` means that the event started 130 years after the predecessor event started.|
| `notes` | string | Unknown | A field for additional commentary or explanatory notes about the event. |
| `groups` | array | Unknown | Groups of people involved in the event. |

### Relationships
- `predecessor` → References field `id` of `events` table records
- `partOf` → References field `id` of `events` table records
- `participants` → References field `id` of `people` table records
- `locations` → References field `id` of `places` table records
- `verses` → References field `id` of `verses` table records
- `people (from verses)` → References field `id` of `people` table records
- `places (from verses)` → References field `id` of `places` table records

### Example
```json
{
  "title": "Birth of Abraham",
  "startDate": "-1996",
  "duration": "1D",
  "participants": [
    "reccdFYIq50NyxNej",
    "recXBYSWubfkpqNQm"
  ],
  "verses": [
    "rec4ayUcZnUN9fhUl",
    "recuJqyP43vbWJbzj"
  ],
  "verseSort": "01011026",
  "modified": "2020-11-25T15:12:15.000Z",
  "sortKey": -1995.98988974,
  "people (from verses)": [
    "recXBYSWubfkpqNQm",
    "reccdFYIq50NyxNej",
    ...
  ],
  "eventID": 65,
  "locations": [
    "recgQtoCtBjbsPwAw"
  ],
  "partOf": [
    "recfnatCOLEHFYeLB"
  ],
  "predecessor": [
    "recePREjv2zZ8Esoo"
  ],
  "lag": "130Y",
  "lagType": "FS",
  "notes": "Not all of Terah's sons would have been born the same year. In light of Acts 7:4 and Genesis 12:4, Abraham was born when Terah was 130 years old.\n"
}
```
## People (38 Fields)
This table provides a comprehensive catalog of every individual mentioned by name in the Bible. Records include identifying information (e.g. `name`, `gender`), biographical details (e.g. `birthYear`, `deathYear`), and extensive relational data, linking to family members (`father`, `mother`, `siblings`), associated `events`, and all `verses` where the person is mentioned.

### Fields Reference (38 Fields)

| Field | Type | Status | Description |
|-------|------|--------|-------------|
| `personLookup` | string | Validated | Unique identifier using name and ID number |
| `personID` | integer | Validated | Unique numerical identifier, helping to distinguish people with the same name. |
| `name` | string | Validated | Primary name used in the text of the KJV |
| `isProperName` | boolean | Validated | Identifies those with proper names vs. descriptive names like "Wife of..." or "Son of..." |
| `gender` | string | Validated | Male or Female |
| `birthYear` | array | Populated | Not yet aligned with passage/event timelines |
| `deathYear` | array | Populated | Not yet aligned with passage/event timelines |
| `memberOf` | array | Validated | Links to peopleGroups if membership can be deduced. |
| `birthPlace` | array | Validated | Links to place records where the birth location is known |
| `deathPlace` | array | Validated | Links to place records where the death location is known |
| `dictionaryLink` | string | Unknown | A URL to its Easton's Bible Dictionary entry at https://www.biblestudytools.com/dictionaries/eastons-bible-dictionary. |
| `dictionaryText` | string | Unknown | The text content from its Easton's Bible Dictionary entry. |
| `verseCount` | integer | Validated | Counts verses where the person is mentioned by name |
| `verses` | array | Validated | Verses where the person is mentioned by name |
| `siblings` | array | Validated | Links to the person's full siblings. |
| `mother` | array | Validated | Links to the person's mother. |
| `father` | array | Validated | Links to the person's father. |
| `children` | array | Validated | Links to the person's children. |
| `minYear` | integer | Temporary | Temporary to help align birth year to passage/events timeline |
| `maxYear` | integer | Temporary | Temporary to help align birth year to passage/events timeline |
| `displayTitle` | string | Populated | Disambiguated name suitable for page titles and search results |
| `status` | string | Temporary | The validation status of the individual person record |
| `alphaGroup` | string | Validated | Used for alphabetical indexing |
| `slug` | string | Validated | Lowercase, url-friendly version of personLookup |
| `partners` | array | Unknown | Links to the person's spouse or partner. |
| `eastons` | array | Incomplete | Links to relevant sub-sections in Easton's dictionary. Complete for the book of Acts |
| `Easton's Count` | integer | Unknown | 1 if it exists as an entry in Easton's Bible Dictionary; 0 otherwise.|
| `dictText` | array | Incomplete | Markdown-formatted text from relevant sub-section in Easton's dictionary. |
| `modified` | string | Unknown | Last modified date and time |
| `timeline` | array | Unknown | Links to events for the person. |
| `ambiguous` | boolean | Temporary | Identifies display titles which have not been edited for disambiguation. |
| `Disambiguation (temp)` | string | Temporary | Mechanical Turk entries used to aid in disambiguation |
| `events` | string | Incomplete | Title of events in which the person participated. Complete for the book of Acts |
| `alsoCalled` | string | Populated | Alternate spellings or other known names for the same person. |
| `halfSiblingsSameMother` | array | Validated | Links to the person's maternal half-siblings. |
| `halfSiblingsSameFather` | array | Validated | Links to the person's paternal half-siblings. |
| `chaptersWritten` | array | Validated | Specific chapters written by this person according to traditional understanding of authorship. |
| `surname` | string | Validated | Surname, if known. |

### Relationships
- `birthYear` → References field `id` of `events` table
- `deathYear` → References field `id` of `events` table
- `memberOf` → References field `id` of `peopleGroups` table records
- `birthPlace` → References field `id` of `places` table records
- `deathPlace` → References field `id` of `places` table records
- `verses` → References field `id` of `verses` table records
- `siblings` → References field `id` of `people` table records
- `mother` → References field `id` of `people` table records
- `father` → References field `id` of `people` table records
- `children` → References field `id` of `people` table records
- `partners` → References field `id` of `people` table records
- `eastons` → References field `id` of `easton` table records
- `timeline` → References field `id` of `events` table records
- `halfSiblingsSameMother` → References field `id` of `people` table records
- `halfSiblingsSameFather` → References field `id` of `people` table records
- `chaptersWritten` → References field `id` of `people` table records

### Example
```json
{
  "personLookup": "joseph_1710",
  "personID": 1710,
  "name": "Joseph",
  "isProperName": true,
  "gender": "Male",
  "birthYear": [
    "recwuinZnl42NLcM4"
  ],
  "deathYear": [
    "reczIlmyAUfTRS1XO"
  ],
  "memberOf": [
    "rec4hpOWgtnNNXWSJ"
  ],
  "birthPlace": [
    "recfrXyxhuYOczKTm"
  ],
  "deathPlace": [
    "recfrXyxhuYOczKTm"
  ],
  "dictionaryLink": "https://www.biblestudytools.com/dictionaries/eastons-bible-dictionary/joseph.html",
  "dictionaryText": " remover or increaser. The elder of the two sons of Jacob by Rachel (  Genesis 30:23   Genesis 30:24  ), *...(hidden for conciseness)*",
  "verseCount": 199,
  "verses": [
    "recry3sM59m5pfdr2",
    "reckxubjFXOC3zchS",
    ...
  ],
  "siblings": [
    "recBOUtTncbBlfEn9"
  ],
  "halfSiblingsSameFather": [
    "rectGDQCkKqZ6LgGB",
    "rec3HzZknu1HOvNci",
    ...
  ],
  "mother": [
    "recT2Tm2K5XORGnbx"
  ],
  "father": [
    "recsU2ZSdzBvDqzgI"
  ],
  "children": [
    "rec1YbscOE9IyJ5ey",
    "recEtv9ql7Hh4XAW4"
  ],
  "minYear": -1752,
  "maxYear": 96,
  "displayTitle": "Joseph (son of Jacob)",
  "status": "publish",
  "alphaGroup": "J",
  "slug": "joseph_1710",
  "partners": [
    "recNkoJz33pFlgcn2"
  ],
  "alsoCalled": "Zaphnath-paaneah",
  "Disambiguation (temp)": "Joseph(The sons of Rachel)",
  "eastons": [
    "rec1hmENiT7j0psby"
  ],
  "Easton's Count": 1,
  "dictText": [
    "The elder of the two sons of Jacob by Rachel ([Gen. 30:23](/gen#Gen.30.23), [24](/gen#Gen.30.24)), who, on the occasion of his birth, said, *...(hidden for conciseness)*"
  ],
  "modified": "2021-01-06T20:45:33.000Z",
  "timeline": [
    "recZDLkLCBpaZjV7D",
    "recj8qDYwzBEfwBAa",
    ...
  ]
}
```

## PeopleGroups (7 Fields)
This table defines collective groups of people, such as tribes, nations, or families. Each record has a `groupName` and contains an array of `members` who belong to that group. It also links to `verses` where the group is mentioned and `events` in which they participated.

### Fields Reference (7 Fields)

| Field | Type | Status | Description |
|-------|------|--------|-------------|
| `groupName` | string | Validated | Unique name |
| `members` | array | Validated | Links to a person record for members of this group |
| `modified` | string | Unknown | Last modified date and time |
| `events_dev` | array | Unknown | Links the group to IDs of relevant events. |
| `verses` | array | Incomplete | Verses mentioning this group |
| `partOf` | array | Unknown | Links a group to a larger group it is a part of (e.g., each of the twelve tribes of Israel is part of the "Nation of Israel" group). |
| `events` | string | Incomplete | Events in which this group participated. |

### Relationships
- `members` → References field `id` of `people` table records
- `partOf` → References field `id` of `peopleGroups` table records
- `verses` → References field `id` of `verses` table records
- `events_dev` → References field `id` of `events` table records

### Example
```json
{
  "groupName": "Tribe of Judah",
  "members": [
    "recYIZfi53zX3NJh0",
    "recEg9i0J2MgmkZr8",
    ...
  ],
  "verses": [
    "recDl7QYLCsVnnMwn"
  ],
  "modified": "2020-09-07T20:00:01.000Z",
  "events_dev": [
    "recjkmUO88wihv8Ci",
    "recr71Fz4NHTnGLJ2",
    "recSF4lyBebGjJEXI"
  ]
}
```

## Periods (9 Fields)
This table organizes the Biblical timeline into discrete years. Each record represents a single year and aggregates key information from that period, including `peopleBorn`, `peopleDied`, `events` that occurred, and Biblical `booksWritten`.

### Fields Reference (9 Fields)

| Field | Type | Status | Description |
|-------|------|--------|-------------|
| `yearNum` | string | Incomplete | Integer for the year where negative values indicate BC, positive indicates AD |
| `peopleBorn` | array | Incomplete | People born that year, if known. |
| `events` | string | Incomplete | Title of events which occurred in that year. Complete for the book of Acts. |
| `isoYear` | integer | Validated | ISO-8601 standard year number (accounts for the non-existence of year 0) |
| `BC-AD` | string | Incomplete | Groups AD and BC years |
| `formattedYear` | string | Validated | Formatted string for the year and AD/BC designation |
| `modified` | string | Unknown | Last modified date and time |
| `peopleDied` | array | Incomplete | People who died that year, if known. |
| `booksWritten` | array | Incomplete | Books of the bible written that year, if known. |

### Relationships
- `peopleBorn` → References field `id` of `people` table records
- `peopleDied` → References field `id` of `people` table records
- `booksWritten` → References field `id` of `books` table records

### Example
```json
{
  "yearNum": "-4004",
  "peopleBorn": [
    "recyYgUiSETdWFgEP",
    "recXhV7rg0zIf4OIB"
  ],
  "events": "God creates all things, God creates man and woman, Man falls into sin",
  "isoYear": -4003,
  "BC-AD": "BC",
  "formattedYear": "4004 BC",
  "modified": "2023-12-02T23:09:33.000Z"
}
```

## Places (40 Fields)
This table catalogs all geographic locations mentioned in the Bible. Each record includes identifying names (e.g. `kjvName`, `displayTitle`), geographic coordinates (e.g. `latitude`, `longitude`), and feature classifications (e.g. `featureType`, `featureSubType`). It also links to all `verses` mentioning the location, `events` that occurred there, and people associated with it.

### Fields Reference (40 Fields)

| Field | Type | Status | Description |
|-------|------|--------|-------------|
| `placeLookup` | string | Validated | Unique identifier using name and ID number |
| `openBibleLat` | string | Populated | Latitude from OpenBible.info |
| `openBibleLong` | string | Populated | Longitude from OpenBible.info |
| `kjvName` | string | Validated | Place name in the King James Version |
| `esvName` | string | Validated | Place Name in the English Standard Version (from OpenBible.info/geo) |
| `comment` | string | Incomplete | Comments from OpenBible.info/geo |
| `featureType` | string | Incomplete | Delineates, region, city, water, etc. Complete for the book of Acts |
| `verseCount` | integer | Validated | Counts how many verses mention this place by name |
| `placeID` | integer | Validated | Unique numerical identifier, useful to separate places which share the same name |
| `recogitoUri` | string | Populated | Links to an associated place in other historical databases |
| `recogitoLat` | string | Populated | Latitude from Recogito matches |
| `recogitoLon` | string | Populated | Longitude from Recogito matches |
| `verses` | array | Validated | Links to verse records mentioning this place by name |
| `recogitoStatus` | string | Populated | Verification of inks to other historical databases |
| `recogitoLabel` | string | Populated | Title from Recogito matches |
| `recogitoUID` | string | Populated | Unique ID for importing Recogito records |
| `latitude` | string | Populated | Best available latitude, depending on Recogito and OpenBible validation |
| `longitude` | string | Populated | Best available longitude, depending on Recogito and OpenBible validation |
| `status` | string | Temporary | The validation status of the individual place record |
| `displayTitle` | string | Populated | Disambiguated name suitable for page titles and search results |
| `alphaGroup` | string | Validated | Used for alphabetical indexing |
| `slug` | string | Validated | Lowercase, url-friendly version of placeLookup |
| `eastons` | array | Incomplete | Links to relevant sub-sections in Easton's dictionary. Complete for the book of Acts |
| `dictText` | array | Incomplete | Markdown-formatted text from relevant sub-section in Easton's dictionary. |
| `modified` | string | Unknown | Last modified date and time |
| `featureSubType` | string | Unknown | A more specific classification of the featureType, such as "River" for the "Water" type. |
| `rootID` | array | Temporary | If lat/Lon is borrowed from another place, this links to that record. |
| `peopleDied` | array | Validated | People who dies here, where known. |
| `precision` | string | Incomplete | Relative accuracy of lat/long assignment |
| `recogitoType` | string | Populated | Geographic type from Recogito matches |
| `hasBeenHere` | string | Incomplete | People who have been to this location. Complete for the book of Acts |
| `eventsHere` | array | Incomplete | Events which took place at the location. Complete for the book of Acts |
| `dictionaryLink` | string | Unknown | A URL to its Easton's Bible Dictionary entry at https://www.biblestudytools.com/dictionaries/eastons-bible-dictionary. |
| `dictionaryText` | string | Unknown | The text content from its Easton's Bible Dictionary entry. |
| `recogitoComments` | string | Populated | Notes on place assignments from Recogito |
| `ambiguous` | boolean | Temporary | Identifies display titles which have not been edited for disambiguation. |
| `aliases` | string | Populated | Alternate names for the same coordinate |
| `booksWritten` | array | Incomplete | Books written here, if known. |
| `duplicate_of` | array | Temporary | Identifies probable duplicates for data cleanup. |
| `peopleBorn` | array | Validated | People born here, where known |

### Relationships
- `verses` → References field `id` of `verses` table records
- `eastons` → References field `id` of `easton` table records
- `peopleDied` → References field `id` of `people` table records
- `hasBeenHere` → References subfield `personLookup` of field `fields` of `people` table records
- `eventsHere` → References field `id` of `events` table records
- `booksWritten` → References field `id` of `books` table records
- `duplicate_of` → References field `id` of `places` table records
- `peopleBorn` → References field `id` of `people` table records

### Example
```json
{
  "placeLookup": "egypt_362",
  "openBibleLat": "30.108086",
  "openBibleLong": "31.338220",
  "kjvName": "Egypt",
  "esvName": "Egypt",
  "comment": "region",
  "featureType": "Region",
  "verseCount": 564,
  "placeID": 362,
  "recogitoUri": "http://sws.geonames.org/357994",
  "recogitoLat": "26.4902014068366",
  "recogitoLon": "29.88079617",
  "verses": [
    "recX74cRHwDmYb1sK",
    "recPMnvB1cd7AQgro",
    ...
  ],
  "recogitoStatus": "VERIFIED",
  "recogitoLabel": "Egypt",
  "recogitoUID": "2f0169bb-b510-4688-8fca-9ea9ea19ed0d",
  "latitude": "26.4902014068366",
  "longitude": "29.88079617",
  "status": "publish",
  "displayTitle": "Egypt",
  "alphaGroup": "E",
  "slug": "egypt_362",
  "eastons": [
    "recaI03cdUrqCbVQE"
  ],
  "dictText": [
    "The land of the Nile and the pyramids, the oldest kingdom of which we have any record, holds a place of great significance in Scripture. *...(hidden for conciseness)*"
  ],
  "modified": "2021-05-06T20:48:10.000Z",
  "featureSubType": "Country",
  "rootID": [
    "recK0feE032FY9Hxi"
  ],
  "peopleDied": [
    "recPXtuWYdjyghv7R",
    "recsU2ZSdzBvDqzgI",
    "rechuDYJoK32gmrME"
  ],
  "precision": "Related-Surrounding",
  "recogitoType": "administrative-region",
  "hasBeenHere": "benjamin_463, moses_2108",
  "eventsHere": [
    "recbqTND1uSdqNjOx",
    "recwCFb0NhrYMkl8t",
    ...
  ],
  "dictionaryLink": "https://www.biblestudytools.com/dictionaries/eastons-bible-dictionary/egypt.html",
  "dictionaryText": " the land of the Nile and the pyramids, the oldest kingdom of which we have any record, holds a place of great significance in Scripture. *...(hidden for conciseness)*",
  "recogitoComments": "Use this as a label but not the modern borders",
  "peopleBorn": [
    "recv0dAY2ULzJ687g",
    "rechuDYJoK32gmrME",
    "recvZksoA0NmFrYZ7",
    "recjNRR60PAuFtjha"
  ]
}
```

## Verses (17 Fields)
This table contains the full text of every verse in the King James Version (`verseText`). Each verse is a fundamental unit of the dataset, identified by its `osisRef` (an ID using Open Scriptural Information Standard) and linked to its `book` and `chapter`. It also contains the core relational data, linking to the specific `people`, `places`, `peopleGroups`, and `event` referenced in its text.

### Fields Reference (17 Fields)

| Field | Type | Status | Description |
|-------|------|--------|-------------|
| `osisRef` | string | Validated | Unique identifier using the Open Scriptural Information Standard |
| `verseNum` | string | Validated | Verse Number (integer) |
| `verseText` | string | Validated | King James Version text, unformatted. |
| `book` | array | Validated | Link to the Book record |
| `people` | array | Validated | People mentioned in the verse text |
| `peopleCount` | integer | Validated | Number of people mentioned by name |
| `placesCount` | integer | Validated | Number of place mentioned by name |
| `yearNum` | integer | Populated | Year related to the verse from Torrey's Treasury of Scripture Knowledge. Not aligned with the events table. |
| `chapter` | array | Validated | Link to the Chapter record |
| `status` | string | Temporary | The validation status of the linkage between the verse and people, places, or events. |
| `mdText` | string | Populated | King James Version text, with markdown formatting for exports. |
| `richText` | string | Populated | King James Version text, with Rich Text formatting for Airtable. |
| `verseID` | string | Validated | Unique sequential identifier, useful for sorting. |
| `modified` | string | Unknown | Last modified date and time |
| `event` | array | Unknown | Links the group to IDs of relevant events. |
| `places` | array | Validated | Places mentioned in the verse text |
| `peopleGroups` | array | Incomplete | Groups of people mentioned in the verse text |

### Relationships
- `book` → References field `id` of `books` table records
- `people` → References field `id` of `people` table records
- `places` → References field `id` of `places` table records
- `chapter` → References field `id` of `chapters` table records
- `peopleGroups` → References field `id` of `peopleGroups` table records
- `event` → References field `id` of `events` table records

### Example
```json
{
  "osisRef": "Gen.2.8",
  "verseNum": "8",
  "verseText": "And the LORD God planted a garden eastward in Eden; and there he put the man whom he had formed.",
  "book": [
    "recIFusdNl6d8dj3L"
  ],
  "people": [
    "reccZB8SVU5bEMcgo"
  ],
  "peopleCount": 1,
  "placesCount": 1,
  "places": [
    "recLIUK6VRKNjnGo6"
  ],
  "yearNum": -4004,
  "chapter": [
    "recParAnlMHJy8vSQ"
  ],
  "status": "publish",
  "mdText": "And the [LORD]([/person/god_1324) [God]([/person/god_1324) planted a garden eastward in Eden; and there he put the man whom he had formed.",
  "richText": "And the [LORD](/person/god_1324) [God](/person/god_1324) planted a garden eastward in Eden; and there he put the man whom he had formed.\n",
  "verseID": "01002008",
  "modified": "2021-01-08T15:07:18.000Z",
  "event": [
    "recTU3ZxG7zQ61N9d"
  ]
}
```