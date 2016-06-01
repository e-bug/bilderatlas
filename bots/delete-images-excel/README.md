#About these files

##deleteImagesExcel.py
This is the script which allows adding images in the DH Replica's database. The image is specified by its URL and it is packed along with other information regarding the image into a JSON file.

####INPUT
* `DBurl`: address to which you send the JSON file
* `excel_file`: name of the file containing the IDs of the images to be deleted in the database
  * it is assumed that the file is filled in starting from the second row (first row reserved to column names)
* `sheets`: names of the sheets inside the original Excel file

####OUTPUT
* For each ID sent to the DH Replica in order to eliminate the corresponding image, a message in the console is printed as a feedback. <br />
  Messages correspond to the [status code of the HTTP protocol](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes). For instance, having as response `200` denotes that the image was successfully removed from the database.

##ToBeEliminated.xlsx
Example file corresponding to `excel_file` in the script. It consists of the ID column only.
