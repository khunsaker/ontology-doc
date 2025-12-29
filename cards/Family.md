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

