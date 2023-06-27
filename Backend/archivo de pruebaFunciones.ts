
function fibonacci(n: number) {
    if (n <= 1) {
        return n;
    } else {
        return fibonacci(n - 1) + fibonacci(n-2);
    }
}

console.log(fibonacci(10));

function parametros(){
    console.log("es una funcion")
    let x = 15;
    //let x = 5;
    let y:number = (3+5);
    let str:string = "CADENA 1";

    let vari;

    console.log(vari)

    console.log(str)
    x = 10;
    console.log(x);
    x=15;
    console.log(x);
    x=21;
    console.log(x);
    x= y+ y;
    console.log(x);

    str = "esta es otra cadena";
    console.log(str)
    str = "me gusta la pizza"
    console.log(str)

    vari = "esta se tiene que repetir"

    console.log("esta es la variiable vari: " + vari)
    let q:number = 0;

    q++;
    q++;
    q++;
    q++;
    console.log(q)

    let q2 = 10;

    q2--;
    q2--;
    q2--;

    console.log(q2)
    console.log(" ")

    for(let i = 0; i < 20; i=i+1){
        if (i === 10) {
            console.log("esta es la variiable q2: "+q2);
            console.log("esta es la variiable i:" +i);
    }else {
            console.log("esta es la variiable i:" +i);
    }
    
        i++;

    }  
}

parametros()


let x = 3.14196545464;

console.log(x.toExponential(2))

function nulas(){
    if (x === null){
        console.log("es nula")
    }else {
        console.log("no es nula")

    }
}

function hola(){
    if (x === null){
        return "es nula"
    }else {
        return "no es nula"

    }
}

nulas()
console.log(hola())
function aver(){
    return;
}
console.log(aver())


interface Persona {
    nombre: string;
    edad: number;
    ciudad: string;
  }
  
  
x = 3

let otra: Persona =  {
    nombre: "Juan2",
    edad: 302,
    ciudad: "guatemala2"
};
  
let persona: Persona = {
    nombre: otra.nombre,
    edad: 30 + x,
    ciudad: "guatemala"
};
  
persona.edad = x  
persona.edad = persona.edad + x
  
otra.nombre = "este es otro nombre"
  
console.log(persona.nombre, otra.nombre, persona.edad, otra.edad)

function aver2(){
    return persona;
}

let persona2
persona2 = aver2()
persona2.ciudad = "michigan"
console.log(persona2.ciudad)