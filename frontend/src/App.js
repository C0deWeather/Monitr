import logo from './logo.svg';
import './App.css';
import Login from './Components/login/Login';
import Register from './Components/register/register';
import { Route,Routes,Link } from 'react-router-dom';

function App() {
  return (
    <div>
       <nav>
        <ul>
          <li><Link to="register">Register</Link></li>
          <li><Link to="login">Login</Link></li>
        </ul>
       </nav>

       <Routes>
        <Route path='register' element={<Register/>}/>
        <Route path='login' element={<Login/>}/>
       </Routes>
    </div>
  );
}

export default App;
