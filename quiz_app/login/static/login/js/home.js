function login( user_type ) {
	localStorage.setItem("user_type", user_type);
	window.location.href = "/login";
}