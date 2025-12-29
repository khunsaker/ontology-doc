\newpage

# Kind Level

## Labels
- **Grouping:** AirKind, AirVehicle, Armament, Continent, Kind, Location, Object, OrgKind, People, SeaVessel, SharkNode, ShipKind, WeaponKind

## Nodes (Shark_Name)
- Africa
- Asia
- Bombs
- Continent of Antarctica
- Continent of Australia
- Europe
- International
- Manned
- Merchant
- Missile
- National
- Naval
- North America
- Oceanic Islands
- Projectile
- South America
- Torpedo
- Unmanned

## Properties
- `Classification` (unknown, optional)
- `Primary_Affiliation` (unknown, optional)
- `Shark_Name` (string, required)
- `Shark_UUID` (unknown, optional)
- `Status` (unknown, optional)

## Relationships

### Outgoing
- (Bombs)-[Family]->(Cluster Bomb)  
  **Source Labels:** Armament, Kind, SharkNode, WeaponKind  
  **Target Labels:** Armament, Family, SharkNode, WeaponFamily  

- (Bombs)-[Family]->(Guided Bomb)  
  **Source Labels:** Armament, Kind, SharkNode, WeaponKind  
  **Target Labels:** Armament, Family, SharkNode, WeaponFamily  

- (Bombs)-[Family]->(Nuclear Bomb)  
  **Source Labels:** Armament, Kind, SharkNode, WeaponKind  
  **Target Labels:** Armament, Family, SharkNode, WeaponFamily  

- (Bombs)-[Family]->(Unguided Bomb)  
  **Source Labels:** Armament, Kind, SharkNode, WeaponKind  
  **Target Labels:** Armament, Family, SharkNode, WeaponFamily  

- (Manned)-[Family]->(Fixed Wing)  
  **Source Labels:** AirKind, AirVehicle, Kind, SharkNode  
  **Target Labels:** AirFamily, AirVehicle, Family, SharkNode  

- (Manned)-[Family]->(Hybrid)  
  **Source Labels:** AirKind, AirVehicle, Kind, SharkNode  
  **Target Labels:** AirFamily, AirVehicle, Family, SharkNode  

- (Manned)-[Family]->(Lighter Than Air)  
  **Source Labels:** AirKind, AirVehicle, Kind, SharkNode  
  **Target Labels:** AirFamily, AirVehicle, Family, SharkNode  

- (Manned)-[Family]->(Rotary)  
  **Source Labels:** AirKind, AirVehicle, Kind, SharkNode  
  **Target Labels:** AirFamily, AirVehicle, Family, SharkNode  

- (Merchant)-[Family]->(Industrial - Merchant)  
  **Source Labels:** Kind, SeaVessel, SharkNode, ShipKind  
  **Target Labels:** Family, SeaVessel, SharkNode, ShipFamily  

- (Merchant)-[Family]->(Merchant Cargo)  
  **Source Labels:** Kind, SeaVessel, SharkNode, ShipKind  
  **Target Labels:** Family, SeaVessel, SharkNode, ShipFamily  

- (Merchant)-[Family]->(Passenger Ships)  
  **Source Labels:** Kind, SeaVessel, SharkNode, ShipKind  
  **Target Labels:** Family, SeaVessel, SharkNode, ShipFamily  

- (Merchant)-[Family]->(Small Craft)  
  **Source Labels:** Kind, SeaVessel, SharkNode, ShipKind  
  **Target Labels:** Family, SeaVessel, SharkNode, ShipFamily  

- (Merchant)-[Family]->(Special Purpose Craft)  
  **Source Labels:** Kind, SeaVessel, SharkNode, ShipKind  
  **Target Labels:** Family, SeaVessel, SharkNode, ShipFamily  

- (Merchant)-[Family]->(Support Ships)  
  **Source Labels:** Kind, SeaVessel, SharkNode, ShipKind  
  **Target Labels:** Family, SeaVessel, SharkNode, ShipFamily  

- (Missile)-[Family]->(Decoy)  
  **Source Labels:** Armament, Kind, SharkNode, WeaponKind  
  **Target Labels:** Armament, Family, SharkNode, WeaponFamily  

- (Missile)-[Family]->(Guided Missile)  
  **Source Labels:** Armament, Kind, SharkNode, WeaponKind  
  **Target Labels:** Armament, Family, SharkNode, WeaponFamily  

- (Missile)-[Family]->(Unguided Missile)  
  **Source Labels:** Armament, Kind, SharkNode, WeaponKind  
  **Target Labels:** Armament, Family, SharkNode, WeaponFamily  

- (National)-[Nation]->(Country)  (count: 204)  
  **Source Labels:** Kind, OrgKind, People, SharkNode  
  **Target Labels:** Country, Location, Object, People, SharkNode  

- (Naval)-[Family]->(Industrial - Naval)  
  **Source Labels:** Kind, SeaVessel, SharkNode, ShipKind  
  **Target Labels:** Family, SeaVessel, SharkNode, ShipFamily  

- (Naval)-[Family]->(Naval Cargo)  
  **Source Labels:** Kind, SeaVessel, SharkNode, ShipKind  
  **Target Labels:** Family, SeaVessel, SharkNode, ShipFamily  

- (Naval)-[Family]->(Passenger Ships)  
  **Source Labels:** Kind, SeaVessel, SharkNode, ShipKind  
  **Target Labels:** Family, SeaVessel, SharkNode, ShipFamily  

- (Naval)-[Family]->(Small Craft)  
  **Source Labels:** Kind, SeaVessel, SharkNode, ShipKind  
  **Target Labels:** Family, SeaVessel, SharkNode, ShipFamily  

- (Naval)-[Family]->(Special Purpose Craft)  
  **Source Labels:** Kind, SeaVessel, SharkNode, ShipKind  
  **Target Labels:** Family, SeaVessel, SharkNode, ShipFamily  

- (Naval)-[Family]->(Support Ships)  
  **Source Labels:** Kind, SeaVessel, SharkNode, ShipKind  
  **Target Labels:** Family, SeaVessel, SharkNode, ShipFamily  

- (Naval)-[Family]->(Warships)  
  **Source Labels:** Kind, SeaVessel, SharkNode, ShipKind  
  **Target Labels:** Family, SeaVessel, SharkNode, ShipFamily  

- (Projectile)-[Family]->(Ammunition)  
  **Source Labels:** Armament, Kind, SharkNode, WeaponKind  
  **Target Labels:** Armament, Family, SharkNode, WeaponFamily  

- (Torpedo)-[Family]->(Guided Torpedo)  
  **Source Labels:** Armament, Kind, SharkNode, WeaponKind  
  **Target Labels:** Armament, Family, SharkNode, WeaponFamily  

- (Unmanned)-[Family]->(Fixed Wing UAV)  
  **Source Labels:** AirKind, AirVehicle, Kind, SharkNode  
  **Target Labels:** AirFamily, AirVehicle, Family, SharkNode  

- (Unmanned)-[Family]->(Rotary UAV)  
  **Source Labels:** AirKind, AirVehicle, Kind, SharkNode  
  **Target Labels:** AirFamily, AirVehicle, Family, SharkNode  

