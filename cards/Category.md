\newpage

# Category Level

## Labels
- **Grouping:** AirVehicle, Armament, Category, Location, People, SeaVessel, SharkNode

## Nodes (Shark_Name)
- Aircraft
- Organization
- Place
- Ship
- Weapon

## Properties
- `Classification` (unknown, optional)
- `Primary_Affiliation` (unknown, optional)
- `Shark_Name` (string, required)
- `Shark_UUID` (unknown, optional)
- `Status` (unknown, optional)

## Relationships

### Outgoing
- (Aircraft)-[Kind]->(Manned)  
  **Source Labels:** AirVehicle, Category, SharkNode  
  **Target Labels:** AirKind, AirVehicle, Kind, SharkNode  

- (Aircraft)-[Kind]->(Unmanned)  
  **Source Labels:** AirVehicle, Category, SharkNode  
  **Target Labels:** AirKind, AirVehicle, Kind, SharkNode  

- (Organization)-[Kind]->(International)  
  **Source Labels:** Category, People, SharkNode  
  **Target Labels:** Kind, OrgKind, People, SharkNode  

- (Organization)-[Kind]->(National)  
  **Source Labels:** Category, People, SharkNode  
  **Target Labels:** Kind, OrgKind, People, SharkNode  

- (Place)-[Kind]->(Africa)  
  **Source Labels:** Category, Location, SharkNode  
  **Target Labels:** Continent, Kind, Location, Object, SharkNode  

- (Place)-[Kind]->(Asia)  
  **Source Labels:** Category, Location, SharkNode  
  **Target Labels:** Continent, Kind, Location, Object, SharkNode  

- (Place)-[Kind]->(Continent of Antarctica)  
  **Source Labels:** Category, Location, SharkNode  
  **Target Labels:** Continent, Kind, Location, Object, SharkNode  

- (Place)-[Kind]->(Continent of Australia)  
  **Source Labels:** Category, Location, SharkNode  
  **Target Labels:** Continent, Kind, Location, Object, SharkNode  

- (Place)-[Kind]->(Europe)  
  **Source Labels:** Category, Location, SharkNode  
  **Target Labels:** Continent, Kind, Location, Object, SharkNode  

- (Place)-[Kind]->(North America)  
  **Source Labels:** Category, Location, SharkNode  
  **Target Labels:** Continent, Kind, Location, Object, SharkNode  

- (Place)-[Kind]->(Oceanic Islands)  
  **Source Labels:** Category, Location, SharkNode  
  **Target Labels:** Continent, Kind, Location, Object, SharkNode  

- (Place)-[Kind]->(South America)  
  **Source Labels:** Category, Location, SharkNode  
  **Target Labels:** Continent, Kind, Location, Object, SharkNode  

- (Ship)-[Kind]->(Merchant)  
  **Source Labels:** Category, SeaVessel, SharkNode  
  **Target Labels:** Kind, SeaVessel, SharkNode, ShipKind  

- (Ship)-[Kind]->(Naval)  
  **Source Labels:** Category, SeaVessel, SharkNode  
  **Target Labels:** Kind, SeaVessel, SharkNode, ShipKind  

- (Weapon)-[Kind]->(Bombs)  
  **Source Labels:** Armament, Category, SharkNode  
  **Target Labels:** Armament, Kind, SharkNode, WeaponKind  

- (Weapon)-[Kind]->(Missile)  
  **Source Labels:** Armament, Category, SharkNode  
  **Target Labels:** Armament, Kind, SharkNode, WeaponKind  

- (Weapon)-[Kind]->(Projectile)  
  **Source Labels:** Armament, Category, SharkNode  
  **Target Labels:** Armament, Kind, SharkNode, WeaponKind  

- (Weapon)-[Kind]->(Torpedo)  
  **Source Labels:** Armament, Category, SharkNode  
  **Target Labels:** Armament, Kind, SharkNode, WeaponKind  

