# Theographic Bible Metadata - JSON Fields Documentation

## Books (17 Fields)

### Field Reference

| Field | Type | Status | Description |
|-------|------|--------|-------------|
| `osisName` |  | Validated | Abbreviation matching the Open Scriptural Information Standard |
| `bookOrder` |  | Validated | Order of books in the traditional Protestant canon, excluding Apocrypha |
| `bookName` |  | Validated | Full name of the book |
| `bookDiv` |  | Validated | High-level divisions of the Bible |
| `testament` |  | Validated | Old or New Testament identifier |
| `shortName` |  | Validated | Shortest abbreviation, useful for small labels |
| `slug` |  | Validated | Lowercase, url-friendly version of Osis Name |
| `yearWritten` |  | Incomplete | Approximate year written, if known |
| `placeWritten` |  | Incomplete | Place the book was written, if known |
| `chapters` |  | Validated | Links to records in the "chapters" table |
| `chapterCount` |  | Validated | Total chapters |
| `verses` |  | Validated | Links to records in the "verses" table |
| `verseCount` |  | Validated | Total verses |
| `writers` |  | Validated | Roll-up from Chapter-level writer assignment |
| `peopleCount` |  | Validated | Number of people mentioned by name within the book |
| `placeCount` |  | Validated | Number of places mentioned by name within the book |
| `modified` |  | Incomplete | Last modified date and time |

### Relationships
- `chapters` → References `chapters` table records
- `verses` → References `verses` table records
- `writers` → References `people` table records
- `yearWritten` → References `periods` table
- `placeWritten` → References `places` table

### Example
```json
{
  "osisName": "Gen",
  "bookOrder": 1,
  "bookName": "Genesis",
  "bookDiv": "Pentateuch",
  "testament": "Old Testament",
  "shortName": "Ge",
  "slug": "gen",
  "chapterCount": 50,
  "verseCount": 1533,
  "writers": ["moses_2108"],
  "peopleCount": 1082,
  "placeCount": 266
}