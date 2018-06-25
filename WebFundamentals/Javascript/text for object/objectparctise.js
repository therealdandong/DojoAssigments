var users = [{name: "Michael", age:37}, {name: "John", age:30}, {name: "David", age:27}];
function callnametoage (names){
    for (var i=0; i<users.length;i++){
        if (users[i].name === names ){
            console.log(names,users[i].age)
        }
    }
}
callnametoage("Michael");//john is the same code

function callthemall () {
    for (var i=0;i<users.length;i++){
        console.log(users[i].name,users[i].age)
    }
}
callthemall();