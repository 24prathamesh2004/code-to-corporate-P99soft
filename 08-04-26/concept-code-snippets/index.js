// Variables
let name = "John";
const age = 20;

// Functions
function greet(name) {
  return "Hello " + name;
}

// Arrow Function
const add = (a, b) => a + b;

// Array Methods
const arr = [1, 2, 3];
arr.map(x => x * 2);
arr.filter(x => x > 1);

// Objects
const user = {
  name: "John",
  age: 25
};

// DOM Manipulation
const btn = document.querySelector("button");
btn.addEventListener("click", () => {
  alert("Clicked");
});

// Form Handling
document.getElementById("form").addEventListener("submit", (e) => {
  e.preventDefault();
  console.log("Form submitted");
});

// Fetch API
fetch("https://api.example.com")
  .then(res => res.json())
  .then(data => console.log(data));

// Async/Await
async function getData() {
  const res = await fetch("https://api.example.com");
  const data = await res.json();
  console.log(data);
}

// Local Storage
localStorage.setItem("key", "value");
localStorage.getItem("key");

// ES6 Features
const { name: userName } = user; // destructuring
const newArr = [...arr]; // spread