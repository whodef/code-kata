/*
* Task
* Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). The fee structure is as follows:
* If the book is returned on or before the expected return date, no fine will be charged (i.e.: fine = 0).
* If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, fine = 15 Hackos x (the number of days late).
* If the book is returned after the expected return month but still within the same calendar year as the expected return date, the fine = 500 Hackos x (the number of months late).
* If the book is returned after the calendar year in which it was expected, there is a fixed fine of 10000 Hackos.
*
* Input Format
* The first line contains 3 space-separated integers denoting the respective day, month, and year on which the book was actually returned.
* The second line contains 3 space-separated integers denoting the respective day, month, and year on which the book was expected to be returned (due date).
*/

function processData(input) {

    const dates = input.split("\n");
    const a = dates[0].split(" ").map(Number);
    const b = dates[1].split(" ").map(Number);
    const actDate = new Date(a[2], a[1], a[0]);
    const expDate = new Date(b[2], b[1], b[0]);

    let fine = 0;

    if (actDate <= expDate) {
        fine = 0;
    } else if (a[1] === b[1]  &&  a[2] === b[2]) {
        fine = 15*(a[0] - b[0]);
    } else if (a[2] === b[2]) {
        fine = 500*(a[1] - b[1]);
    } else {
        fine = 10000;
    }
    console.log(fine);
}

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
    processData(_input);
});
