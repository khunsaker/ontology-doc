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

