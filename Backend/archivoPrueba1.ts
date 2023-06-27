let x = 15;
let y:number = (3+5);
let str:string = "CADENA 1";

interface Estructura {
    tipo1: number;
    tipo2: boolean;
    tipo3: any;
    tipo4: string;
}

console.log("cadena 2");
console.log(x + y);

let a:boolean = true;
let ab:string;
let ab2 = 10;
let ab3 = "5"
if (true){
    console.log("hola2");
    console.log(ab);
    console.log(ab2);
    console.log(ab3 + "cadena" + true);
    

    let x:string = "esta es la variable x";
    console.log(true + " " + x + " " + 1 );
}else{
    let xx= 1
    let xy = 2
    console.log(xx + xy)
}

while(index < t1){console.log(holamundo)} //si jala
for(let i=0; i < 4; i++){}  // si jala
for(let i:number=0; i < 4; i++){console.log("item");}     // si jala
for(let i; i < 4; i++){console.log("item");} // error en declaracion 3
for(let i=0; i < 4; i++){console.log(item.color);} // esta no lo jala por el punto  del item.colo
for(i=0; i < 4; i++){console.log(item);}// esta tampoco la jala porque no viene el let 
let ab:string; for(let i=0; i < 4; i++){console.log(ab);} // si jala
for(let i=0; i < 4; i++)
//ARRAYS
let arr=[1,2]                            ;// si jala 
let arr=[1,2,arr];                        // si jala
//Asignaciones
x = 15;                                   // si jala
prueba = 15;                              // si jala
x[0] = 3                                  // si jala
x[0][1] = 33                              // si jala

function add(i: number, j=10): number   //no jalan las funciones
{
	console.log("cadena 2");
}

interface Carro{
    placa: string;
}
interface Carro{placa: string;}