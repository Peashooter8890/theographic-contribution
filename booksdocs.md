# Theographic Bible Metadata - JSON Fields Documentation

## Books (16 Fields)

### Field Reference

| Field | Type | Status | Description |
|-------|------|--------|-------------|
| `osisName` | string | Validated | Abbreviation matching the Open Scriptural Information Standard. |
| `bookName` | string | Validated | Full name of the book |
| `chapterCount` | integer | Validated | Total chapters |
| `bookDiv` | string | Validated | High-level divisions of the Bible |
| `shortName` | string | Validated | Shortest abbreviation, useful for small labels |
| `bookOrder` | integer | Validated | Order of books in the traditional Protestant canon, excluding Apocrypha. |
| `verses` | array | Validated | Links to records in the "verses" table. |
| `verseCount` | integer | Validated | Total verses |
| `chapters` | array | Validated | Links to records in the "chapters" table. |
| `writers` | array | Validated | Roll-up from Chapter-level writer assignment |
| `testament` | string | Validated | Old or New Testament identifier |
| `slug` | string | Validated | Lowercase, url-friendly version of Osis Name |
| `peopleCount` | integer | Validated | Number of people mentioned by name within the book |
| `placeCount` | integer | Validated | Number of places mentioned by name within the book |
| `yearWritten` | array | Incomplete | Approximate year written, if known. |
| `placeWritten` | array | Incomplete | Place the book was written, if known. |

### Relationships
## TODO add what field it references, not all reference pure id
- `verses` → References `verses` table records
- `chapters` → References `chapters` table records
- `writers` → References `people` table records
- `yearWritten` → References `periods` table
- `placeWritten` → References `places` table

### Example
```json
{
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
```