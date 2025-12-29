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

