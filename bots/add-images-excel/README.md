#About these files

##addImagesExcel.py
This is the script which allows adding images in the DH Replica's database. The image is specified by its URL and it is packed along with other information regarding the image into a JSON file.

####INPUT
* `url`: address to which you send the JSON file
* `original_excel_file`: name of the original Excel file containing metadata of the pictures to be added (but no ID)
  * it is assumed that the file is filled in starting from the second row (first row reserved to column names)
  * every row must contain the URL of the image
* `sheets`: names of the sheets inside the original Excel file
* `updated_excel_file`: name of the updated Excel file containing metadata of the pictures and their IDs

####OUTPUT
* `updated_excel_file.xlsx` filled in with all metadata and corresponding IDs

##tables.xlsx
Example file corresponding to `original_excel_file` in the script. It consists of the following columns:
* Image URL
* Author
* Title
* Date
* School
* Form
* Type 
* Origin
* Table Number
* Picture Number
* Webpage URL
* ID (not used here, but it will hold the IDs in `updated_excel_file.xlsx`.

##finalTables.xlsx
Example file corresponding to `updated_excel_file` in the script. 
It is generated starting from _tables.xlsx_ and by filling the ID column with the values returned by the DH Replica.
