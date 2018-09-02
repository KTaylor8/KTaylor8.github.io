//window.onload makes it so the initial things happen only after the page is actually loaded
var post1Filled = false;
window.onload = function () {
//hiding the post boxes
document.getElementById("postBox0").style.display = "none";
document.getElementById("postBox2").style.display = "none";
document.getElementById("like0").style.display = "none";
document.getElementById("dislike0").style.display = "none";
}

function post() {
    var postTextEntered = document.getElementById("enteredPost").value;
    if(post1Filled == false) {
      document.getElementById("textSpace0").innerHTML = postTextEntered;
      post1Filled = true;
      document.getElementById("noPosts").style.display = "none";
      document.getElementById("postBox0").style.display = "block";
    }
    else {//need to add more else ifs and variables for more posts
      document.getElementById("textSpace2").innerHTML = postTextEntered;
      document.getElementById("postBox0").style.visibility = "visible";
      document.getElementById("postBox2").style.visibility = "visible";
    }
}

var count1 = 1;
function sendComments0() {
    var x = document.getElementById("commentBox0").value;
    // chat2.push(x);
    var p = document.createElement("p");
    p.className = 'chatMessage';
    p.innerHTML = count1 + ". " + x;
    document.getElementById("commentList0").appendChild(p);
    count1 = count1 + 1; // count++; or ++count; or count += 1;
}

var count2 = 1;
function sendComments2() {
    var x = document.getElementById("commentBox2").value;
    // chat2.push(x);
    var p2 = document.createElement("p");
    p2.className = 'chatMessage';
    p2.innerHTML = count2 + ". " + x;
    document.getElementById("commentList2").appendChild(p2);
    count2 = count2 + 1; // count++; or ++count; or count += 1;
}

function thumbsUp0() {
  document.getElementById("like0").style.display = "block";
  document.getElementById("dislike0").style.display = "none";
}

function thumbsDown0() {
  document.getElementById("like0").style.display = "none";
  document.getElementById("dislike0").style.display = "block";
}
