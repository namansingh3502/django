function dashboard(){

	let user_token = localStorage.setItem("user_token");
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
    console.log("hello I am working")

  })
  .catch(function (error) {
    console.log('Request failed', error);
  });
	
}