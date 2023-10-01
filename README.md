# auto-bartender
Automatic Bartender system User Interface and database configurations

User Interface Module:
Classes to create and maintain the Graphical User Interface for the Auto Bartender. 
Divided into three base classes, the first of which is the Main Application which is the main driver of the customtkinter application object.
The Options Frame Class inherits from the customtkinter Frame class to establish and operate the choice/ option screens (Such as the category and specific drink).
The Modification Frame inherits from the customtkinter Frame class and leverages another custom Spin Box class to create the modification screen availible when a drink is selected.

Flow of operations:
  Main Application fires up with "Home" Options Frame present on start up. As the name suggests, the Home screen is the center of all UI operations and will be presented after every order event is processed. From the home screen, a category may be selected which will provide options for each items in the category. THe secondary option frames leverage the same Option Frame class as the Home options Frame with some configuration differences upon initialization.
* Required Modules:
  - customtkinter
  - Some Database access module

Data Storage Module:

Data Importer Module:

AutoBartender Module:

Arduino Interface Module:
    
