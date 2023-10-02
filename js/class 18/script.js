let questions = [
    {
        question: "What is 2 + 2?",
        answers: {
            ans1: 1,
            ans2: 2,
            ans3: 3,
            ans4: 4,
        },
        correct: 4
    },
    {
        question: "What is 2 + 3?",
        answers: {
            ans1: 1,
            ans2: 5,
            ans3: 3,
            ans4: 4,
        },
        correct: 5
    },
    {
        question: "What is 4 + 2?",
        answers: {
            ans1: 1,
            ans2: 2,
            ans3: 6,
            ans4: 4,
        },
        correct: 6
    },
    {
        question: "What is the capital of Pakistan?",
        answers: {
            ans1: "P",
            ans2: "Lahore",
            ans3: "Ichra",
            ans4: "Islamabad",
        },
        correct: "Islamabad"
    }
];


let currentQuestionIndex = 0;
let score = 0;
let total = questions.length;
start();

function start(){

    currentQuestionIndex = 0;
    score = 0;

    let start = document.querySelector('#start');

    start.addEventListener('click', function(){
        addQuestion();
    });
}


function addQuestion(){
    let quizContainer = document.querySelector('.quiz-container');

    quizContainer.innerHTML = `<h3>${questions[currentQuestionIndex].question}</h3>`;

    let answers = questions[currentQuestionIndex].answers;

    for(let key in answers){
        let button = document.createElement('button');
        button.innerText = answers[key];
        button.classList.add('ans');
        quizContainer.append(button);
    }
    checkAns();
}

function checkAns(){
    let ans = document.querySelectorAll('.ans');
    
    for(let i = 0; i < ans.length; i++){
        ans[i].addEventListener('click', function(){
            if(questions[currentQuestionIndex].correct == this.innerText){
                score++;
            }
            currentQuestionIndex++;
            if(currentQuestionIndex + 1 > questions.length){
                endGame();
            }
            else {
                addQuestion();
            }
        });
    }
}


function endGame(){
    document.querySelector('.quiz-container').innerHTML = `<h3>Game Over!</h3><br><h3>Score: ${score} / ${total}</h3><button id='exit'>Exit</button>`;

    let button = document.createElement('button');
    button.id = 'start';
    button.innerText = 'Restart Game';

    document.querySelector('.quiz-container').append(button);
    // start();
    // document.getElementById('exit').addEventListener('click',function name(params) {
    //     location.reload();
    // })
}
