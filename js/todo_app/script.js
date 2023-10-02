let form = document.querySelector('form');
let ul = document.getElementById('ul');

//get data from storage
let data = localStorage.getItem('todos');

ul.innerHTML = data;


//add new task on form submit
form.addEventListener('submit', function(e){
    e.preventDefault();

    let input = document.getElementById('input');
    console.log(input)
    if(input.value == ''){
        // alert('Kindly Enter a Todo.')
        let alert = document.getElementById('alert');
        alert.classList.remove('d-none');
    } else {

        let li = document.createElement('li');
        li.innerHTML = '<p>' + input.value + '</p> <button> X </button>';
        ul.append(li);


        input.value = '';
        store_data();
    }

    console.log(input);
});

//completed tasks
let lis = document.querySelectorAll('li');

console.log(lis)

let length = lis.length;

for(let i=0; i<length;i++){
    
    let li = lis[i];

    let p = li.children[0];
    p.addEventListener('click', function() {
        this.classList.toggle('completed');
        store_data();
    })

    let button = li.children[1];
    button.addEventListener('click', function(){
        console.log(i);
        lis[i].remove();
        store_data();

    })
}

function store_data(){
    localStorage.setItem('todos',ul.innerHTML);
}
