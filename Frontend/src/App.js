import Editor from '@monaco-editor/react'
import { useState } from 'react';
import { saveAs } from 'file-saver';
import Button from '@material-ui/core/Button';
import axios from 'axios';
import DataTable, { createTheme } from 'react-data-table-component'
import Graphviz from 'graphviz-react';

export default function App() {

  const [myValue, setMyValue] = useState('')
  const [myConsola, setMyConsola] = useState('')
  const [myErrores, setMyErrores] = useState('')
  const [mySimbolos, setMySimbolos] = useState('')
  const [myAst, setMyAst] = useState('')

  const columnas = [
    {
      name: 'IDENTIFICADOR',
      selector: 'id',
      center: true
    },{
      name: 'VALOR',
      selector: 'valor',
      center: true
    },
    {
      name: 'TIPO',
      selector: 'tipo',
      center: true
    },
    {
      name: 'ENTORNO',
      selector: 'entorno',
      center: true
    },
    {
      name: 'FILA',
      selector: 'fila',
      center: true
    },
    {
      name: 'COLUMNA',
      selector: 'columna',
      center: true
    }
  ];
  const columnasErrores = [
    {
      name: '#',
      selector: 'id',
      center: true,
    },
    {
      name: 'TIPO ERROR',
      selector: 'tipo',
      center: true,
      grow: 50
    },
    {
      name: 'DESCRIPCION',
      selector: 'descripcion',
      wrap: true,
      grow: 50
    },
    {
      name: 'FILA',
      selector: 'fila',
      center: true
    },
    {
      name: 'COLUMNA',
      selector: 'columna',
      center: true
    }
  ];
  const createFile = () => {
    const blob = new Blob([myValue], { type: 'text/plain;charset=utf-8' })
    saveAs(blob, 'Guardado.ts')
  }
  function handleEditorChange(value, event) {
    setMyValue(value)
  }
  const readFile = (e) => {
    const file = e.target.files[0];

    if (!file) return;

    const fileReader = new FileReader();
    fileReader.readAsText(file);
    fileReader.onload = () => {
      setMyValue(fileReader.result);
    }
  }
  async function postName(e) {
    try {
      var contenido = {
        codigo: myValue
      }
      console.log(contenido)
      const respuesta = await axios.post("http://localhost:5000/analizar", contenido)
      setMyConsola(respuesta.data.consola)
      setMySimbolos(respuesta.data.tablaSimbolos)
      setMyErrores(respuesta.data.tablaErrores)
      setMyAst(respuesta.data.dotAst)
    } catch (error) {
      console.log(error)
    }
  }

  async function postName2(e) {
    try {
      var contenido = {
        codigo: myValue
      }
      console.log(contenido)
      const respuesta = await axios.post("http://localhost:5000/compilar", contenido)
      setMyConsola(respuesta.data.consola)
      setMySimbolos(respuesta.data.tablaSimbolos)
      setMyErrores(respuesta.data.tablaErrores)
      setMyAst(respuesta.data.dotAst)
    } catch (error) {
      console.log(error)
    }
  }


  createTheme('custom', {
    text: {
      primary: '#268bd2',
      secondary: '#2aa198',
    },
    background: {
      default: '#002b36',
    },
    context: {
      background: '#cb4b16',
      text: '#FFFFFF',
    },
    divider: {
      default: '#073642',
    },
    action: {
      button: 'rgba(0,0,0,.54)',
      hover: 'rgba(0,0,0,.08)',
      disabled: 'rgba(0,0,0,.12)',
    },
  }, 'dark');

  function mostrarTablaSimbolos() {
    var x = document.getElementById("tbsimbolos");
    var y = document.getElementById("tbErrores");
    var z = document.getElementById("imgAst");
    x.style.display = "block";
    y.style.display = "none";
    z.style.display = "none";
  }
  function mostrarTablaErrores() {
    var x = document.getElementById("tbErrores");
    var y = document.getElementById("tbsimbolos");
    var z = document.getElementById("imgAst");
    x.style.display = "block";
    y.style.display = "none";
    z.style.display = "none";
  }
  function mostrarAst() {
    var x = document.getElementById("imgAst");
    var y = document.getElementById("tbsimbolos");
    var z = document.getElementById("tbErrores");
    x.style.display = "block";
    y.style.display = "none";
    z.style.display = "none";
  }

  return (

    <div>
      <div>
        <h1>PyTypeCraft</h1>
      </div>
      <div class="contenedor-botones">
        <input
          type="file"
          multiple={false}
          onChange={readFile}
          accept="image/*"
          style={{ display: 'none' }}
          id="contained-button-file"
        />
        <label htmlFor="contained-button-file">
          <Button variant="contained" component="span" style={{
            backgroundColor: "#6f6f6f",
            borderRadius: 10,
            width: 100,
            bottom: 3,
            fontSize: "medium",
            fontFamily: "Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif",
            margin: 10,
            color: "#000000"
          }}>
            Abrir
          </Button>
        </label>

        <button onClick={createFile}>Guardar</button>
        <button onClick={postName}>EJECUTAR</button>
        <button onClick={postName2}>COMPILAR</button>
        <button onClick={mostrarTablaSimbolos}>Simbolos</button>
        <button onClick={mostrarTablaErrores}>Errores</button>
        <button onClick={mostrarAst}>AST</button>
      </div>
      <div class="contenedor">
        <div class="izquierda">
          EDITOR
          <Editor
            height='50vh'
            theme='vs-dark'
            defaultLanguage='markdown'
            value={myValue}
            onChange={handleEditorChange}

          />
        </div>
        <div class="derecha">
          CONSOLA
          <Editor
            height='50vh'
            theme='vs-dark'
            defaultLanguage='markdown'
            value={myConsola}
          />
        </div>
      </div>
      <div class="tablaSimbolos" id='tbsimbolos'>
        <div> <h2>TABLA DE SIMBOLOS</h2></div>
        <DataTable
          columns={columnas}
          data={mySimbolos}
          theme='vs-dark'
          pagination
        />
      </div>
      <div class="tablaErrores" id='tbErrores'>
        <div> <h2>TABLA DE ERRORES</h2></div>
        <DataTable
          columns={columnasErrores}
          data={myErrores}
          theme='vs-dark'
          pagination
        />
      </div>
      <div class="imgAst" id='imgAst'>
        <div> <h2>Arbol AST</h2></div>
        < Graphviz
          dot={`digraph G {`+myAst+`
            }`}
          options={{
             zoom: true,
             width: 5000}}
        />
      </div>
    </div>
  )
}