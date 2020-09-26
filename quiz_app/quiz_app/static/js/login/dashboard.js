function dashboard(){

	let user_token = localStorage.getItem("user_token");
console.log("hello I am working")

  fetch( "dashboard",{
  	method: 'POST',
  	mode: 'same-origin',
    body: JSON.stringify(user_token),
  	headers: {
    	"Content-Type": "application/json"
  	}
  })
  .then(json => json.json())
  .then(function (data) {

    console.log(data)

  })
  .catch(function (error) {
    console.log('Request failed', error);
  });
	
}