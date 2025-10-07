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
| osisName | Validated |  | Abbreviation matching the Open Scriptural Information Standard |
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

---

## Table: chapters - 8 fields
| Name | Status | Links to | Notes |
|------|--------|----------|-------|
| osisRef | Validated |  | Unique identifier using book.chapter |
| book | Validated | books |  |
| chapterNum | Validated |  |  |
| writer | Validated | people | Links to a person record, based on traditional understandings of authorship. |
| verses | Validated | verses |  |
| slug | Validated |  | Lowercase, url-friendly version of Osis Ref |
| peopleCount | Validated |  | Number of people mentioned by name within the chapter |
| placeCount | Validated |  | Number of places mentioned by name within the chapter |

---

## Table: easton - 9 fields
| Name | Status | Links to | Notes |
|------|--------|----------|-------|
| dictLookup | Validated |  | Unique string for a dictionary entry, split out by sub-paragraphs |
| index | Validated |  | Unique identifier |
| termLabel | Validated |  | Title of the original entry |
| dictText | Validated |  | Text of the dictionary entry |
| itemNum | Validated |  | Sub-section number, if multiple sections are listed in one entry |
| matchType | Temporary |  | Used to validate scripts which automatically match entities. |
| matchSlugs | Temporary |  | Used to check automatically matched slugs of entities in other tables |
| personLookup | Populated | people | Links to the "people" table |
| placeLookup | Populated | places | Links to the "places" table |

---

## Table: events - 19 fields
| Name | Status | Links to | Notes |
|------|--------|----------|-------|
| eventName | Incomplete |  | Unique title for an event |
| sequence | Incomplete |  | Puts events in order where multiple events fall in one year and more precise dates are unknown. |
| eventGroup | Incomplete |  | Groups multiple events in broader categories |
| sortKey | Incomplete |  | Uses a combination of year and sequence to sort all events chronolgically. |
| startDate | Incomplete |  | ISO formatted date to identify calendar dates where known |
| years | Incomplete | periods | Link to periods to get multiple year formats and identify eras |
| startYear | Incomplete | periods | minimum year, ISO standard format |
| duration | Incomplete |  | Event length in days, years, etc. for use in end date calculations |
| minYearLookup | Temporary | verses | Minimum year from verses table, used for data validation and consistency checks |
| maxYearLookup | Temporary | verses | Maximum year from verses table, used for data validation and consistency checks |
| preceedingEvent | Incomplete | events | Establishes predecessor-successor constraints if applicable |
| Event Group | Incomplete |  | Groups events into a higher level for simplified views of longer time ranges |
| participants | Incomplete | people | Links people involved in the event |
| participantGroups | Incomplete | peopleGroups | Links groups involved in the event |
| placeOccurred | Incomplete | places | Links to place records where the event took place |
| versesDescribed | Incomplete | verses | Verses which serve as an original narrative for the event |
| versesReferenced | Incomplete | verses | Verses which refer to a prior event and do not serve as the original narrative for that event. |
| verseCount | Incomplete |  | Number of verses related to the event |
| slug | Incomplete |  | Lowercase, url-friendly version of event group name |

---

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
| eastons | Incomplete | easton | Links to relevant sub-sections in Easton's dictionary. Complete for the book of Acts |
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
| slug | Validated |  | Lowercase, url-friendly version of personLookup |

---

## Table: peopleGroups - 4 fields
| Name | Status | Links to | Notes |
|------|--------|----------|-------|
| groupName | Validated |  | Unique name |
| members | Validated | people | Links to a person record for members of this group |
| verses | Incomplete | verses | Verses mentioning this group |
| events | Incomplete | events | Events in which this group participated. |

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

---

## Table: places - 35 fields
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
| Aliases | Populated |  | Alternate names for the same coordinate |
| comment | Incomplete |  | Comments from OpenBible.info/geo |
| verses | Validated | verses | Links to verse records mentioning this place by name |
| verseCount | Validated | verses | Counts how many verses mention this place by name |
| eastons | Incomplete | easton | Links to relevant sub-sections in Easton's dictionary. Complete for the book of Acts |
| dictText | Incomplete | easton | Markdown-formatted text from relevant sub-section in Easton's dictionary. |
| recogitoUri | Populated |  | Links to an associated place in other historical databases |
| recogitoLat | Populated |  | Latitude from Recogito matches |
| recogitoLon | Populated |  | Longitude from Recogito matches |
| peopleBorn | Validated | people | People born here, where known |
| peopleDied | Validated | people | People who dies here, where known. |
| recogitoStatus | Populated |  | Verification of inks to other historical databases |
| recogitoComments | Populated |  | Notes on place assignments from Recogito |
| recogitoType | Populated |  | Geographic type from Recogito matches |
| recogitoLabel | Populated |  | Title from Recogito matches |
| recogitoUID | Populated |  | Unique ID for importing Recogito records |
| booksWritten | Incomplete | books | Books written here, if known. |
| eventsHere | Incomplete | events | Events which took place at the location. Complete for the book of Acts |
| alphaGroup | Validated |  | Used for alphabetical indexing |
| slug | Validated |  | Lowercase, url-friendly version of placeLookup |

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
| eventsDescribed | Incomplete | events | If the text is an original narrative for an event, this links to those details. |
| eventsReferenced | Incomplete | events | If this verse references a prior event and does not serve as an original narrative, this links to the referenced event. |
| quotesFrom | Incomplete | verses | If the text is a quotation from another verse, this links to the quoted source |

---

