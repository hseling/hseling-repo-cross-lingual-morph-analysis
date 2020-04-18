function corpDownloader(uri,filename) { 
    var link = document.createElement("a");
    link.download = name;
    link.href = uri;
    link.click();
    alert("Press Ctrl+S (Win/Linux) or Cmd+S (Mac OS) to download the file :)");
}