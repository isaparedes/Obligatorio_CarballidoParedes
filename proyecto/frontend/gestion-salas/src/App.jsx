import { BrowserRouter, Route, Routes} from 'react-router-dom';

import TitleManager from './components/TitleManager';
import Layout from './components/Layout';
import Home from './components/Home';
import Login from './components/Login';
import SignUp from './components/Signup';
import Reserva from './components/Reserva';
import ReservaSala from './components/ReservaSala';
import Admin from './components/Admin';
import Metrica from './components/Metrica';
import ProtectedRoute from './components/ProtectedRoute';

export default function App() {



  return (
    <BrowserRouter>
      <TitleManager/>
      <Routes>
        <Route element={<Layout />}>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<SignUp />} />
          <Route path="/reserva/form" element={<Reserva />} />
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
        </Route>

      </Routes>
    </BrowserRouter>
  );
}