function indexAccessCheck(event) {
    event.preventDefault()
    if (document.getElementById('indexAccessPassword').value == 'meGustaElKpop') {
        // multiple elements w/ this class means that it returns a list and you have to set the element displays individually
        var defaultHiddenElems = document.getElementsByClassName('defaultHide');
        for (var i = 0; i < defaultHiddenElems.length; i++) {
            defaultHiddenElems[i].style.display = 'block';
        }
        var defaultShownElems = document.getElementsByClassName('defaultShow');
        for (var i = 0; i < defaultShownElems.length; i++) {
            defaultShownElems[i].style.display = 'none';
        }
    }
    else {
        alert("Incorrect password")
    }
}

function moveRight() {
    i_love_kpop_sticker.style.left = parseInt(i_love_kpop_sticker.style.left) + 30 + 'px';
}
function moveLeft() {
    i_love_kpop_sticker.style.left = parseInt(i_love_kpop_sticker.style.left) - 30 + 'px';
}

window.onload = function () {
    // var defaultHiddenElems = document.getElementsByClassName('defaultHide');
    // for (var i = 0; i < defaultHiddenElems.length; i++) {
    //     defaultHiddenElems[i].style.display = 'none';
    // }
    // var defaultShownElems = document.getElementsByClassName('defaultShow');
    // for (var i = 0; i < defaultShownElems.length; i++) {
    //     defaultShownElems[i].style.display = 'block';
    // }
    var i_love_kpop_sticker = null;
    i_love_kpop_sticker.style.position = 'relative';
    i_love_kpop_sticker.style.left = '0px';
}