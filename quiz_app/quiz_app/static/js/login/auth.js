function check(){

    var username = localStorage.getItem("username"),
   		user_type = localStorage.getItem("user_type"),
        user_token = localStorage.getItem("user_token");

    if( username  && user_token ){
        window.location.href = user_type + "/" + username ;
    }
    else {
    	document.getElementById("box").style.display = "block";
    }
}
