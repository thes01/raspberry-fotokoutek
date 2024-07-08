## Backend (Google Scripts)

1. Create a new Google Script project (script.google.com)
2. Copy the `backend/gscript.gs` and `backend/form.html` file into the project.
3. In the same Google account, create a folder in Google Drive.
4. Copy the ID of the folder (see url) and update it in the `gscript.gs` file.
5. Publish the project as a web app (Implement > New implementation).
  - Execute as "me"
  - Who has access: "anyone"
6. The `form.html` should be accessible from the generated URL. (thanks to the `doGet` function in `gscript.gs`).
7. Uploading a photo through the form should save it in the Google Drive folder.


## Frontend (Raspberry PI)

Frontend is done in two parts:
- photo slideshow presentation (frontend/main.py)
- photo sync by [rclone](https://github.com/rclone/rclone)


1. Load the python script to raspberry
2. Install and configure rclone to sync your Google Drive folder with a local folder in the raspberry. (TODO documentation)
3. Add both the script and the rclone command to startup jobs. (TODO documentation)