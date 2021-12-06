#------------------------------------------#
# Title: Assignment08.py
# Desc: Assignment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# LWarner, 2021-Dec-05, added code and docstrings for functionality
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """
    #--Constructor--#
    def __init__(self, cd_id, cd_title, cd_artist):
        #--Attributes--#
        self.__cd_id = cd_id
        self.__cd_title = cd_title
        self.__cd_artist = cd_artist

    #--Properties--#
    
    @property    
    def cd_id(self):
        return self.__cd_id
    
    @cd_id.setter
    def cd_id(self, cd_id):
        if str(cd_id).isnumeric():
            return cd_id
        else:
            raise Exception ('ID must be a number!')
    
    @property
    def cd_title(self):
        return self.__cd_title
    
    @cd_title.setter
    def cd_title(self, cd_title):
        if str(cd_title).isnumeric():
            raise Exception('Title must be a string.')
        else:
            return cd_title
        
    @property
    def cd_artist(self):
        return self.__cd_artist
    
    @cd_artist.setter
    def cd_artist(self, cd_artist):
        if str(cd_artist).isnumeric():
            raise Exception('Artist must be a string.')
        else:
            return cd_artist
        
# -- PROCESSING -- #
class DataProcessor:
    """ Functions to add, delete, and save data in the table"""
  
    @staticmethod
    def add_row(objRow):
        """Function to append a row to the table
        Gathers the user input for ID, Title and Artist and appends it to the table in memory.

        Args:
            row: the row of ID, Title, and Artist
            table: the 2D data structure that holds the data during runtime

        Returns:
            Shows inventory
        """
        objRow["ID"] = int(objRow["ID"])
        lstOfCDObjects.append(objRow)
   
    @staticmethod   
    def delete_row(intRowNr, lstTbl):
        """ Function to delete a row from the table if the user wants. 
        
        Args:
            intRowNr: the ID number for the row to be deleted
            lstTbl: the table with the data
            
        Returns:
            The information showing whether or not the row was successfully deleted.
        """    
        intRowNr = -1
        blnCDRemoved = False
        for row in lstTbl:
           intRowNr += 1
           if row['ID'] == intIDDel:
               del lstTbl[intRowNr]
               blnCDRemoved = True
               break
           if blnCDRemoved:
               print('The CD was removed')
        else:
           print('Could not find this CD!')

class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    @staticmethod
    def load_inventory(file_name):
        """Function to manage data ingestion from file to a list of objects

        Reads the data from file identified by file_name into a 2D table
        (list of objects) table one line in the file represents one object row in table.

        Args:
            file_name (string): name of file used to read the data from
            
        Returns:
            lstOfCDObjects (list of objects): 2D data structure (list of objects) that holds the data during runtime
        """
        lstOfCDObjects.clear()  # this clears existing data and allows to load data from file
        try:
            objFile = open(file_name, 'r')
            for line in objFile:
                data = line.strip().split(',')
                objRow = [int(data[0]), data[1], data[2]]
                lstOfCDObjects.append(objRow)
            objFile.close()
        except OSError:
            print('File could not be opened!')
            
    @staticmethod
    def save_inventory(file_name, lst_Inventory):
        """ Function to  allow data to be written to the .txt file that has previously been created
        
        Args:
            strFileName (string): name of file used to write the data to
            lstOfCDObjects (list of objects): 2D data structure (list of objects) that holds the data during runtime
            
         Returns:
             None.
         """    
        try:
            objFile = open(strFileName, 'w')
            for row in lstOfCDObjects:
                lstValues = list(row.values())
                lstValues[0] = str(lstValues[0])
                objFile.write(','.join(lstValues) + '\n')
            objFile.close()
        except OSError:
            print('File could not be opened!')
            
# -- PRESENTATION (Input/Output) -- #
class IO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            lstOfCDObjects (list of objects): 2D data structure (list of objects) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in lstOfCDObjects:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')

    @staticmethod
    def enter_row():
       """ Gets user input for adding a new CD to the inventory

       Args:
           cd_id: The ID of the CD to be added
           cd_title: the Title of the CD to be added
           cd_artist: the Artist of the CD to be added

       Returns:
            The ID, Title, and Artist info for each CD rendered as a string.
       """
       while True:
           try:
               cd_id = int(input('Enter ID: ').strip())
               break
           except ValueError:
               print('You have not entered a number. Please enter a number')

       cd_title = input('What is the CD\'s title? ').strip()
       cd_artist = input('What is the Artist\'s name? ').strip()
       return [ cd_id, cd_title, cd_artist]


# -- Main Body of Script -- #
# 1. When program starts, read in the currently saved Inventory
FileIO.load_inventory(strFileName)

# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled: ')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileIO.load_inventory(strFileName, lstOfCDObjects)
            IO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
        DataProcessor.add_row(IO.enter_row())
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # 3.5 process delete a CD
    elif strChoice == 'd':
        # 3.5.1 get Userinput for which CD to delete
        # 3.5.1.1 display Inventory to user
        IO.show_inventory(lstOfCDObjects)
        # 3.5.1.2 ask user which ID to remove
        intIDDel = int(input('Which ID would you like to delete? ').strip())
        # 3.5.2 search thru table and delete CD
        DataProcessor.delete_row(intIDDel, lstOfCDObjects)
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # 3.6 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            FileIO.save_inventory(strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')

