import ucuLogo from "../assets/ucuLogo.svg";
import "./App.css"

export default function BarraBienvenida() {
    return (
        <div id="barraBienvenida">
            <h1>Salas de estudio UCU</h1>
            <img src={ucuLogo} alt="logo ucu" />
        </div>
    )
}