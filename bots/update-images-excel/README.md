#About these files

##updateImagesExcel.py
This is the script which allows updating images in the DH Replica's database by specifying their IDs in an Excel file. <br />
In particular, it allows modifying the following metadata:
* Author
* Title
* Date
* School
* Form 
* Type

####INPUT
* `DBurl`: address to which you send the JSON file containing the overwriting metadata
* `excel_file`: name of the Excel file containing IDs and metadata of the pictures to be updated
  * it is assumed that the file is filled in starting from the second row (first row reserved to column names)
  * every row must contain the ID of the image
* `sheets`: names of the sheets inside the Excel file

####OUTPUT
* For each ID sent to the DH Replica in order to update the corresponding image, a message in the console is printed as a feedback. 
Messages correspond to the [status code of the HTTP protocol](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes). For instance, having as response `200` denotes that the image was successfully removed from the database.

##toBeUpdated.xlsx
Example file corresponding to `excel_file` in the script. It consists of an ID column and of the aforementioned ones.

