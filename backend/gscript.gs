function upload(form) {
  const folder = DriveApp.getFolderById("<FOLDER_ID>"); // open the folder in GDrive (in the same google account), see the id in the url

  const file = folder.createFile(Utilities.getUuid() + '.jpg', form.upFile);
}

function doGet() {
  return HtmlService.createHtmlOutputFromFile('form.html');
}