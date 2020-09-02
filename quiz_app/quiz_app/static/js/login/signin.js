function login(){

	const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;


	const request = new Request(
    	'/login/',
    	{headers: {'X-CSRFToken': csrftoken}}
	);

	let user = {
  		username: document.querySelector('[name=username]').value,
  		password: document.querySelector('[name=password]').value,
  		user_type: localStorage.getItem("user_type")
	};

	/*let response = fetch( request , {
      method: 'POST',
      mode: 'same-origin',		// Do not send CSRF token to another domain.
  		body: JSON.stringify(user)
	})
	.then(response => {

    if( response.ok ){
        
      }
    else{
      document.getElementById("msg").innerHTML = "Username or password is incorrect";
    }
  })*/

  fetch(request, {
    method: 'POST',
    mode: 'same-origin',    // Do not send CSRF token to another domain.
    body: JSON.stringify(user)
  })
  //.then(response => response.json())
  //.then(json => json.json())
  .then(function (data) {
    console.log('Request succeeded with JSON response', data);
    console.log(data.json())
  })
  .catch(function (error) {
    console.log('Request failed', error);
  });
}