function login( num ){

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

	let response = fetch( request , {
      method: 'POST',
      mode: 'same-origin',		// Do not send CSRF token to another domain.
  		body: JSON.stringify(user)
	})
	.then(response => {

    if( response.ok ){
      //obj = JSON.parse(response.text());
      //console.log('response:' + obj.token )
      check(response.text()) 
    }
    else{
      document.getElementById("msg").innerHTML = "Username or password is incorrect";
    }
  })
}

function check (text){
    obj = JSON.parse(text);
  console.log('response:' + text )
}
