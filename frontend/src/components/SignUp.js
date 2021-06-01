import React, { Component } from "react";
import '../styles/form.css';

export default class SignUp extends Component {

    constructor(props) {
        super(props);
        this.state = {            
        }
    }

    handleSubmit = (e) => {
        e.preventDefault()
        // TODO : ajout warning au front
        if (e.target[0].value === "" || e.target[0].value.length < 2 || // min 2 len
            e.target[1].value === "" || e.target[1].value.length < 2 || // min 2 len
            e.target[2].value === "" || e.target[2].value.length !== 10 || !isNaN(e.target[3].value) || // isNumeric with 10 digit
            e.target[3].value === "" ||  // email format already checked
            e.target[4].value === "" || e.target[4].value.length < 8) { // len 8 mini
            alert(`
            Firstname length 2+
            Lastname length 2+
            Phone must be in valid format
            Email must be in valid format
            Password lengh 8+
            `)
        } else {                
            fetch('http://localhost:5000/create-user', { // sign-up
                method: 'POST',
                headers:{
                    "Content-Type":"application/json"
                },
                body: JSON.stringify({
                    firstname : e.target[0].value,
                    lastname : e.target[1].value,
                    phone : e.target[2].value,
                    email : e.target[3].value,
                    password : e.target[4].value
                }),
            }).then(response => {
                if (response === 200) {
                    this.props.history.push("/sign-in");
                    return
                }
            }) // .catch(err => console.log(err)); 
        }      
    }
    
    render() {
        return (
            <div className="auth-wrapper">
                <div className="auth-inner">
                    <form onSubmit={this.handleSubmit}>
                        <h3>Sign Up</h3>
                        <div className="form-group">
                            <label>Firstname</label><br/>
                            <input type="text" className="form-control" placeholder="Enter password" />
                        </div>
                        <br/>
                        <div className="form-group">
                            <label>Lastname</label><br/>
                            <input type="text" className="form-control" placeholder="Enter password" />
                        </div>
                        <br/>
                        <div className="form-group">
                            <label>Phone</label><br/>
                            <input type="text" className="form-control" placeholder="Enter password" />
                        </div>
                        <br/>
                        <div className="form-group">
                            <label>Email</label><br/>
                            <input type="email" className="form-control" placeholder="Enter password" />
                        </div>
                        <br/>
                        <div className="form-group">
                            <label>Password</label><br/>
                            <input type="password" className="form-control" placeholder="Enter password" />
                        </div>
                        <br/>
                        <button type="submit" className="btn btn-primary btn-block">Sign Up</button>
                        <p className="forgot-password text-right">
                            Already registered <a href="/sign-in">sign in?</a>
                        </p>
                    </form>
                </div>
            </div>
        );
    }
}