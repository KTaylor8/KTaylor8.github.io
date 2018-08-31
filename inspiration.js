
function addimage() {
    // document.getElementById("img").style.display = "inline-block";
    // get all of the hidden images
    var images= document.getElementsByClassName("hiddenImage")

    // get the position of last element on a classList
    var position=images.length-1

    //show the first one
    images[position].classList.remove("hiddenImage");
    //
}
