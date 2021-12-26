var layoutheader = document.getElementsByClassName("header__container")[0]

let button = document.createElement("button")

button.innerHTML = "Download memes"

button.onclick = function () {
    var memes = document.getElementsByClassName("media__image");
    //alert(memes)

    for(var meme in memes) {
        var MEME = memes[meme].src
    }
    if(meme.includes("mp4")) {
        alert(`Meme ${MEME}`)
    }
    else {
        alert("No video/meme to download")
    }
};  

layoutheader.appendChild(button)