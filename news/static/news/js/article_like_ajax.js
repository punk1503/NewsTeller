function update_like_counter (new_like_amount) {
	document.querySelector('#likes_span').innerHTML = new_like_amount
}

function create_request () {
	let httpRequest;
	if (window.XMLHttpRequest) {
		httpRequest = new XMLHttpRequest()
	} else if (window.ActiveXObject) {
		httpRequest = new ActiveXObject("Microsoft.XMLHTTP")
	}

	httpRequest.overrideMimeType('text/xml')

	httpRequest.onreadystatechange = () => {
		if (httpRequest.readyState == 4) {
			if (httpRequest.status == 200) {
				const response_data = JSON.parse(httpRequest.responseText)
				update_like_counter(response_data.like_counter)
				let like_button = document.querySelector('.like-btn')
				if (response_data.current_user_liked) {
					like_button.classList.add('checked')
				} else {
					like_button.classList.remove('checked')
				}
			}
		}
	}

	return httpRequest
}

function send_request (user_id) {
	let request = create_request(method='POST')
	request.open('POST', document.location.href, true) // async == true
	request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded') // needed for POST request
	request.setRequestHeader('X-CSRFToken', window.CSRF_TOKEN)
	request.send(`user_id=${user_id}`)
}
