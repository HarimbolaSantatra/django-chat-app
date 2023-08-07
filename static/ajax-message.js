const loadingBtn = document.querySelector('#load-more-btn');

function loadMoreMessage(roomName, webSocket){
	var xhr = new XMLHttpRequest();
	xhr.open('GET', `http://localhost:8000/chat/load/${roomName}`, true);
	xhr.setRequestHeader("Content-Type", "application/json");
	xhr.send();
	xhr.onload = function(){
		if(xhr.status === 200) {
			addMoreMessage(webSocket)
		}
	}
}


loadingBtn.addEventListener('click', () => {
	const room_name = document.querySelector("#chat-message-room").value;
	loadMoreMessage(room_name, chatSocket);
})

