albums = db.albums;
images= db.images;
i=0;
longAlbums = albums.find().length();
longImages = images.find().length();
while (i<=longImages){
	if((albums.find({"images":i})).length()<=0){
            images.remove({"_id":i});
            i++;
        }else{
            i++;
        }
}