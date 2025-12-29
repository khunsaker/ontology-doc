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

