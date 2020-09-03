function login(){

	const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;


	const request = new Request(
      '',                         //url
    	{headers: {'X-CSRFToken': csrftoken}}
	);

	let user = {
  		username: document.querySelector('[name=username]').value,
  		password: document.querySelector('[name=password]').value,
      user_type: document.querySelector('[name=user_type]').value,	
  };

  fetch(request, {
    method: 'POST',
    mode: 'same-origin',    // Do not send CSRF token to another domain.
    body: JSON.stringify(user)
  })
  .then(json => json.json())
  .then(function (data) {

    if( data.status == true){

      localStorage.setItem("user_token", data.token);
      localStorage.setItem("username", document.querySelector('[name=username]').value);
      localStorage.setItem("password", document.querySelector('[name=password]').value);
      localStorage.setItem("user_type", document.querySelector('[name=user_type]').value);
      localStorage.setItem("user_pk", data.pk);
      window.location.href = "/" +localStorage.getItem("user_type") + "/" + localStorage.getItem("username");

    }
    else{
      document.getElementById("msg").innerHTML = "Username or Password incorrect";
    }

  })
  .catch(function (error) {
    console.log('Request failed', error);
  });
}