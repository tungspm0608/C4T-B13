
var questions = [
    {
        prompt:"How many NBA teams are there in 2019?\n(a) 30\n\
        (b) 28\n(c) 36",
        answer: "a"
    },
    {
        prompt: "Which team is Aaroon Gordon in?\n(a) GoldenState Warriors\n\
        (b) Phoenix Sun\n(c) Orlando Magic",
        answer: "c"
    },
    {
        prompt: "Who won the first Kobe Bryant All-star MVP award in 2020?\n(a) Kemba Walker\n\
        (b) Kawhi Leonard\n(c) Russell Westbrook",
        answer: "b"
    },
]
var score = 0; 
    

for(var i=0; i < questions.length; i++){
    var response= window.prompt(questions[i].prompt)
    if(response == questions[i].answer){
        score++;
        alert("CORRECT!!!");
    }   else {
        alert("WRONG!!!");

    }
}
alert("Your score is" + score + "/" + questions.length);
    