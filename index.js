//document.getElementById([id]).innerHTML =
var i_love_kpop_sticker = null;

            function init(){
               i_love_kpop_sticker = document.getElementById('myImage');
               i_love_kpop_sticker.style.position= 'relative';
               i_love_kpop_sticker.style.left = '0px';
            }

            function moveRight(){
               i_love_kpop_sticker.style.left = parseInt(i_love_kpop_sticker.style.left) + 30 + 'px';
            }
            function moveLeft(){
               i_love_kpop_sticker.style.left = parseInt(i_love_kpop_sticker.style.left) - 30 + 'px';
            }

            window.onload =init;
