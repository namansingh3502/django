/*var input = document.getElementById("sbmt");
    input.addEventListener("keyup", function(event) {
    if (event.keyCode === 13) {
        event.preventDefault();
        document.getElementById("sbmt").click();
    }
});*/

function login(){

	const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;


	const request = new Request(
      '',                         //url
    	{headers: {'X-CSRFToken': csrftoken}}
	);

	let user = {
  		username: document.querySelector('[name=username]').value,
  		password: document.querySelector('[name=password]').value,
      user_type: document.querySelector('[name=user_type]').value
  };

  fetch(request, {
    method: 'POST',
    mode: 'same-origin',    // Do not send CSRF token to another domain.
    body: JSON.stringify(user)
  })
  .then(json => json.json())
  .then(function (data) {

    if( data.status == true ){

      var username = document.querySelector('[name=username]').value;

      localStorage.setItem("username", username);
      localStorage.setItem("user_token", data.token);
      localStorage.setItem("user_type", document.querySelector('[name=user_type]').value);

      window.location.href = document.querySelector('[name=user_type]').value + "/" +username;

    }
    else{
      document.getElementById("msg").innerHTML = "Username or Password incorrect";
    }

  })
  .catch(function (error) {
    console.log('Request failed', error);
  });
}

