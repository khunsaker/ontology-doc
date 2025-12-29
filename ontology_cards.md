\newpage

# Hub Level

## Labels
- **Grouping:** Hub, SharkNode

## Nodes (Shark_Name)
- Shark2

## Properties
- `Classification` (unknown, optional)
- `Shark_Name` (string, required)
- `Shark_UUID` (unknown, optional)

## Relationships

### Outgoing
- (Shark2)-[Category]->(Aircraft)  
  **Source Labels:** Hub, SharkNode  
  **Target Labels:** AirVehicle, Category, SharkNode  

- (Shark2)-[Category]->(Organization)  
  **Source Labels:** Hub, SharkNode  
  **Target Labels:** Category, People, SharkNode  

- (Shark2)-[Category]->(Place)  
  **Source Labels:** Hub, SharkNode  
  **Target Labels:** Category, Location, SharkNode  

- (Shark2)-[Category]->(Ship)  
  **Source Labels:** Hub, SharkNode  
  **Target Labels:** Category, SeaVessel, SharkNode  

- (Shark2)-[Category]->(Weapon)  
  **Source Labels:** Hub, SharkNode  
  **Target Labels:** Armament, Category, SharkNode

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

\newpage

# Family Level

## Labels
- **Grouping:** AirFamily, AirVehicle, Armament, Family, SeaVessel, SharkNode, ShipFamily, WeaponFamily

## Nodes (Shark_Name)
- Ammunition
- Cluster Bomb
- Decoy
- Fixed Wing
- Fixed Wing UAV
- Guided Bomb
- Guided Missile
- Guided Torpedo
- Hybrid
- Industrial - Merchant
- Industrial - Naval
- Lighter Than Air
- Merchant Cargo
- Naval Cargo
- Nuclear Bomb
- Passenger Ships
- Rotary
- Rotary UAV
- Small Craft
- Special Purpose Craft
- Support Ships
- Unguided Bomb
- Unguided Missile
- Warships

## Properties
- `Classification` (unknown, optional)
- `Primary_Affiliation` (unknown, optional)
- `Shark_Name` (string, required)
- `Shark_UUID` (unknown, optional)
- `Status` (unknown, optional)

## Relationships

### Outgoing
- (Ammunition)-[Weapon_Type]->(Armament)  (count: 9)  
  **Source Labels:** Armament, Family, SharkNode, WeaponFamily  
  **Target Labels:** Armament, Object, SharkNode, WeaponType  

- (Cluster Bomb)-[Weapon_Type]->(Armament)  (count: 8)  
  **Source Labels:** Armament, Family, SharkNode, WeaponFamily  
  **Target Labels:** Armament, Object, SharkNode, WeaponType  

- (Decoy)-[Weapon_Type]->(Armament)  (count: 2)  
  **Source Labels:** Armament, Family, SharkNode, WeaponFamily  
  **Target Labels:** Armament, Object, SharkNode, WeaponType  

- (Fixed Wing)-[Derivative]->(AirType)  (count: 691)  
  **Source Labels:** AirFamily, AirVehicle, Family, SharkNode  
  **Target Labels:** AirSystem, AirType, AirVehicle, Object, SharkNode, System  

- (Fixed Wing UAV)-[Derivative]->(AirType)  (count: 169)  
  **Source Labels:** AirFamily, AirVehicle, Family, SharkNode  
  **Target Labels:** AirSystem, AirType, AirVehicle, Object, SharkNode, System  

- (Guided Bomb)-[Weapon_Type]->(Armament)  (count: 19)  
  **Source Labels:** Armament, Family, SharkNode, WeaponFamily  
  **Target Labels:** Armament, Object, PGM, SharkNode, WeaponType  

- (Guided Missile)-[Weapon_Type]->(Armament)  (count: 37)  
  **Source Labels:** Armament, Family, SharkNode, WeaponFamily  
  **Target Labels:** Armament, Object, SharkNode, WeaponType  

- (Guided Torpedo)-[Weapon_Type]->(Armament)  (count: 3)  
  **Source Labels:** Armament, Family, SharkNode, WeaponFamily  
  **Target Labels:** Armament, Object, SharkNode, WeaponType  

- (Hybrid)-[Derivative]->(AirType)  (count: 7)  
  **Source Labels:** AirFamily, AirVehicle, Family, SharkNode  
  **Target Labels:** AirSystem, AirType, AirVehicle, Object, SharkNode, System  

- (Industrial - Merchant)-[Ship_Type]->(ShipType)  (count: 7)  
  **Source Labels:** Family, SeaVessel, SharkNode, ShipFamily  
  **Target Labels:** Object, SeaVessel, SharkNode, ShipSystem, ShipType, System  

- (Industrial - Naval)-[Ship_Type]->(ShipType)  (count: 5)  
  **Source Labels:** Family, SeaVessel, SharkNode, ShipFamily  
  **Target Labels:** Object, SeaVessel, SharkNode, ShipSystem, ShipType, System  

- (Lighter Than Air)-[Derivative]->(AirType)  (count: 6)  
  **Source Labels:** AirFamily, AirVehicle, Family, SharkNode  
  **Target Labels:** AirSystem, AirType, AirVehicle, Object, SharkNode, System  

- (Merchant Cargo)-[Ship_Type]->(ShipType)  (count: 12)  
  **Source Labels:** Family, SeaVessel, SharkNode, ShipFamily  
  **Target Labels:** Object, SeaVessel, SharkNode, ShipSystem, ShipType, System  

- (Naval Cargo)-[Ship_Type]->(ShipType)  (count: 11)  
  **Source Labels:** Family, SeaVessel, SharkNode, ShipFamily  
  **Target Labels:** Object, SeaVessel, SharkNode, ShipSystem, ShipType, System  

- (Nuclear Bomb)-[Weapon_Type]->(Armament)  (count: 2)  
  **Source Labels:** Armament, Family, SharkNode, WeaponFamily  
  **Target Labels:** Armament, Object, SharkNode, WeaponType  

- (Passenger Ships)-[Ship_Type]->(ShipType)  (count: 5)  
  **Source Labels:** Family, SeaVessel, SharkNode, ShipFamily  
  **Target Labels:** Object, SeaVessel, SharkNode, ShipSystem, ShipType, System  

- (Rotary)-[Derivative]->(AirType)  (count: 93)  
  **Source Labels:** AirFamily, AirVehicle, Family, SharkNode  
  **Target Labels:** AirSystem, AirType, AirVehicle, Object, SharkNode, System  

- (Rotary UAV)-[Derivative]->(AirType)  (count: 59)  
  **Source Labels:** AirFamily, AirVehicle, Family, SharkNode  
  **Target Labels:** AirSystem, AirType, AirVehicle, Object, SharkNode, System  

- (Small Craft)-[Ship_Type]->(ShipType)  (count: 18)  
  **Source Labels:** Family, SeaVessel, SharkNode, ShipFamily  
  **Target Labels:** Object, SeaVessel, SharkNode, ShipSystem, ShipType, System  

- (Special Purpose Craft)-[Ship_Type]->(ShipType)  (count: 11)  
  **Source Labels:** Family, SeaVessel, SharkNode, ShipFamily  
  **Target Labels:** Object, SeaVessel, SharkNode, ShipSystem, ShipType, System  

- (Support Ships)-[Ship_Type]->(ShipType)  (count: 22)  
  **Source Labels:** Family, SeaVessel, SharkNode, ShipFamily  
  **Target Labels:** Object, SeaVessel, SharkNode, ShipSystem, ShipType, System  

- (Unguided Bomb)-[Weapon_Type]->(Armament)  (count: 11)  
  **Source Labels:** Armament, Family, SharkNode, WeaponFamily  
  **Target Labels:** Armament, Object, SharkNode, WeaponType  

- (Unguided Missile)-[Weapon_Type]->(Armament)  (count: 2)  
  **Source Labels:** Armament, Family, SharkNode, WeaponFamily  
  **Target Labels:** Armament, Object, SharkNode, WeaponType  

- (Warships)-[Ship_Type]->(ShipType)  (count: 13)  
  **Source Labels:** Family, SeaVessel, SharkNode, ShipFamily  
  **Target Labels:** Object, SeaVessel, SharkNode, ShipSystem, ShipType, System

\newpage

# AirType Level

## Labels
- **Grouping:** AirSystem, AirType, AirVehicle, Object, SharkNode, System


## Properties
- `Aircraft_Code` (unknown, optional)
- `Approach_Cat` (unknown, optional)
- `Approach_Speed` (unknown, optional)
- `BLOS` (unknown, optional)
- `Classification` (unknown, optional)
- `Climb_Mach` (unknown, optional)
- `Climb_Rate` (unknown, optional)
- `Climb_Speed` (unknown, optional)
- `Cruise_Mach` (unknown, optional)
- `Cruise_Speed` (unknown, optional)
- `Empty_Weight` (unknown, optional)
- `Endurance` (unknown, optional)
- `Engines` (unknown, optional)
- `Height` (unknown, optional)
- `ICAO_Acft_Cat` (unknown, optional)
- `ICAO_Acft_Code` (unknown, optional)
- `Initial_Approach_Speed` (unknown, optional)
- `Landing_Dist` (unknown, optional)
- `Landing_Field_Length` (unknown, optional)
- `Landing_Run` (unknown, optional)
- `Landing_Speed` (unknown, optional)
- `Length` (unknown, optional)
- `Link` (unknown, optional)
- `Link_EuroC` (unknown, optional)
- `MTOW` (unknown, optional)
- `Max_Payload` (unknown, optional)
- `Max_Range` (unknown, optional)
- `Max_Speed` (unknown, optional)
- `NATO_Name` (unknown, optional)
- `Nickname` (unknown, optional)
- `Power` (unknown, optional)
- `Primary_Affiliation` (unknown, optional)
- `Primary_Platform` (unknown, optional)
- `Radius` (unknown, optional)
- `Range` (unknown, optional)
- `Secondary_Affiliation` (unknown, optional)
- `Secondary_Platform` (unknown, optional)
- `Service_Ceiling` (unknown, optional)
- `Shark_Name` (string, required)
- `Shark_UUID` (unknown, optional)
- `Stall_Speed` (unknown, optional)
- `Status` (unknown, optional)
- `TO_Field_Length` (unknown, optional)
- `TO_Run` (unknown, optional)
- `TO_Speed` (unknown, optional)
- `Tertiary_Affiliation` (unknown, optional)
- `Tertiary_Platform` (unknown, optional)
- `Wake_Turbulence_Cat` (unknown, optional)
- `Wing_Area` (unknown, optional)
- `Wing_Span` (unknown, optional)

## Relationships

### Outgoing
- (AirType)-[Derivative]->(AirSubType)  (count: 1407)  
  **Source Labels:** AirSystem, AirType, AirVehicle, Object, SharkNode, System  
  **Target Labels:** AirSubType, AirSystem, AirVehicle, Object, SharkNode, System  

- (AirType)-[Employs]->(Armament)  (count: 112)  
  **Source Labels:** AirSystem, AirType, AirVehicle, Object, SharkNode, System  
  **Target Labels:** Armament, Object, PGM, SharkNode, WeaponType  

- (AirType)-[Made_by]->(ArmedForces)  
  **Source Labels:** AirSystem, AirType, AirVehicle, Object, SharkNode, System  
  **Target Labels:** ArmedForces, Manufacturer, Object, People, SharkNode  

- (AirType)-[Made_by]->(Company)  (count: 1030)  
  **Source Labels:** AirSystem, AirType, AirVehicle, Object, SharkNode, System  
  **Target Labels:** Company, Manufacturer, Object, People, SharkNode  

- (AirType)-[Made_by]->(Manufacturer)  (count: 60)  
  **Source Labels:** AirSystem, AirType, AirVehicle, Object, SharkNode, System  
  **Target Labels:** Manufacturer, Object, People, SharkNode, Subsidiary  

- (AirType)-[Used_by]->(ArmedForces)  (count: 1988)  
  **Source Labels:** AirSystem, AirType, AirVehicle, Object, SharkNode, System  
  **Target Labels:** ArmedForces, Object, People, SharkNode  

- (AirType)-[Used_by]->(Civilians)  (count: 351)  
  **Source Labels:** AirSystem, AirType, AirVehicle, Object, SharkNode, System  
  **Target Labels:** Civilians, People, SharkNode  

- (AirType)-[Used_by]->(Government)  (count: 214)  
  **Source Labels:** AirSystem, AirType, AirVehicle, Object, SharkNode, System  
  **Target Labels:** Government, People, SharkNode  

- (AirType)-[Used_by]->(Object)  (count: 12)  
  **Source Labels:** AirSystem, AirType, AirVehicle, Object, SharkNode, System  
  **Target Labels:** Object, People, Service, SharkNode

\newpage

# AirSubType Level

## Labels
- **Grouping:** AirSubType, AirSystem, AirVehicle, Object, SharkNode, System


## Properties
- `Aircraft_Code` (unknown, optional)
- `Approach_Cat` (unknown, optional)
- `Approach_Speed` (unknown, optional)
- `BLOS` (unknown, optional)
- `Classification` (unknown, optional)
- `Climb_Mach` (unknown, optional)
- `Climb_Rate` (unknown, optional)
- `Climb_Speed` (unknown, optional)
- `Cruise_Mach` (unknown, optional)
- `Cruise_Speed` (unknown, optional)
- `Empty_Weight` (unknown, optional)
- `Endurance` (unknown, optional)
- `Engines` (unknown, optional)
- `Height` (unknown, optional)
- `ICAO_Acft_Cat` (unknown, optional)
- `ICAO_Acft_Code` (unknown, optional)
- `Initial_Approach_Speed` (unknown, optional)
- `Landing_Dist` (unknown, optional)
- `Landing_Field_Length` (unknown, optional)
- `Landing_Run` (unknown, optional)
- `Landing_Speed` (unknown, optional)
- `Length` (unknown, optional)
- `Link_EuroC` (unknown, optional)
- `MTOW` (unknown, optional)
- `Max_Payload` (unknown, optional)
- `Max_Range` (unknown, optional)
- `Max_Speed` (unknown, optional)
- `NATO_Name` (unknown, optional)
- `Nickname` (unknown, optional)
- `Power` (unknown, optional)
- `Primary_Affiliation` (unknown, optional)
- `Primary_Platform` (unknown, optional)
- `Radius` (unknown, optional)
- `Range` (unknown, optional)
- `Secondary_Affiliation` (unknown, optional)
- `Secondary_Platform` (unknown, optional)
- `Service_Ceiling` (unknown, optional)
- `Shark_Name` (string, required)
- `Shark_UUID` (unknown, optional)
- `Stall_Speed` (unknown, optional)
- `Status` (unknown, optional)
- `TO_Field_Length` (unknown, optional)
- `TO_Run` (unknown, optional)
- `TO_Speed` (unknown, optional)
- `Tertiary_Affiliation` (unknown, optional)
- `Tertiary_Platform` (unknown, optional)
- `Wake_Turbulence_Cat` (unknown, optional)
- `Wing_Area` (unknown, optional)
- `Wing_Span` (unknown, optional)

## Relationships

### Outgoing
- (AirSubType)-[Derivative]->(AirVariant)  (count: 896)  
  **Source Labels:** AirSubType, AirSystem, AirVehicle, Object, SharkNode, System  
  **Target Labels:** AirSystem, AirVariant, AirVehicle, Object, SharkNode, System  

- (AirSubType)-[Employs]->(Armament)  (count: 227)  
  **Source Labels:** AirSubType, AirSystem, AirVehicle, Object, SharkNode, System  
  **Target Labels:** Armament, Object, SharkNode, WeaponType  

- (AirSubType)-[Made_by]->(Company)  (count: 1427)  
  **Source Labels:** AirSubType, AirSystem, AirVehicle, Object, SharkNode, System  
  **Target Labels:** Company, Manufacturer, Object, People, SharkNode  

- (AirSubType)-[Made_by]->(Manufacturer)  (count: 89)  
  **Source Labels:** AirSubType, AirSystem, AirVehicle, Object, SharkNode, System  
  **Target Labels:** Manufacturer, Object, People, SharkNode, Subsidiary  

- (AirSubType)-[Used_by]->(ArmedForces)  (count: 2511)  
  **Source Labels:** AirSubType, AirSystem, AirVehicle, Object, SharkNode, System  
  **Target Labels:** ArmedForces, Object, People, SharkNode  

- (AirSubType)-[Used_by]->(Civilians)  (count: 377)  
  **Source Labels:** AirSubType, AirSystem, AirVehicle, Object, SharkNode, System  
  **Target Labels:** Civilians, People, SharkNode  

- (AirSubType)-[Used_by]->(Command)  (count: 2)  
  **Source Labels:** AirSubType, AirSystem, AirVehicle, Object, SharkNode, System  
  **Target Labels:** Command, Object, People, SharkNode  

- (AirSubType)-[Used_by]->(Government)  (count: 435)  
  **Source Labels:** AirSubType, AirSystem, AirVehicle, Object, SharkNode, System  
  **Target Labels:** Government, People, SharkNode  

- (AirSubType)-[Used_by]->(Object)  (count: 57)  
  **Source Labels:** AirSubType, AirSystem, AirVehicle, Object, SharkNode, System  
  **Target Labels:** Object, People, Service, SharkNode

\newpage

# AirVariant Level

## Labels
- **Grouping:** AirSystem, AirVariant, AirVehicle, Object, SharkNode, System


## Properties
- `Aircraft_Code` (unknown, optional)
- `Approach_Cat` (unknown, optional)
- `Approach_Speed` (unknown, optional)
- `BLOS` (unknown, optional)
- `Classification` (unknown, optional)
- `Climb_Mach` (unknown, optional)
- `Climb_Rate` (unknown, optional)
- `Climb_Speed` (unknown, optional)
- `Cruise_Mach` (unknown, optional)
- `Cruise_Speed` (unknown, optional)
- `Empty_Weight` (unknown, optional)
- `Endurance` (unknown, optional)
- `Engines` (unknown, optional)
- `Height` (unknown, optional)
- `ICAO_Acft_Cat` (unknown, optional)
- `ICAO_Acft_Code` (unknown, optional)
- `Initial_Approach_Speed` (unknown, optional)
- `Landing_Dist` (unknown, optional)
- `Landing_Field_Length` (unknown, optional)
- `Landing_Run` (unknown, optional)
- `Landing_Speed` (unknown, optional)
- `Length` (unknown, optional)
- `Link_EuroC` (unknown, optional)
- `MTOW` (unknown, optional)
- `Max_Payload` (unknown, optional)
- `Max_Range` (unknown, optional)
- `Max_Speed` (unknown, optional)
- `NATO_Name` (unknown, optional)
- `Nickname` (unknown, optional)
- `Power` (unknown, optional)
- `Primary_Affiliation` (unknown, optional)
- `Primary_Platform` (unknown, optional)
- `Radius` (unknown, optional)
- `Range` (unknown, optional)
- `Secondary_Affiliation` (unknown, optional)
- `Secondary_Platform` (unknown, optional)
- `Service_Ceiling` (unknown, optional)
- `Shark_Name` (string, required)
- `Shark_UUID` (unknown, optional)
- `Stall_Speed` (unknown, optional)
- `Status` (unknown, optional)
- `TO_Field_Length` (unknown, optional)
- `TO_Run` (unknown, optional)
- `TO_Speed` (unknown, optional)
- `Tertiary_Affiliation` (unknown, optional)
- `Tertiary_Platform` (unknown, optional)
- `Wake_Turbulence_Cat` (unknown, optional)
- `Wing_Area` (unknown, optional)
- `Wing_Span` (unknown, optional)

## Relationships

### Outgoing
- (AirVariant)-[Derivative]->(AirSubType)  
  **Source Labels:** AirSystem, AirVariant, AirVehicle, Object, SharkNode, System  
  **Target Labels:** AirSubType, AirSystem, AirVehicle, Object, SharkNode, System  

- (AirVariant)-[Derivative]->(AirSubVariant)  (count: 323)  
  **Source Labels:** AirSystem, AirVariant, AirVehicle, Object, SharkNode, System  
  **Target Labels:** AirSubVariant, AirSystem, AirVehicle, Object, SharkNode, System  

- (AirVariant)-[Employs]->(Armament)  (count: 16)  
  **Source Labels:** AirSystem, AirVariant, AirVehicle, Object, SharkNode, System  
  **Target Labels:** Armament, Object, PGM, SharkNode, WeaponType  

- (AirVariant)-[Instance]->(AirInstance)  (count: 844)  
  **Source Labels:** AirSystem, AirVariant, AirVehicle, Object, SharkNode, System  
  **Target Labels:** AirInstance, InstanceNode, Object, SharkNode  

- (AirVariant)-[Made_by]->(Company)  (count: 922)  
  **Source Labels:** AirSystem, AirVariant, AirVehicle, Object, SharkNode, System  
  **Target Labels:** Company, Manufacturer, Object, People, SharkNode  

- (AirVariant)-[Made_by]->(Manufacturer)  (count: 71)  
  **Source Labels:** AirSystem, AirVariant, AirVehicle, Object, SharkNode, System  
  **Target Labels:** Manufacturer, Object, People, SharkNode, Subsidiary  

- (AirVariant)-[Used_by]->(ArmedForces)  (count: 993)  
  **Source Labels:** AirSystem, AirVariant, AirVehicle, Object, SharkNode, System  
  **Target Labels:** ArmedForces, Object, People, SharkNode  

- (AirVariant)-[Used_by]->(Civilians)  (count: 74)  
  **Source Labels:** AirSystem, AirVariant, AirVehicle, Object, SharkNode, System  
  **Target Labels:** Civilians, People, SharkNode  

- (AirVariant)-[Used_by]->(Command)  
  **Source Labels:** AirSystem, AirVariant, AirVehicle, Object, SharkNode, System  
  **Target Labels:** Command, Object, People, SharkNode  

- (AirVariant)-[Used_by]->(Government)  (count: 113)  
  **Source Labels:** AirSystem, AirVariant, AirVehicle, Object, SharkNode, System  
  **Target Labels:** Government, People, SharkNode  

- (AirVariant)-[Used_by]->(Object)  (count: 74)  
  **Source Labels:** AirSystem, AirVariant, AirVehicle, Object, SharkNode, System  
  **Target Labels:** Object, People, Service, SharkNode

\newpage

# AirSubVariant Level

## Labels
- **Grouping:** AirSubVariant, AirSystem, AirVehicle, Object, SharkNode, System


## Properties
- `Aircraft_Code` (unknown, optional)
- `Approach_Cat` (unknown, optional)
- `Approach_Speed` (unknown, optional)
- `Classification` (unknown, optional)
- `Climb_Mach` (unknown, optional)
- `Climb_Rate` (unknown, optional)
- `Climb_Speed` (unknown, optional)
- `Cruise_Mach` (unknown, optional)
- `Cruise_Speed` (unknown, optional)
- `Empty_Weight` (unknown, optional)
- `Endurance` (unknown, optional)
- `Engines` (unknown, optional)
- `Height` (unknown, optional)
- `ICAO_Acft_Cat` (unknown, optional)
- `ICAO_Acft_Code` (unknown, optional)
- `Initial_Approach_Speed` (unknown, optional)
- `Landing_Dist` (unknown, optional)
- `Landing_Field_Length` (unknown, optional)
- `Landing_Run` (unknown, optional)
- `Landing_Speed` (unknown, optional)
- `Length` (unknown, optional)
- `Link_EuroC` (unknown, optional)
- `MTOW` (unknown, optional)
- `Max_Payload` (unknown, optional)
- `Max_Range` (unknown, optional)
- `Max_Speed` (unknown, optional)
- `NATO_Name` (unknown, optional)
- `Nickname` (unknown, optional)
- `Power` (unknown, optional)
- `Primary_Affiliation` (unknown, optional)
- `Primary_Platform` (unknown, optional)
- `Radius` (unknown, optional)
- `Range` (unknown, optional)
- `Secondary_Affiliation` (unknown, optional)
- `Secondary_Platform` (unknown, optional)
- `Service_Ceiling` (unknown, optional)
- `Shark_Name` (string, required)
- `Shark_UUID` (unknown, optional)
- `Stall_Speed` (unknown, optional)
- `Status` (unknown, optional)
- `Super_Type` (unknown, optional)
- `TO_Field_Length` (unknown, optional)
- `TO_Run` (unknown, optional)
- `TO_Speed` (unknown, optional)
- `Wake_Turbulence_Cat` (unknown, optional)
- `Wing_Area` (unknown, optional)
- `Wing_Span` (unknown, optional)

## Relationships

### Outgoing
- (AirSubVariant)-[Derivative]->(AirModel)  (count: 83)  
  **Source Labels:** AirSubVariant, AirSystem, AirVehicle, Object, SharkNode, System  
  **Target Labels:** AirModel, AirSystem, AirVehicle, Object, SharkNode, System  

- (AirSubVariant)-[Employs]->(Armament)  (count: 2)  
  **Source Labels:** AirSubVariant, AirSystem, AirVehicle, Object, SharkNode, System  
  **Target Labels:** Armament, Object, PGM, SharkNode, WeaponVariant  

- (AirSubVariant)-[Instance]->(AirInstance)  (count: 103)  
  **Source Labels:** AirSubVariant, AirSystem, AirVehicle, Object, SharkNode, System  
  **Target Labels:** AirInstance, InstanceNode, Object, SharkNode  

- (AirSubVariant)-[Made_by]->(Company)  (count: 304)  
  **Source Labels:** AirSubVariant, AirSystem, AirVehicle, Object, SharkNode, System  
  **Target Labels:** Company, Manufacturer, Object, People, SharkNode  

- (AirSubVariant)-[Made_by]->(Manufacturer)  (count: 23)  
  **Source Labels:** AirSubVariant, AirSystem, AirVehicle, Object, SharkNode, System  
  **Target Labels:** Manufacturer, Object, People, SharkNode, Subsidiary  

- (AirSubVariant)-[Used_by]->(ArmedForces)  (count: 199)  
  **Source Labels:** AirSubVariant, AirSystem, AirVehicle, Object, SharkNode, System  
  **Target Labels:** ArmedForces, Object, People, SharkNode  

- (AirSubVariant)-[Used_by]->(Civilians)  (count: 9)  
  **Source Labels:** AirSubVariant, AirSystem, AirVehicle, Object, SharkNode, System  
  **Target Labels:** Civilians, People, SharkNode  

- (AirSubVariant)-[Used_by]->(Government)  (count: 7)  
  **Source Labels:** AirSubVariant, AirSystem, AirVehicle, Object, SharkNode, System  
  **Target Labels:** Government, People, SharkNode  

- (AirSubVariant)-[Used_by]->(Object)  (count: 34)  
  **Source Labels:** AirSubVariant, AirSystem, AirVehicle, Object, SharkNode, System  
  **Target Labels:** Object, People, Service, SharkNode

\newpage

# AirModel Level

## Labels
- **Grouping:** AirModel, AirSystem, AirVehicle, Object, SharkNode, System


## Properties
- `Aircraft_Code` (unknown, optional)
- `Approach_Cat` (unknown, optional)
- `Approach_Speed` (unknown, optional)
- `Classification` (unknown, optional)
- `Climb_Mach` (unknown, optional)
- `Climb_Rate` (unknown, optional)
- `Climb_Speed` (unknown, optional)
- `Cruise_Mach` (unknown, optional)
- `Cruise_Speed` (unknown, optional)
- `Empty_Weight` (unknown, optional)
- `Endurance` (unknown, optional)
- `Engines` (unknown, optional)
- `Height` (unknown, optional)
- `ICAO_Acft_Cat` (unknown, optional)
- `ICAO_Acft_Code` (unknown, optional)
- `Initial_Approach_Speed` (unknown, optional)
- `Landing_Dist` (unknown, optional)
- `Landing_Field_Length` (unknown, optional)
- `Landing_Run` (unknown, optional)
- `Landing_Speed` (unknown, optional)
- `Length` (unknown, optional)
- `Link_EuroC` (unknown, optional)
- `MTOW` (unknown, optional)
- `Max_Payload` (unknown, optional)
- `Max_Range` (unknown, optional)
- `Max_Speed` (unknown, optional)
- `NATO_Name` (unknown, optional)
- `Nickname` (unknown, optional)
- `Power` (unknown, optional)
- `Primary_Affiliation` (unknown, optional)
- `Primary_Platform` (unknown, optional)
- `Radius` (unknown, optional)
- `Range` (unknown, optional)
- `Secondary_Affiliation` (unknown, optional)
- `Secondary_Platform` (unknown, optional)
- `Service_Ceiling` (unknown, optional)
- `Shark_Name` (string, required)
- `Shark_UUID` (unknown, optional)
- `Stall_Speed` (unknown, optional)
- `Status` (unknown, optional)
- `Super_Type` (unknown, optional)
- `TO_Field_Length` (unknown, optional)
- `TO_Run` (unknown, optional)
- `TO_Speed` (unknown, optional)
- `Wake_Turbulence_Cat` (unknown, optional)
- `Wing_Area` (unknown, optional)
- `Wing_Span` (unknown, optional)

## Relationships

### Outgoing
- (AirModel)-[Derivative]->(AirSubModel)  (count: 12)  
  **Source Labels:** AirModel, AirSystem, AirVehicle, Object, SharkNode, System  
  **Target Labels:** AirSubModel, AirSystem, AirVehicle, Object, SharkNode, System  

- (AirModel)-[Made_by]->(Company)  (count: 69)  
  **Source Labels:** AirModel, AirSystem, AirVehicle, Object, SharkNode, System  
  **Target Labels:** Company, Manufacturer, Object, People, SharkNode  

- (AirModel)-[Made_by]->(Manufacturer)  (count: 4)  
  **Source Labels:** AirModel, AirSystem, AirVehicle, Object, SharkNode, System  
  **Target Labels:** Manufacturer, Object, People, SharkNode, Subsidiary  

- (AirModel)-[Used_by]->(ArmedForces)  (count: 65)  
  **Source Labels:** AirModel, AirSystem, AirVehicle, Object, SharkNode, System  
  **Target Labels:** ArmedForces, Object, People, SharkNode  

- (AirModel)-[Used_by]->(Civilians)  
  **Source Labels:** AirModel, AirSystem, AirVehicle, Object, SharkNode, System  
  **Target Labels:** Civilians, People, SharkNode  

- (AirModel)-[Used_by]->(Government)  (count: 4)  
  **Source Labels:** AirModel, AirSystem, AirVehicle, Object, SharkNode, System  
  **Target Labels:** Government, People, SharkNode  

- (AirModel)-[Used_by]->(Object)  (count: 19)  
  **Source Labels:** AirModel, AirSystem, AirVehicle, Object, SharkNode, System  
  **Target Labels:** Object, People, Service, SharkNode

\newpage

# AirSubModel Level

## Labels
- **Grouping:** AirSubModel, AirSystem, AirVehicle, Object, SharkNode, System


## Properties
- `Aircraft_Code` (unknown, optional)
- `Approach_Cat` (unknown, optional)
- `Classification` (unknown, optional)
- `Climb_Rate` (unknown, optional)
- `Climb_Speed` (unknown, optional)
- `Cruise_Speed` (unknown, optional)
- `Engines` (unknown, optional)
- `Height` (unknown, optional)
- `ICAO_Acft_Cat` (unknown, optional)
- `ICAO_Acft_Code` (unknown, optional)
- `Initial_Approach_Speed` (unknown, optional)
- `Landing_Dist` (unknown, optional)
- `Landing_Field_Length` (unknown, optional)
- `Landing_Run` (unknown, optional)
- `Landing_Speed` (unknown, optional)
- `Length` (unknown, optional)
- `Link_EuroC` (unknown, optional)
- `MTOW` (unknown, optional)
- `Max_Payload` (unknown, optional)
- `Max_Range` (unknown, optional)
- `Max_Speed` (unknown, optional)
- `NATO_Name` (unknown, optional)
- `Nickname` (unknown, optional)
- `Power` (unknown, optional)
- `Primary_Affiliation` (unknown, optional)
- `Primary_Platform` (unknown, optional)
- `Radius` (unknown, optional)
- `Range` (unknown, optional)
- `Service_Ceiling` (unknown, optional)
- `Shark_Name` (string, required)
- `Shark_UUID` (unknown, optional)
- `Stall_Speed` (unknown, optional)
- `Status` (unknown, optional)
- `Super_Type` (unknown, optional)
- `TO_Field_Length` (unknown, optional)
- `TO_Run` (unknown, optional)
- `TO_Speed` (unknown, optional)
- `Wake_Turbulence_Cat` (unknown, optional)
- `Wing_Area` (unknown, optional)
- `Wing_Span` (unknown, optional)

## Relationships

### Outgoing
- (AirSubModel)-[Employs]->(Armament)  
  **Source Labels:** AirSubModel, AirSystem, AirVehicle, Object, SharkNode, System  
  **Target Labels:** Armament, Object, PGM, SharkNode, WeaponSubType  

- (AirSubModel)-[Made_by]->(Company)  (count: 13)  
  **Source Labels:** AirSubModel, AirSystem, AirVehicle, Object, SharkNode, System  
  **Target Labels:** Company, Manufacturer, Object, People, SharkNode  

- (AirSubModel)-[Used_by]->(ArmedForces)  (count: 12)  
  **Source Labels:** AirSubModel, AirSystem, AirVehicle, Object, SharkNode, System  
  **Target Labels:** ArmedForces, Object, People, SharkNode  

- (AirSubModel)-[Used_by]->(Object)  (count: 2)  
  **Source Labels:** AirSubModel, AirSystem, AirVehicle, Object, SharkNode, System  
  **Target Labels:** Object, People, Service, SharkNode

\newpage

# AirInstance Level

## Labels
- **Grouping:** AirInstance, InstanceNode, Object, SharkNode


## Properties
- `Air_System` (unknown, optional)
- `Mode_S` (unknown, optional)
- `Nationality` (unknown, optional)
- `Operator` (unknown, optional)
- `Registration` (unknown, optional)
- `Shark_Name` (string, required)
- `Shark_UUID` (unknown, optional)
- `Side_Number` (unknown, optional)
- `Status` (unknown, optional)
- `Tail_Number` (unknown, optional)

## Relationships

### Outgoing
- (none)

\newpage

# ShipType Level

## Labels
- **Grouping:** Object, SeaVessel, SharkNode, ShipSystem, ShipType, System


## Properties
- `Classification` (unknown, optional)
- `Default_Affiliation` (unknown, optional)
- `Shark_Name` (string, required)
- `Shark_UUID` (unknown, optional)

## Relationships

### Outgoing
- (ShipType)-[Instance]->(ShipInstance)  (count: 2)  
  **Source Labels:** Object, SeaVessel, SharkNode, ShipSystem, ShipType, System  
  **Target Labels:** InstanceNode, Object, SeaVessel, SharkNode, ShipInstance  

- (ShipType)-[Ship_Sub_Type]->(ShipSubType)  (count: 60)  
  **Source Labels:** Object, SeaVessel, SharkNode, ShipSystem, ShipType, System  
  **Target Labels:** Object, SeaVessel, SharkNode, ShipSubType, ShipSystem, System

\newpage

# ShipSubType Level

## Labels
- **Grouping:** Object, SeaVessel, SharkNode, ShipSubType, ShipSystem, System


## Properties
- `Classification` (unknown, optional)
- `Default_Affiliation` (unknown, optional)
- `Shark_Name` (string, required)
- `Shark_UUID` (unknown, optional)

## Relationships

### Outgoing
- (ShipSubType)-[Class]->(ShipClass)  (count: 168)  
  **Source Labels:** Object, SeaVessel, SharkNode, ShipSubType, ShipSystem, System  
  **Target Labels:** Object, SeaVessel, SharkNode, ShipClass, ShipSystem, System  

- (ShipSubType)-[Instance]->(ShipInstance)  (count: 18)  
  **Source Labels:** Object, SeaVessel, SharkNode, ShipSubType, ShipSystem, System  
  **Target Labels:** InstanceNode, MunitionsStorage, Object, SeaVessel, SharkNode, ShipInstance

\newpage

# ShipClass Level

## Labels
- **Grouping:** Object, SeaVessel, SharkNode, ShipClass, ShipSystem, System


## Properties
- `Classification` (unknown, optional)
- `Default_Affiliation` (unknown, optional)
- `Shark_Name` (string, required)
- `Shark_UUID` (unknown, optional)
- `Ship_Sub_Type` (unknown, optional)
- `Ship_Type` (unknown, optional)

## Relationships

### Outgoing
- (ShipClass)-[Employs]->(Armament)  (count: 43)  
  **Source Labels:** Object, SeaVessel, SharkNode, ShipClass, ShipSystem, System  
  **Target Labels:** Armament, Object, SharkNode, WeaponType  

- (ShipClass)-[Instance]->(ShipInstance)  (count: 240)  
  **Source Labels:** Object, SeaVessel, SharkNode, ShipClass, ShipSystem, System  
  **Target Labels:** InstanceNode, Object, SeaVessel, SharkNode, ShipInstance  

- (ShipClass)-[Sub_Class]->(ShipSubClass)  (count: 37)  
  **Source Labels:** Object, SeaVessel, SharkNode, ShipClass, ShipSystem, System  
  **Target Labels:** Object, SeaVessel, SharkNode, ShipSubClass, ShipSystem, System

\newpage

# ShipSubClass Level

## Labels
- **Grouping:** Object, SeaVessel, SharkNode, ShipSubClass, ShipSystem, System


## Properties
- `Classification` (unknown, optional)
- `Default_Affiliation` (unknown, optional)
- `Shark_Name` (string, required)
- `Shark_UUID` (unknown, optional)
- `Ship_Sub_Type` (unknown, optional)
- `Ship_Type` (unknown, optional)

## Relationships

### Outgoing
- (ShipSubClass)-[Instance]->(ShipInstance)  (count: 199)  
  **Source Labels:** Object, SeaVessel, SharkNode, ShipSubClass, ShipSystem, System  
  **Target Labels:** InstanceNode, Object, SeaVessel, SharkNode, ShipInstance

\newpage

# ShipInstance Level

## Labels
- **Grouping:** InstanceNode, MunitionsStorage, Object, SeaVessel, SharkNode, ShipInstance


## Properties
- `AMS_Name` (unknown, optional)
- `Affiliation` (unknown, optional)
- `Allegiance` (unknown, optional)
- `Callsign` (unknown, optional)
- `Class` (unknown, optional)
- `Classification` (unknown, optional)
- `Flag` (unknown, optional)
- `Home_Port` (unknown, optional)
- `IMO_Number` (unknown, optional)
- `MMSI` (unknown, optional)
- `Operator` (unknown, optional)
- `Pennant` (unknown, optional)
- `SCONUM` (unknown, optional)
- `Shark_Name` (string, required)
- `Shark_UUID` (unknown, optional)
- `Ship_Sub_Type` (unknown, optional)
- `Ship_Type` (unknown, optional)
- `Status` (unknown, optional)
- `Sub_Class` (unknown, optional)

## Relationships

### Outgoing
- (none)

