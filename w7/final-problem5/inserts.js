for(i=0;i<=2000;i++){
	db.fubar.insert({"a":(Math.floor(Math.random()*1000)+100), "b":(Math.floor(Math.random()*10000)+1000), "c":(Math.floor(Math.random()*1000)+10000)});
}
