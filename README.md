# auto-bartender

## User Interface Module:
### Overview:
  The User Interface module contains the various classes used to create and maintain the Graphical User Interface for the Auto Bartender. 
Leveraging three main structures, the first of which being the Main Application which is inherited from the customtkinter application object.
Secondly, there is the Options Frame class, inheriting from the customtkinter Frame class to establish and operate the choice/ option screens (Such as the category and specific drink).
Lastly, the Modification Frame class, also inheriting from the customtkinter Frame class, provides element modification through a custom Spin Box class creating the modification screen available when a drink is selected. The majority of the functionality is self-contained into the User Interface module, however, there is a small portion that will be externally setup and referenced through passed in callbacks. 

### Flow of operations:
  Main Application initialization entail basic setup of the overall application, including components such as the title frame, home and random buttons, as well as the window attributes. After the Main Application is created, the first member function to be run should be DisplayHomePage which as the name suggests, creates a "Home" Options Frame as the primary view. The Home Options Frame is the center of all UI operations and will be presented after every order event is processed. From the "Home Screen" (as it will also be referred to), a category may be selected which will invoke the passed in callback to continue the ordering process. The callback passed to the Home Options Frame should spin up the secondary option frames, leveraging the same Option Frame class as the Home options Frame, to provide a more granular selection (in the case the drinks). An external callback allows for additional operations to be invoked prior to the presentation of a secondary screen. Additionally, it is important to note that the User Interface module does not initially import all category data upon Main Application initialization, however, each Options Frame class instance is saved off after first use to decrease the time required to be re-presented. Where auto-bartender uses secondary Option Frames as the last point before order modification, the Main Application class is setup to support multiple tiers of Option screens.

  The Modification Frame is the final primary component to the User Interface module, providing a series of spin boxes (implemented as another inherited customtkinter Frame class) to enable modifications to specific components of a drink. Additionally, a "Back" and "Order" button are presented as means of canceling or proceeding with the order. There is a configurable number of spin boxes to present at a time and scroll arrows will appear in the event the total number of modification spin boxes exceeds the display limit. Furthermore, an indicator of the number of modification options available, in addition to the total measurement of ingredients, are positioned at the bottom of the screen. A maximum measurement may be passed into the Modification Frame class to limit the overall limit that can be added to an order overall. The user also has an option to decrement any value down to zero (0) if desired. When the user is satisfied with their order, they may select the "Order" button positioned on the right side of the screen, invoking the order callback passed into the Main Application upon initialization. The callback is passed the Modification Frame instance itself for the callback function to poll/ extract the individual item information. If at any point the user wishes to return to the previous screen, the "Back" button on the left side may be selected. (Note, the order and back buttons are part of the Main Application rather than the Modification Frame).  
  
* Required Modules:
  - customtkinter
  - functools (partial specifically)

## Data Storage Module:

## Data Importer Module:
### Overview
Currently, the only format of data accepted is a csv file. The first line in the file is interpreted as the columns/ elements of a drink entry with each subsequent line pertaining to a single drink. These entries are loaded into a dictionary of dictionaries to support easy retrieval of individual elements. There should be only one instance of this class in terms of the auto-bartender as a whole, and the data is only imported upon initialization.
## AutoBartender Module:
### Overview: 
The main driver of the auto-bartender application, instantiating the User Interface modules to provide a GUI to the user as well as importing the drinks data, storing order information, and passing orders to the Arduino Interface Module. 
## Arduino Interface Module:
  
