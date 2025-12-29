# Category Level

## Properties
- **Shark_Name** (string)
- **Classification** (string)
- **Status** (string)

---

## Outgoing Relationships

### Category → Kind

- **Source (Level):** Category  
- **Grouping Labels:** *(none)*  
- **Utility Labels:** SharkNode  

➡ **Relationship:** `Category --[Kind]--> Aircraft`

---

### Category → Kind

- **Source (Level):** Category  
- **Grouping Labels:** Maritime  
- **Utility Labels:** SharkNode  

➡ **Relationship:** `Category --[Kind]--> Vessel`

---

## Incoming Relationships

### Hub → Category

- **Source Level:** Hub  
- **Grouping Labels:** *(none)*  
- **Utility Labels:** SharkNode  

➡ **Relationship:** `Hub --[Category]--> Category`
