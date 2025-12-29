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

