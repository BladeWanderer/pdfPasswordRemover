This project remove password from pdf's

1. create a config.json file like so (absolute paths):
   - make sure the pdf_directoryis the encrypted folder
````
   {
    "pdf_directory": "/path/to/encrypted/pdf/folder",
    "unencrypted_directory": "/path/to/output/folder",
    "password": "your_password"
   }
   ````
2. save your encrypted files in the encrypted folder
