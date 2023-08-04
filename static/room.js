const roomName = JSON.parse(document.getElementById("room-name").textContent);

const chatSocket = new WebSocket(
  "ws://" + window.location.host + "/ws/chat/" + roomName + "/"
);

chatSocket.onmessage = function (e) {
  const data = JSON.parse(e.data);
  chatLog = document.querySelector("#chat-log");
  chatLog.value += data.username + ": " + data.message + "\n";
};

chatSocket.onclose = function (e) {
  console.error("Chat socket closed unexpectedly");
};

document.querySelector("#chat-message-input").focus();
document.querySelector("#chat-message-input").onkeyup = function (e) {
  if (e.keyCode === 13) {
    // enter, return
    document.querySelector("#chat-message-submit").click();
  }
};

var currentTime = function () {
  let current = new Date();
  return current.toLocaleTimeString();
};

document.querySelector("#chat-message-submit").onclick = function (e) {
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

  chatSocket.send(
    JSON.stringify({
      username: username,
      room_name: room_name,
      message: message,
    })
  );
  messageInputDom.value = "";
};