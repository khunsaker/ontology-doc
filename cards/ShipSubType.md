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

