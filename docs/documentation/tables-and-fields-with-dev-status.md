# Theographic Bible Metadata - Field Documentation

## Table: (Empty) - 3 fields
| Name | Status | Links to | Notes |
|------|--------|----------|-------|
| hasBeenHere | Incomplete |  | People who have been to this location. Complete for the book of Acts |
| personalNetwork | Incomplete |  | Relationships other than immediate family. Complete for the book of Acts. |
| hasBeenTo | Incomplete |  | Complete for the book of Acts |

---

## Table: books - 16 fields
| Name | Status | Links to | Notes |
|------|--------|----------|-------|
| osisName | Validated |  | Abbreviation matching the Open Scriptural Information Standard. |
| bookOrder | Validated |  | Order of books in the traditional Protestant canon, excluding Apocrypha. |
| bookName | Validated |  | Full name of the book |
| bookDiv | Validated |  | High-level divisions of the Bible |
| testament | Validated |  | Old or New Testament identifier |
| shortName | Validated |  | Shortest abbreviation, useful for small labels |
| slug | Validated |  | Lowercase, url-friendly version of Osis Name |
| yearWritten | Incomplete | periods | Approximate year written, if known. |
| placeWritten | Incomplete | places | Place the book was written, if known. |
| chapters | Validated | chapters | Links to records in the "chapters" table. |
| chapterCount | Validated | chapters | Total chapters |
| verses | Validated | chapters | Links to records in the "verses" table. |
| verseCount | Validated | chapters | Total verses |
| writers | Validated | chapters | Roll-up from Chapter-level writer assignment |
| peopleCount | Validated | people | Number of people mentioned by name within the book |
| placeCount | Validated | places | Number of places mentioned by name within the book |
| modified | Incomplete |  | Last modified date and time |
---

## Table: chapters - 9 fields
| Name | Status | Links to | Notes |
|------|--------|----------|-------|
| osisRef | Validated |  | Unique identifier using book.chapter |
| book | Validated | books | Links to records in the "book" table. |
| chapterNum | Validated |  |  |
| writer | Validated | people | Links to a person record, based on traditional understandings of authorship. |
| verses | Validated | verses |  Links to verse records of all verses within the chapter. |
| slug | Validated |  | Lowercase, url-friendly version of Osis Ref |
| peopleCount | Validated |  | Number of people mentioned by name within the chapter |
| placeCount | Validated |  | Number of places mentioned by name within the chapter |
| modified | Unknown |  | Last modified date and time |
---

## Table: easton - 9 fields|
Contains parsed entries from the XML version of Easton's Bible Dictionary. The data was sourced by programmatically fetching and processing the XML from http://www.ccel.org/ccel/easton/ebd2.xml. Each record represents a single dictionary term, with its associated definition and metadata extracted from the original XML structure to create a machine-readable format.
| Name | Status | Links to | Notes |
|------|--------|----------|-------|
| dictLookup | Validated |  | Unique string for a dictionary entry, split out by sub-paragraphs |
| index | Validated |  | Unique identifier |
| termID | Unknown |  | The id attribute of the <term> tag in the source XML. This ID indicates the location of the term within the original document's structure. For example, "a-p1.11" signifies that the term is in the "a" section, and within that section, it is associated with the paragraph block indexed as "p1" and is the 11th tagged element within that block. |
| termLabel | Validated |  | Title of the original entry |
| dictText | Validated |  | Text of the dictionary entry |
| def_id | Unknown |  | The id attribute of the <def> tag in the source XML. This ID directly corresponds to the termID and points to the definition block for that specific term. For example, if the termID is "a-p1.11", the corresponding def_id will be "a-p1.12". |
| has_list | Unknown |  | A boolean field ("True" or "False") that indicates whether the definition text contains a numbered or itemized list. This is derived from the structure of the source XML, though not explicitly shown in the provided snippet. |
| itemNum | Validated |  | Sub-section number, if multiple sections are listed in one entry |
| matchType | Temporary |  | Used to validate scripts which automatically match entities. |
| matchSlugs | Temporary |  | Used to check automatically matched slugs of entities in other tables |
| personLookup | Populated | people | Links to the "people" table |
| placeLookup | Populated | places | Links to the "places" table |

## Table: events - 19 fields
| Name | Status | Links to | Notes |
|------|--------|----------|-------|
| title | Incomplete |  | Unique title for an event |
| eventID | Unknown | | Unique identifier |
| sortKey | Incomplete |  | Uses a combination of year and verseSort to sort all events chronolgically. The calculation formula in airtable is `INT(IF(LEFT(startDate,1)='-',LEFT(startDate,5),LEFT(startDate,4))) + INT(verseSort)/100000000`|
| startDate | Incomplete |  | ISO formatted date to identify calendar dates where known |
| duration | Incomplete |  | Event length in days, years, etc. for use in end date calculations |
#TODO rangeFlag
| predecessor | Incomplete | events | Establishes predecessor-successor constraints if applicable |
| lag | Unknown | | The time elapsed between the predecessor event and the current event. |
| lagType | Unknown | | The type of predecessor relationship - either Start-to-Start (SS) or Finish-to-Start (FS). For example, for an event with lag of 130Y, lagType `FS` means that the event started 130 years after the predecessor event finished, whereas lagType `SS` means that the event started 130 years after the predecessor event started.|
| partOf | Unknown | events | Links an event to a larger event that it is a part of. |
| participants | Incomplete | people | Links people involved in the event |
| locations | Incomplete | places | Links to place records where the event took place |
| verses | Incomplete | verses | Verses which serve as an original narrative for the event |
| people (from verses) | Unknown | people | People who are mentioned in the verses associated with the event. |
| places (from verses) | Unknown | places | Locations that are mentioned in the verses associated with the event. |
| groups | Unknown | | Groups of people involved in the event. |
| notes | Unknown | | A field for additional commentary or explanatory notes about the event. |
| verseSort | Unknown | | The `verseID` of the first verse in the `verses` field of this event.|
| modified | Unknown |  | Last modified date and time |

## Table: people - 34 fields
| Name | Status | Links to | Notes |
|------|--------|----------|-------|
| personLookup | Validated |  | Unique identifier using name and ID number |
| status | Temporary |  | The validation status of the individual person record |
| personID | Validated |  | Unique numerical identifier, helping to distinguish people with the same name. |
| displayTitle | Populated |  | Disambiguated name suitable for page titles and search results |
| name | Validated |  | Primary name used in the text of the KJV |
| surname | Validated |  | Surname, if known. |
| alsoCalled | Populated |  | Alternate spellings or other known names for the same person. |
| isProperName | Validated |  | Identifies those with proper names vs. descriptive names like "Wife of..." or "Son of..." |
| ambiguous | Temporary |  | Identifies display titles which have not been edited for disambiguation. |
| Disambiguation (temp) | Temporary |  | Mechanical Turk entries used to aid in disambiguation |
| gender | Validated |  | Male or Female |
| occupations | Incomplete |  | The person's primary occupation, if known. |
| birthYear | Populated |  | Not yet aligned with passage/event timelines |
| minYear | Temporary |  | Temporary to help align birth year to passage/events timeline |
| deathYear | Populated |  | Not yet aligned with passage/event timelines |
| maxYear | Temporary |  | Temporary to help align birth year to passage/events timeline |
| birthPlace | Validated | places | Links to place records where the birth location is known |
| deathPlace | Validated | places | Links to place records where the death location is known |
| memberOf | Validated | peopleGroups | Links to peopleGroups if membership can be deduced. |
| dictionaryLink | Unknown | | A URL to its Easton's Bible Dictionary entry at https://www.biblestudytools.com/dictionaries/eastons-bible-dictionary. |
| dictionaryText | Unknown | | The text content from its Easton's Bible Dictionary entry. |
| eastons | Incomplete | easton | Links to relevant sub-sections in Easton's dictionary. Complete for the book of Acts |
| Easton's Count | Unknown | | 1 if it exists as an entry in Easton's Bible Dictionary; 0 otherwise.|
| dictText | Incomplete | easton | Markdown-formatted text from relevant sub-section in Easton's dictionary. |
| events | Incomplete | events | Events in which the person participated. Complete for the book of Acts |
| eventGroups | Incomplete | events | Lookup from events table to identify higher-level groups. |
| verseCount | Validated | verses | Counts verses where the person is mentioned by name |
| verses | Validated | verses | Verses where the person is mentioned by name |
| mother | Validated | people |  |
| father | Validated | people |  |
| children | Validated | people |  |
| siblings | Validated | people |  |
| halfSiblingsSameMother | Validated | people |  |
| halfSiblingsSameFather | Validated | people |  |
| chaptersWritten | Validated | people | Specific chapters written by this person according to traditional understanding of authorship. |
| alphaGroup | Validated |  | Used for alphabetical indexing |
| partners | Unknown | people | Links to the person's spouse or partner. |
| slug | Validated |  | Lowercase, url-friendly version of personLookup |
| timeline | Unknown | events | Links to events for the person. |
| modified | Unknown |  | Last modified date and time |
---

## Table: peopleGroups - 4 fields
| Name | Status | Links to | Notes |
|------|--------|----------|-------|
| groupName | Validated |  | Unique name |
| members | Validated | people | Links to a person record for members of this group |
| partOf | Unknown | peopleGroups | Links a group to a larger group it is a part of (e.g., each of the twelve tribes of Israel is part of the "Nation of Israel" group). |
| verses | Incomplete | verses | Verses mentioning this group |
| events | Incomplete | events | Events in which this group participated. |
| events_dev | Unknown | events | Links the group to IDs of relevant events. |
| modified | Unknown |  | Last modified date and time |
---

## Table: periods - 9 fields
| Name | Status | Links to | Notes |
|------|--------|----------|-------|
| yearNum | Incomplete |  | Integer for the year where negative values indicate BC, positive indicates AD |
| formattedYear | Validated |  | Formatted string for the year and AD/BC designation |
| era | Incomplete |  | grouping of multiple years. |
| isoYear | Validated |  | ISO-8601 standard year number (accounts for the non-existence of year 0) |
| BC-AD | Incomplete |  | Groups AD and BC years |
| peopleBorn | Incomplete | people | People born that year, if known. |
| peopleDied | Incomplete | people | People who died that year, if known. |
| events | Incomplete | events | Events which occurred in that year. Complete for the book of Acts. |
| booksWritten | Incomplete | books | Books of the bible written that year, if known. |
| modified | Unknown |  | Last modified date and time |
---

## Table: places - 40 fields
| Name | Status | Links to | Notes |
|------|--------|----------|-------|
| placeLookup | Validated |  | Unique identifier using name and ID number |
| status | Temporary |  | The validation status of the individual place record |
| displayTitle | Populated |  | Disambiguated name suitable for page titles and search results |
| ambiguous | Temporary |  | Identifies display titles which have not been edited for disambiguation. |
| duplicate_of | Temporary |  | Identifies probable duplicates for data cleanup. |
| placeID | Validated |  | Unique numerical identifier, useful to separate places which share the same name |
| latitude | Populated |  | Best available latitude, depending on Recogito and OpenBible validation |
| longitude | Populated |  | Best available longitude, depending on Recogito and OpenBible validation |
| kjvName | Validated |  | Place name in the King James Version |
| esvName | Validated |  | Place Name in the English Standard Version (from OpenBible.info/geo) |
| featureType | Incomplete |  | Delineates, region, city, water, etc. Complete for the book of Acts |
| openBibleLat | Populated |  | Latitude from OpenBible.info |
| openBibleLong | Populated |  | Longitude from OpenBible.info |
| rootID | Temporary |  | If lat/Lon is borrowed from another place, this links to that record. |
| precision | Incomplete |  | Relative accuracy of lat/long assignment |
| aliases | Populated |  | Alternate names for the same coordinate |
| comment | Incomplete |  | Comments from OpenBible.info/geo |
| dictionaryLink | Unknown | | A URL to its Easton's Bible Dictionary entry at https://www.biblestudytools.com/dictionaries/eastons-bible-dictionary. |
| dictionaryText | Unknown | | The text content from its Easton's Bible Dictionary entry. |
| verses | Validated | verses | Links to verse records mentioning this place by name |
| verseCount | Validated | verses | Counts how many verses mention this place by name |
| eastons | Incomplete | easton | Links to relevant sub-sections in Easton's dictionary. Complete for the book of Acts |
| dictText | Incomplete | easton | Markdown-formatted text from relevant sub-section in Easton's dictionary. |
| recogitoUri | Populated |  | Links to an associated place in other historical databases |
| recogitoLat | Populated |  | Latitude from Recogito matches |
| recogitoLon | Populated |  | Longitude from Recogito matches |
| peopleBorn | Validated | people | People born here, where known |
| peopleDied | Validated | people | People who dies here, where known. |
| hasBeenHere | Incomplete |  | People who have been to this location. Complete for the book of Acts |
| recogitoStatus | Populated |  | Verification of inks to other historical databases |
| recogitoComments | Populated |  | Notes on place assignments from Recogito |
| recogitoType | Populated |  | Geographic type from Recogito matches |
| recogitoLabel | Populated |  | Title from Recogito matches |
| recogitoUID | Populated |  | Unique ID for importing Recogito records |
| booksWritten | Incomplete | books | Books written here, if known. |
| eventsHere | Incomplete | events | Events which took place at the location. Complete for the book of Acts |
| alphaGroup | Validated |  | Used for alphabetical indexing |
| slug | Validated |  | Lowercase, url-friendly version of placeLookup |
| featureSubType | Unknown | | A more specific classification of the featureType, such as "River" for the "Water" type. |
| modified | Unknown |  | Last modified date and time |
---

## Table: verses - 18 fields
| Name | Status | Links to | Notes |
|------|--------|----------|-------|
| osisRef | Validated |  | Unique identifier using the Open Scriptural Information Standard |
| status | Temporary |  | The validation status of the linkage between the verse and people, places, or events. |
| verseID | Validated |  | Unique sequential identifier, useful for sorting. |
| book | Validated | books | Link to the Book record |
| chapter | Validated | chapters | Link to the Chapter record |
| verseNum | Validated |  | Verse Number (integer) |
| verseText | Validated |  | King James Version text, unformatted. |
| richText | Populated |  | King James Version text, with Rich Text formatting for Airtable. |
| mdText | Populated |  | King James Version text, with markdown formatting for exports. |
| people | Validated | people | People mentioned in the verse text |
| peopleCount | Validated | people | Number of people mentioned by name |
| places | Validated | places | Places mentioned in the verse text |
| placesCount | Validated | places | Number of place mentioned by name |
| yearNum | Populated |  | Year related to the verse from Torrey's Treasury of Scripture Knowledge. Not aligned with the events table. |
| peopleGroups | Incomplete | peopleGroups | Groups of people mentioned in the verse text |
| eventsReferenced | Incomplete | events | If this verse references a prior event and does not serve as an original narrative, this links to the referenced event. |
| quotesFrom | Incomplete | verses | If the text is a quotation from another verse, this links to the quoted source |
#TODO event
| modified | Unknown |  | Last modified date and time |
---

### TODO
A JSON that gets data from a source XML 
| Name | Status | Links to | Notes |
|------|--------|----------|-------|
| dictLookup | Validated |  | Unique string for a dictionary entry, split out by sub-paragraphs |
| index | Validated |  | A zero-based numerical index for each record in the JSON array, ensuring a unique identifier for each entry. |

| termLabel | Validated |  | The dictionary term being defined. |
| dictText | Validated |  | The full definition text for the term. This field may contain Markdown-style links and newline characters (\n) for paragraph breaks. |


| itemNum | Validated |  | 	Indicates the item number for definitions that are part of a list (e.g., 1, 2, 3). This occurs when multiple definitions exist for the same word and they are itemized. Defaults to 0 for entries that are not itemized. |
| matchType | Temporary |  | Used to validate scripts which automatically match entities. |
| matchSlugs | Temporary |  | Used to check automatically matched slugs of entities in other tables |
| personLookup | Populated | people | An array of record IDs that link to corresponding entries in the 'people' JSON. Each ID represents a person mentioned in the dictText. |
| placeLookup | Populated | places | An array of record IDs that link to corresponding entries in the 'places' JSON. Each ID represents a place mentioned in the dictText. |