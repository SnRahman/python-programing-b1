let form = document.querySelector('form');
let ul = document.querySelector('ul');
let input = document.querySelector('input');

form.addEventListener('submit', function(e){
    e.preventDefault();


    // if(input.value == ''){
    //     alert('Please enter todo');
    // }
    // else {
        let li = document.createElement('li');
        li.innerHTML = `<p>${input.value}</p> <button class="btn_dlt">X</button>`;

        ul.prepend(li);
        input.value = '';

        dlt_todo();
        saveTodos();
    // }

});


function dlt_todo(){
    let lis = document.querySelectorAll('li');

    for(let i = 0; i < lis.length; i++){
        lis[i].children[1].addEventListener('click', function(){
            lis[i].remove();
            saveTodos()
        });

        lis[i].addEventListener('click', function(){
            lis[i].children[0].classList.toggle('completed');
                saveTodos()
        });
    }
}

function saveTodos(){
    localStorage.setItem('todos', ul.innerHTML);
}

showTodos()
function showTodos(){
    ul.innerHTML = localStorage.getItem('todos');
    dlt_todo();
}