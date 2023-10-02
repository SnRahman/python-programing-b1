let questions = [
    {
        question : "What is 10 + 2?",
        options : {
            ans1 : 5,
            ans2 : 8,
            ans3 : 12,
            ans4 : 15,
        },
        correct : 12
    },
    {
        question: "What is 15 - 10?",
        options: {
            ans1: 1,
            ans2: 5,
            ans3: 2,
            ans4: 4,
        },
        correct: 5
    },
    {
        question: "What is 4 + 10?",
        options: {
            ans1: 1,
            ans2: 2,
            ans3: 6,
            ans4: 14,
        },
        correct: 14
    },
    {
        question: "What is the capital of Pakistan?",
        options: {
            ans1: "P",
            ans2: "Lahore",
            ans3: "Ichra",
            ans4: "Islamabad",
        },
        correct: "Islamabad"
    }
];

let index = 0;
let start = document.getElementById('start');
let correct_answers = 0;

start_game();

function start_game(){
    start.addEventListener('click',function(){

        add_question()
    
    })  
}
function add_question(){
    let Container = document.querySelector('.container');

    let question = questions[index];
    // Container.innerHTML =  `<h1> ${ question.question}</h1>`;
    Container.innerHTML =  "<h1>" + question.question + "</h1> ";

    let options = question.options;

    for(let option in options){
        // console.log(option);

            option_btn = document.createElement('button');
            option_btn.innerHTML = options[option];
            option_btn.classList.add('answer');
            Container.append(option_btn);
    }
    check_answer()
}

function check_answer(){

    
    let answer_btn = document.getElementsByClassName('answer');

    let question = questions[index];


    for (ans_btn of answer_btn) {
        ans_btn.addEventListener('click', function(){
            
            let user_selection = this.innerText;

            if(user_selection == question.correct){
                console.log('correct answer');
                correct_answers++;
            }

            index++;

            questions_length = questions.length;
            if (index < questions_length) {
                console.log('questions_length :' +questions_length)
                console.log('index :' + index)
                add_question();
            } else {
                end_game()
            }
           
        })
        console.log(ans_btn);
    }
}


function end_game() {
    // questions_length = questions.length;

    let Container = document.querySelector('.container');
    Container.innerHTML =  "<h1> Game Over!</h1> <h1> Score:" + correct_answers + "/"+questions_length + "</h1>";

    let button = document.createElement('button');
    button.id = 'start';
    button.innerText = 'Restart Game';
    Container.append(button);
    start_game();
}
