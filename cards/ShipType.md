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

