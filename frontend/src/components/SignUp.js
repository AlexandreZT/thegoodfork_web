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

        fetch('http://localhost:5000/sign-up', {
            method: 'POST',
            headers:{
                "Content-Type":"application/json"
            },
            body: JSON.stringify({
                username : e.target[0].value,
                password : e.target[1].value
            }),
        }).then(response => {
            if (response === 200) {
                this.props.history.push("/sign-in");
                return
            }
        }) // .catch(err => console.log(err));  
    }
    
    render() {
        return (
            <div className="auth-wrapper">
                <div className="auth-inner">
                    <form onSubmit={this.handleSubmit}>
                        <h3>Sign Up</h3>
                        <div className="form-group">
                            <label>Username</label><br/>
                            <input type="text" className="form-control" placeholder="Enter username" />
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