function addMoreMessage(webSocket){

  // webSocket is an instance of WebSocket class
  
  const userInputDom = document.querySelector("#chat-message-user");
  const username = userInputDom.value;
  const roomInputDom = document.querySelector("#chat-message-room");
  const room_name = roomInputDom.value;
  const messageInputDom = document.querySelector("#chat-message-input");
  const message = messageInputDom.value;

  const messageBlock = document.getElementById("message-block");
  const messageRow = document.createElement("div");
  messageRow.className = "message-row primary-message-row";

  const messageCard = document.createElement("div");
  messageCard.className = "message-card";

  const messageUsername = document.createElement("div");
  messageUsername.className = "message-name";
  messageUsername.textContent = "just now";

  const messageBox = document.createElement("div");
  messageBox.className = "message-box";
  messageBox.textContent = message;

  messageRow.appendChild(messageCard);
  messageCard.appendChild(messageUsername);
  messageCard.appendChild(messageBox);
  messageBlock.appendChild(messageRow);

  webSocket.send(
    JSON.stringify({
      username: username,
      room_name: room_name,
      message: message,
    })
  );

  // clear input value
  messageInputDom.value = "";
};