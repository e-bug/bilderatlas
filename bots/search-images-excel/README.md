#About these files

##searchImagesExcel.py
This is the script which allows querying the DH Replica's database by specifying positive and negative IDs in an Excel file. <br />
It sends a JSON file containing a list of positive IDs, a list of negative IDs and the number of results (in descending score order) to be returned by the database. <br />
The results of the query are placed in a new directory containing an Excel file filled with the metadata of the images, and the images themselves named in descending order.

####INPUT
* `url`: address to which you perform your query
* `nResults`: number of results returned by the database
* `excel_file`: name of the original Excel file containing IDs 
  * it is assumed that the file is filled in starting from the second row (first row reserved to column names)
* `sheets`: names of the sheets inside the original Excel file
  * note that the source code assumes a single sheet but you can easily create a `for loop` to iterate through all your sheets

####OUTPUT
* A folder named with the time of creation containing:
  * an Excel file, named as the folder, which contains the metadata shown in `searchIDs.xlsx` for each image in the result
  * the result images, named in descending order of score
    * if you do not want to retrieve them, comment (by using `#`) lines 81 and 82 of the source file.

A [video](https://github.com/e-bug/bilderatlas/blob/master/demo/bilderatlas_search-excel.avi) showing how to perform query by using this script is available in the demo folder.

##searchIDs.xlsx
Example file corresponding to `excel_file` in the script. It consists of the following columns:
* positive IDs
* negative IDs
* score (not used here, but it will hold the scores in the result Excel file)
* ID (not used here, but it will hold the IDs in the result Excel file)
* Author (not used here, but it will hold the authors of the artworks in the result Excel file)
* Title (not used here, but it will hold the titles of the artworks in result the Excel file)
* Date (not used here, but it will hold the dates of the artworks in result the Excel file)
* Table Number (not used here, but it will hold the table number of the bilderatalas artworks in the result Excel file)
* Image URL (not used here, but it will hold the URL of the artworks in the result Excel file)
* Webpage URL (not used here, but it will hold the URL of the corresponding webpage of the artworks in the result Excel file)

