import '../styles/App.css';
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import logo from '../static/logo.png';
import Home from './Home.js';
import SignIn from './SignIn.js';
import SignUp  from './SignUp.js';

function App() {
  const headerMenuItems = [
    {href: "/", title: "Home"},
    {href: "/sign-in", title: "Sign in"},
    {href: "/sign-up", title: "Sign up"},
  ]

  return (    
    <Router>  
      <div className="App">
        <header className="App-header">        
          <nav style={{boxShadow: "0px 0px 5px 5px rgba(0, 0, 255, .2)"}}>            
            <Link to={"/"}>
              <img  src={logo} width="200px" alt="PROJ"/>
            </Link>                     
            <ul>
            {headerMenuItems.map((values, index) =>
              <li>
                <Link key={index} to={values.href}>{values.title}</Link>
              </li>                              
            )}          
            </ul>                       							
          </nav>
          <Switch>
            <Route key="0" exact path="/" component={Home} /> 
            <Route key="1" path="/sign-up" component={SignUp} />    
            <Route key="2" path="/sign-in" component={SignIn} />                 
          </Switch>      
        </header>
      </div>
    </Router>
  );
} 


export default App;