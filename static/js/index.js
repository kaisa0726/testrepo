const area = document.getElementById("area");
const headerDiv = document.getElementById("headerDiv");
const input_text = document.getElementById("input_text");
const submit = document.getElementById("a");
const destination = document.getElementById("destination");
const address = document.getElementById("address");
const createMail = document.getElementById("createMail");
const push = document.getElementById("push");

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

submit.addEventListener('click',function(){
    const input = input_text.value;

})