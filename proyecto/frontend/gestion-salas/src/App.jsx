import { BrowserRouter, Route, Routes } from 'react-router-dom';
//import Home from './Home';
//import ApiRef from './ApiRef';
//import { Country } from './Country';

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/*
        <Route path="/" element={<Home />} />
        <Route path="/ref/api" element={<ApiRef />} />
        <Route path="/country/:cca3" element={<Country/>} />
        */}
      </Routes>
    </BrowserRouter>
  );
}
