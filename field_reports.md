### books.json
Field names (order of first appearance):
- osisName
- bookName
- chapterCount
- bookDiv
- shortName
- bookOrder
- verses
- verseCount
- chapters
- writers
- testament
- slug
- peopleCount
- placeCount
- yearWritten
- placeWritten

Field type summary:
osisName: string
bookName: string
chapterCount: integer
bookDiv: string
shortName: string
bookOrder: integer
verses: array
verseCount: integer
chapters: array
writers: array
testament: string
slug: string
peopleCount: integer
placeCount: integer
yearWritten: array
placeWritten: array

Sample object (with max fields):
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
      "recld8Sxx8yDn1Ik8",
      "reczZ8CrNFwW1n6MD",
      *...(hidden for conciseness)*
    ],
    "yearWritten": [
      "recvOFi9OkrgM1IAO"
    ],
    "placeWritten": [
      "recpmPd6JhbqhqA0Q"
    ],
    "verseCount": 433,
    "chapters": [
      "recMCMGLnVg4olx48",
      "recMcLBnD88gjBXir",
      *...(hidden for conciseness)*
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

### chapters.json
Field names (order of first appearance):
- osisRef
- book
- chapterNum
- writer
- verses
- slug
- peopleCount
- placesCount
- modified
- writer count

Field type summary:
osisRef: string
book: array
chapterNum: integer
writer: array
verses: array
slug: string
peopleCount: integer
placesCount: integer
modified: string
writer count: integer

Sample object (with max fields):
{
  "id": "recRAcqtgn28zXm1a",
  "createdTime": "2018-06-01T13:12:45.000Z",
  "fields": {
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
      *...(hidden for conciseness)*
    ],
    "slug": "1chr_1",
    "peopleCount": 54,
    "placesCount": 8,
    "modified": "2019-08-08T01:43:21.000Z",
    "writer count": 1
  }
}

### easton.json
Field names (order of first appearance):
- dictLookup
- termID
- termLabel
- def_id
- has_list
- itemNum
- matchType
- matchSlugs
- dictText
- index
- personLookup
- placeLookup

Field type summary:
dictLookup: string
termID: string
termLabel: string
def_id: string
has_list: string
itemNum: integer
matchType: string
matchSlugs: string
dictText: string
index: integer
personLookup: array
placeLookup: array

Sample object (with max fields):
{
  "id": "recoeKZq3dxVIkGSU",
  "createdTime": "2019-07-08T22:44:33.000Z",
  "fields": {
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
}

### events.json
Field names (order of first appearance):
- title
- startDate
- duration
- participants
- verses
- verseSort
- modified
- sortKey
- people (from verses)
- eventID
- locations
- partOf
- places (from verses)
- predecessor
- rangeFlag
- lag
- lagType
- notes
- groups

Field type summary:
title: string
startDate: string
duration: string
participants: array
verses: array
verseSort: string
modified: string
sortKey: float
people (from verses): array
eventID: integer
locations: array
partOf: array
places (from verses): array
predecessor: array
rangeFlag: boolean
lag: string
lagType: string
notes: string
groups: array

Sample object (with max fields):
{
  "id": "recXveJRjCtPNMLqs",
  "createdTime": "2020-08-20T20:43:12.000Z",
  "fields": {
    "title": "Birth of Abraham",
    "startDate": "-1996",
    "duration": "1D",
    "participants": [
      "reccdFYIq50NyxNej",
      "recXBYSWubfkpqNQm"
    ],
    "locations": [
      "recgQtoCtBjbsPwAw"
    ],
    "verses": [
      "rec4ayUcZnUN9fhUl",
      "recuJqyP43vbWJbzj"
    ],
    "predecessor": [
      "recePREjv2zZ8Esoo"
    ],
    "lag": "130Y",
    "partOf": [
      "recfnatCOLEHFYeLB"
    ],
    "notes": "Not all of Terah's sons would have been born the same year. In light of Acts 7:4 and Genesis 12:4, Abraham was born when Terah was 130 years old.\n",
    "verseSort": "01011026",
    "modified": "2020-11-25T15:12:15.000Z",
    "sortKey": -1995.98988974,
    "people (from verses)": [
      "recXBYSWubfkpqNQm",
      "reccdFYIq50NyxNej",
      *...(hidden for conciseness)*
    ],
    "lagType": "FS",
    "eventID": 65
  }
}

### people.json
Field names (order of first appearance):
- personLookup
- personID
- name
- isProperName
- gender
- birthYear
- deathYear
- memberOf
- birthPlace
- deathPlace
- dictionaryLink
- dictionaryText
- verseCount
- verses
- siblings
- mother
- father
- children
- minYear
- maxYear
- displayTitle
- status
- alphaGroup
- slug
- partners
- eastons
- Easton's Count
- dictText
- modified
- timeline
- ambiguous
- Disambiguation (temp)
- events
- alsoCalled
- halfSiblingsSameMother
- halfSiblingsSameFather
- chaptersWritten
- surname

Field type summary:
personLookup: string
personID: integer
name: string
isProperName: boolean
gender: string
birthYear: array
deathYear: array
memberOf: array
birthPlace: array
deathPlace: array
dictionaryLink: string
dictionaryText: string
verseCount: integer
verses: array
siblings: array
mother: array
father: array
children: array
minYear: integer
maxYear: integer
displayTitle: string
status: string
alphaGroup: string
slug: string
partners: array
eastons: array
Easton's Count: integer
dictText: array
modified: string
timeline: array
ambiguous: boolean
Disambiguation (temp): string
events: string
alsoCalled: string
halfSiblingsSameMother: array
halfSiblingsSameFather: array
chaptersWritten: array
surname: string

Sample object (with max fields):
{
  "id": "rechuDYJoK32gmrME",
  "createdTime": "2018-03-19T00:26:39.000Z",
  "fields": {
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
      *...(hidden for conciseness)*
    ],
    "siblings": [
      "recBOUtTncbBlfEn9"
    ],
    "halfSiblingsSameFather": [
      "rectGDQCkKqZ6LgGB",
      "rec3HzZknu1HOvNci",
      *...(hidden for conciseness)*
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
      *...(hidden for conciseness)*
    ]
  }
}

### peopleGroups.json
Field names (order of first appearance):
- groupName
- members
- modified
- events_dev
- verses
- partOf
- events

Field type summary:
groupName: string
members: array
modified: string
events_dev: array
verses: array
partOf: array
events: string

Sample object (with max fields):
{
  "id": "reciI2noa29XOlF3E",
  "createdTime": "2018-03-19T00:37:26.000Z",
  "fields": {
    "groupName": "Tribe of Judah",
    "members": [
      "recYIZfi53zX3NJh0",
      "recEg9i0J2MgmkZr8",
      *...(hidden for conciseness)*
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
}

### periods.json
Field names (order of first appearance):
- yearNum
- peopleBorn
- events
- isoYear
- BC-AD
- formattedYear
- modified
- peopleDied
- booksWritten

Field type summary:
yearNum: string
peopleBorn: array
events: string
isoYear: integer
BC-AD: string
formattedYear: string
modified: string
peopleDied: array
booksWritten: array

Sample object (with max fields):
{
  "id": "recPI0EyJYFA3IUUZ",
  "createdTime": "2018-04-28T22:40:37.000Z",
  "fields": {
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
}

### places.json
Field names (order of first appearance):
- placeLookup
- openBibleLat
- openBibleLong
- kjvName
- esvName
- comment
- featureType
- verseCount
- placeID
- recogitoUri
- recogitoLat
- recogitoLon
- verses
- recogitoStatus
- recogitoLabel
- recogitoUID
- latitude
- longitude
- status
- displayTitle
- alphaGroup
- slug
- eastons
- dictText
- modified
- featureSubType
- rootID
- peopleDied
- precision
- recogitoType
- hasBeenHere
- eventsHere
- dictionaryLink
- dictionaryText
- recogitoComments
- ambiguous
- aliases
- booksWritten
- duplicate_of
- peopleBorn

Field type summary:
placeLookup: string
openBibleLat: string
openBibleLong: string
kjvName: string
esvName: string
comment: string
featureType: string
verseCount: integer
placeID: integer
recogitoUri: string
recogitoLat: string
recogitoLon: string
verses: array
recogitoStatus: string
recogitoLabel: string
recogitoUID: string
latitude: string
longitude: string
status: string
displayTitle: string
alphaGroup: string
slug: string
eastons: array
dictText: array
modified: string
featureSubType: string
rootID: array
peopleDied: array
precision: string
recogitoType: string
hasBeenHere: string
eventsHere: array
dictionaryLink: string
dictionaryText: string
recogitoComments: string
ambiguous: boolean
aliases: string
booksWritten: array
duplicate_of: array
peopleBorn: array

Sample object (with max fields):
{
  "id": "recfrXyxhuYOczKTm",
  "createdTime": "2017-09-19T23:40:41.000Z",
  "fields": {
    "placeLookup": "egypt_362",
    "openBibleLat": "30.108086",
    "openBibleLong": "31.338220",
    "kjvName": "Egypt",
    "esvName": "Egypt",
    "comment": "region",
    "precision": "Related-Surrounding",
    "featureType": "Region",
    "rootID": [
      "recK0feE032FY9Hxi"
    ],
    "dictionaryLink": "https://www.biblestudytools.com/dictionaries/eastons-bible-dictionary/egypt.html",
    "dictionaryText": " the land of the Nile and the pyramids, the oldest kingdom of which we have any record, holds a place of great significance in Scripture. *...(hidden for conciseness)*",
    "verseCount": 564,
    "placeID": 362,
    "recogitoUri": "http://sws.geonames.org/357994",
    "recogitoLat": "26.4902014068366",
    "recogitoLon": "29.88079617",
    "peopleBorn": [
      "recv0dAY2ULzJ687g",
      "rechuDYJoK32gmrME",
      "recvZksoA0NmFrYZ7",
      "recjNRR60PAuFtjha"
    ],
    "peopleDied": [
      "recPXtuWYdjyghv7R",
      "recsU2ZSdzBvDqzgI",
      "rechuDYJoK32gmrME"
    ],
    "verses": [
      "recX74cRHwDmYb1sK",
      "recPMnvB1cd7AQgro",
      *...(hidden for conciseness)*
    ],
    "recogitoStatus": "VERIFIED",
    "recogitoComments": "Use this as a label but not the modern borders",
    "recogitoLabel": "Egypt",
    "recogitoUID": "2f0169bb-b510-4688-8fca-9ea9ea19ed0d",
    "hasBeenHere": "benjamin_463, moses_2108",
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
    "eventsHere": [
      "recbqTND1uSdqNjOx",
      "recwCFb0NhrYMkl8t",
      *...(hidden for conciseness)*
    ],
    "featureSubType": "Country"
  }
}

### verses.json
Field names (order of first appearance):
- osisRef
- verseNum
- verseText
- book
- people
- peopleCount
- placesCount
- yearNum
- chapter
- status
- mdText
- richText
- verseID
- modified
- event
- places
- peopleGroups

Field type summary:
osisRef: string
verseNum: string
verseText: string
book: array
people: array
peopleCount: integer
placesCount: integer
yearNum: integer
chapter: array
status: string
mdText: string
richText: string
verseID: string
modified: string
event: array
places: array
peopleGroups: array

Sample object (with max fields):
{
  "id": "recmb6LrwBeHu6MJK",
  "createdTime": "2018-05-13T17:36:24.000Z",
  "fields": {
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
}
