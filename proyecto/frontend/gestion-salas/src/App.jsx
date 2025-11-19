import { useEffect, useState } from 'react'
import ucuLogo from './assets/ucuLogo.svg'
import './App.css'

function App() {
  const [salas, setSalas] = useState([])

  useEffect(() => {
    fetch("http://localhost:5000/salas")
    .then(res => res.json())
    .then(data => setSalas(data))
  }, [])


  return (
  )

} 

export default App;
