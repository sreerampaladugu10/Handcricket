var scr = 0;
var compScr = 0;
var userBatting = true;
var userChoice = 0;
var compBatting = false;
var sts = document.getElementById("status");
var sts2 = document.getElementById("status2");
var sts3 = document.getElementById("status3");

function addToScore(val) {
    if (userBatting) {
        compChoice = Math.floor(Math.random() * 6) + 1;
        document.getElementById("userChoice").innerHTML = "You: " + val;
        document.getElementById("compChoice").innerHTML = "Computer: " + compChoice;

        if (val === compChoice) {
            userChoice = 0;
            playerOut();
        } else {
            scr += val;
            document.getElementById("score").innerHTML = "Your Score: " + scr;
        }

        // Check for the winner after every user's turn
        if (compScr > scr) {
            compWin();
        }
    } else if (compBatting) {
        compChoice = Math.floor(Math.random() * 6) + 1;
        document.getElementById("compChoice").innerHTML = "Computer: " + compChoice;
        document.getElementById("userChoice").innerHTML = "You: " + val;

        if (val === compChoice) {
            compChoice = 0;
            compOut();
        } else {
            compScr += compChoice; // Add computer's choice to its score
            document.getElementById("compScore").innerHTML = "Computer score: " + compScr;
        }

        // Check for the winner after every computer's turn
        if (compScr > scr) {
            compWin();
        }
    }
}

function playerOut() {
    sts.innerHTML = "Out! The computer will now bat.";
    userBatting = false;
    compBatting = true;
    userChoice = 0;
    compScr = 0;
    const myTimeout = setTimeout(myMsg, 3000);
    function myMsg() {
        sts.innerHTML = "Computer is Batting ";
    }

    document.getElementById("userChoice").innerHTML = '';
}

function compOut() {
    if (compScr > scr) {
        sts.innerHTML = "Computer Wins";
    } else {
        userWin();
    }
}

function userWin() {
    sts.innerHTML = '';
    sts2.innerHTML = "You Win";
}

function compWin() {
    sts.innerHTML = "Computer Wins";
}

function closeAll() {
    document.getElementById("btn1").style.visibility = "hidden";
    document.getElementById("btn2").style.visibility = "hidden";
    document.getElementById("btn3").style.visibility = "hidden";
    document.getElementById("btn4").style.visibility = "hidden";
    document.getElementById("btn5").style.visibility = "hidden";
    document.getElementById("btn6").style.visibility = "hidden";
}
