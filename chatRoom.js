//window.onload makes it so the initial things happen only after the page is actually loaded
var postsAvailable = 1;
var post1Filled = false;
window.onload = function () {
  for (var postNum = 0; postNum < postsAvailable; postNum++) {
//hiding the post boxes and likes/dislikes
document.getElementById("postBox" + postNum).style.display = "none";
document.getElementById("like" + postNum).style.display = "none";
document.getElementById("dislike" + postNum).style.display = "none";
  }
}

function post() {
  for (var postNum = 0; postNum < postsAvailable; postNum++) {
    //if the post box with this post number isn't displayed, give it the text and display it
    if (document.getElementById("postBox" + postNum).style.display == "none"){
      if (postNum == 0) {
        document.getElementById("noPosts").style.display = "none";
      }
      var postTextEntered = document.getElementById("enteredPost").value;
      document.getElementById("textSpace" + postNum).innerHTML = postTextEntered;
      document.getElementById("postBox" + postNum).style.display = "block";
      break;
    }
  }

    // var postTextEntered = document.getElementById("enteredPost").value;
    // if(post1Filled == false) {
    //   document.getElementById("textSpace0").innerHTML = postTextEntered;
    //   post1Filled = true;
    //   document.getElementById("noPosts").style.display = "none";
    //   document.getElementById("postBox0").style.display = "block";
    // }
    // // else {//need to add more else ifs and variables for more posts
    // //   document.getElementById("textSpace2").innerHTML = postTextEntered;
    // //   document.getElementById("postBox0").style.visibility = "visible";
    // //   document.getElementById("postBox2").style.visibility = "visible";
    // //  }
}

/*not sure how to make this for the general case since different posts will need
*different counts and idk how to detect if a veriable already exists or not*/
var count0 = 0;
function sendComments0() {
    var p = document.createElement("p");
    p.className = 'chatMessage';
    p.innerHTML = count0 + ". " + document.getElementById("commentBox0").value;
    document.getElementById("commentList0").appendChild(p);
    count0 = count0 + 1; // count++; or ++count; or count += 1;
}

function thumbsUp(postNum) {
  document.getElementById("like"+postNum).style.display = "block";
  document.getElementById("dislike"+postNum).style.display = "none";
}

function thumbsDown(postNum) {
  document.getElementById("like"+postNum).style.display = "none";
  document.getElementById("dislike"+postNum).style.display = "block";
}
