# libraries.io
#### A general purpose python utility written to connect to the libraries.io api that helps find the relavent open source code libraries. 

### Usage:<br>
  #### python rest-connect.py<br>
 This will cause the program to search for the libraries.io code base. The code base has a collection of more than 30 million open source project and libraries. At the end of the script execution, the program will be clone the repositories for the top 5 entries of the search result as well as save into the database, the results of the search.
 
 #### The database
 The database has a single table named records. In which there are three fields namely: ID, Name and Description
 
