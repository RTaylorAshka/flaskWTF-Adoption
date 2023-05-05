console.log('here!')


// Makes entire div act like a link, links to /div.id where div.id is set to the corrisponding pet.id in the HTML page
function redirect(div){

    window.location = (`http://127.0.0.1:5000/${div.id}`);
    return true;
}


// If image URL fails to load for whatever reason, replaces it with the default image.
function replaceImage(image){
    image.onerror = "";
    image.src = "http://clipart-library.com/images/rTLo9BGkc.png";
    return true;
}




