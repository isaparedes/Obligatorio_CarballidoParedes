import { BrowserRouter, Route, Routes } from 'react-router-dom';

import Home from './Home';
import Login from './Login';
import SignUp from './SignUp';
import Reserva from './Reserva';
import Admin from './Admin';
import Metrica from './Metrica';
import ProtectedRoute from "./ProtectedRoute";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>

        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<SignUp />} />
        <Route path="/reserva" element={<Reserva />} />

        <Route path="/adminABM" element={
          <ProtectedRoute rol="admin">
            <Admin />
          </ProtectedRoute>
        } />

        <Route path="/metricaBI" element={
          <ProtectedRoute rol="admin">
            <Metrica />
          </ProtectedRoute>
        } />

      </Routes>
    </BrowserRouter>
  );
}
