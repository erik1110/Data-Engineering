console.log("Hello World!");

//================================ var 變量 ====================================

var name = "John";
var age = 30;

console.log(name+age);
console.log(age+age);
console.log(name+" is "+age+" years old.");

age="thirty";

console.log(name+" is "+age+" years old.");


// Boolean
var isMale = false;
console.log(isMale);

//================================ if 語句 =====================================

if (isMale) {
  console.log("You are male.");
} else {
  console.log("You are female.");
}

var isFemale="Yes";

if (isFemale == "Yes") {

  console.log("She is female");

} else {

  console.log("He is male");

}
//雙等於會自動轉換成字串做對比
if (23 == "23") {

  console.log("equal");

} else {

  console.log("not equal");

}
//三等於不會轉換
if (23 === "23") {

  console.log("equal");

} else {

  console.log("not equal");

}
//=========================== if 語句的範圍表達式=================================

var number = 20;

if (number < 20) {
  //code
} else if (number >30){
  //code
} else {
  //code
}

// and &&
if (number > 20 && number < 30){
  //code
}
// or ||
if (number < 18 || number > 65) {
  //code
}
// 相反
if (!number) {
  //code
}

//=============================== switch 語句 ==================================

var newcase = "case3"

switch (newcase) {
  case "case1":
    console.log("This is case1");
    break;

  case "case2":
    console.log("This is case2");
    break;

  case "case3":
    console.log("This is case3");
    break;

  default:
    console.log("That is other case");
}

//============================== function 語句 =================================


function myfirstfunction(){

  console.log("This is my first function.");

}

myfirstfunction();


function sum(a,b){

  var c = a + b;
  console.log(c);
}

sum(100,200);
sum(999,999);

//============================= function 返回值 ================================


function returnfunction(a){
  var b=a+5;
  return b;
}

var result = returnfunction(100);

console.log(result);

//============================= Array 數組 =====================================

var names = ['A','B','C'];
var numbers =[1,2,3,4,5];

names[names.indexOf('A')]='X';

console.log(names);
console.log(numbers[0]);

var ken =['Ken',28,'teacher'];

console.log(ken[1]);

// 在後面添加新元素
names.push('D')
console.log(names);
// 在前面添加新元素
names.unshift('Chris')
console.log(names);
// 移除前面元素
names.shift();
console.log(names);
// 移除後面元素
names.pop();
console.log(names);
// 了解位置
console.log(names.indexOf('B'));

//============================= Object 對象 ====================================

var dict ={
  name:'Ken',
  lastname:'Chen',
  age:30,
  job:'teacher'
}


 dict['name']='Jacky';
 console.log(dict['name']);

 dict.name='Ken';
 console.log(dict['name']);


 var dict2 = new Object();

 dict2.name='Jacky';
 dict2.lastname='Tsai';
 dict2.age=25;
 console.log(dict2);

//======================= fuction 與 Array、Object =============================

var dict ={
  name:'Ken',
  lastname:'Chen',
  age:30,
  job:'teacher',
  family:['A','B','C'],
  calculate:function yearOfBirth(myage){

  return 2019 - myage;


  }
}

console.log(dict.family[1]);
console.log(dict.calculate(30));

//================================= this  ======================================

var dict ={
  name:'Ken',
  lastname:'Chen',
  age:30,
  job:'teacher',
  family:['A','B','C'],
  calculate:function yearOfBirth(){

  this.yearOfBirth = 2019 - this.age;


  }
}

dict.calculate();
console.log(dict);
