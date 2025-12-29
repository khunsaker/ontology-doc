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

