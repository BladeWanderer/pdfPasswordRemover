This project remove password from pdf's

1. create a config.json file like so (absolute paths):
   - make sure the pdf_directory is named: encrypted
   - in case no such directory exists, it would be created but it would be empty and an error notification will inform you to put your encrypted files there
````
   {
    "pdf_directory": "/path/to/encrypted/pdf/folder",
    "unencrypted_directory": "/path/to/output/folder",
    "password": "your_password"
   }
   ````
2. save your encrypted files in the encrypted folder
