//add team


function getRandomColor() {
    var colors = [ '##a1ffce;', '#a1ffce'] // green shades 
    var randomIndex = Math.floor(Math.random() * colors.length);
    return colors[randomIndex];
}

function createBox() {
    var taskName = prompt("Enter the task name:");
    var dueDate = prompt("Enter the due date:");
    var members = prompt("Enter a comma-separated list of active members (limit 3):");
    var membersArray = members.split(',').map(member => member.trim());//this is for setting the limit of active members to 3
    var limitedMembers = membersArray.slice(0, 3).join(', ');
    var box = document.createElement("div");
    box.classList.add("box");//adds the box properties
    var taskNamePara = document.createElement("p");
    taskNamePara.textContent = "Task Name: " + taskName;
    taskNamePara.classList.add("writings");//adds the text properties
    var dueDatePara = document.createElement("p");
    dueDatePara.textContent = "Due Date: " + dueDate;
    dueDatePara.classList.add("writings");
    var membersPara = document.createElement("p");
    membersPara.textContent = "Active Members: " + limitedMembers;
    membersPara.classList.add("writings");
    var randomColor = getRandomColor();//set
    box.style.background = randomColor; //set the background color
    box.appendChild(taskNamePara);
    box.appendChild(dueDatePara);
    box.appendChild(membersPara);
    document.querySelector('.box-container').appendChild(box);//this adds the container properties
}




