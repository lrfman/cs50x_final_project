document.addEventListener("DOMContentLoaded", function (){
    let button = document.querySelector("#random");
    button.addEventListener("click", function (){
        let red = document.querySelector("#red");
        let green = document.querySelector("#green");
        let blue = document.querySelector("#blue");
        red.value = `${Math.floor(Math.random() * 256)}`;
        green.value = `${Math.floor(Math.random() * 256)}`;
        blue.value = `${Math.floor(Math.random() * 256)}`;
    });
});
