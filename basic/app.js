const main_div = document.getElementById('root')

const para = document.createElement("p")
const text = document.createTextNode("Hello World")
para.appendChild(text);
para.classList.add("myStyle")

main_div.appendChild(para)