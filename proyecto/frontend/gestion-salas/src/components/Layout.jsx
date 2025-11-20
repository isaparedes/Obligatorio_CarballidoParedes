import BarraBienvenida from "./BarraBienvenida";
import { Outlet } from "react-router-dom";
import "./Layout.css"

export default function Layout() {
  return (
    <div className="layout">
      <header className="barraBienvenida">
        <BarraBienvenida />
      </header>
      <main className="contenido">
        <Outlet />
      </main>
    </div>
  );
}

