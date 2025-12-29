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

