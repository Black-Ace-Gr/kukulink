const button=document.getElementById("ai-button");

const windowBox=document.getElementById("ai-window");

const closeBtn=document.getElementById("close-ai");

const send=document.getElementById("send");

const input=document.getElementById("message");

const messages=document.getElementById("ai-messages");

button.onclick=()=>{

windowBox.style.display="flex";

};

closeBtn.onclick=()=>{

windowBox.style.display="none";

};

function addMessage(text,type){

const div=document.createElement("div");

div.className=type;

div.innerText=text;

messages.appendChild(div);

messages.scrollTop=messages.scrollHeight;

}

async function ask(){

const text=input.value.trim();

if(text==="") return;

addMessage(text,"user");

input.value="";

const typing=document.createElement("div");

typing.className="bot";

typing.innerText="...";

messages.appendChild(typing);

messages.scrollTop=messages.scrollHeight;

const form=new FormData();

form.append("message",text);

const response=await fetch("/ai/chat/",{

method:"POST",

headers:{

"X-CSRFToken":getCookie("csrftoken")

},

body:form

});

const data=await response.json();

typing.remove();

addMessage(data.reply,"bot");

}

send.onclick=ask;

input.addEventListener("keypress",e=>{

if(e.key==="Enter"){

ask();

}

});

function getCookie(name){

let cookieValue=null;

if(document.cookie && document.cookie!==""){

const cookies=document.cookie.split(";");

for(let cookie of cookies){

cookie=cookie.trim();

if(cookie.startsWith(name+"=")){

cookieValue=decodeURIComponent(cookie.substring(name.length+1));

break;

}

}

}

return cookieValue;

}