import { useState } from 'react'
import reactLogo from './assets/react.svg'
import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";
import './App.css'
import UserCreateForm from './components/UserCreateForm/UserCreateForm'

function App() {

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/register" element={ <UserCreateForm /> } />
      </Routes>
    </BrowserRouter>
  )
}

export default App
