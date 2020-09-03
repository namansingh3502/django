function signup( ){

	const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;


	const request = new Request(
    	'/new_user/',
    	{headers: {'X-CSRFToken': csrftoken}}
	);

	let user = {
      name: document.querySelector('[name=name]').value,
  		username: document.querySelector('[name=username]').value,
  		password: document.querySelector('[name=password]').value,
  		user_type: document.querySelector('[name=user_type]').value,
	};

	let response = fetch( request , {
 		  method: 'POST',
 		  mode: 'same-origin',		// Do not send CSRF token to another domain.
  	  body: JSON.stringify(user)
	})
	.then(json => json.json())
  .then(function (data) {

    if( data.status == true){
      console.log("success")
      
      window.location.href = "/";

    }
    else{
      document.getElementById("msg").innerHTML = "Username already exist";
    }
  })
  .catch(function (error) {
    console.log('Request failed', error);
  });
}