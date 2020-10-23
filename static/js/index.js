const area = document.getElementById("area");
const headerDiv = document.getElementById("headerDiv");
const input_text = document.getElementById("input_text");
const button = document.getElementById("button");
const destination = document.getElementById("destination");
const address = document.getElementById("address");
const createMail = document.getElementById("createMail");
const push = document.getElementById("push");
const scrollbar = document.getElementById("scrollbar");

function a() {
    area.style.display = "block";
}

createMail.addEventListener("click",function(){
    const div = document.createElement("div");
    div.setAttribute("id","div")
    push.appendChild(div);
    const destiMessa = document.getElementById("destination").value ;
    const destiTag = document.createElement("p");
    destiTag.innerHTML = destiMessa;
    div.appendChild(destiTag);
    const addMessa = document.getElementById("address").value ;
    const addTag = document.createElement("p");
    addTag.innerHTML = addMessa;
    div.appendChild(addTag);
    area.style.display = "none";
})

function turnBack(){
    area.style.display = "none";
}

headerDiv.addEventListener("mouseover",function(){
    headerDiv.style.backgroundColor = "orange";
})
headerDiv.addEventListener("mouseout",function(){
    console.log("foo");
    headerDiv.style.backgroundColor = "rgb(139, 142, 145)"
})

button.addEventListener('click',function(){
    const input = input_text.value ;
    const element = document.createElement("p");
    element.innerHTML = input;
    scrollbar.appendChild(element);
    element.setAttribute('id', 'add')
})

const 