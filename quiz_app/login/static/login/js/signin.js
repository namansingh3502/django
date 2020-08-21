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
	.then(res => {
        return res.json()
    })
    .then((response) => {
        console.log('res: ' + response )
    })

}
