import React, { Component } from "react";
// import { Link } from "react-router-dom";
import '../styles/Home.css';

export default class Home extends Component {
  state = {
    users_data: {}, // store users data
    menu_data: {}, // store menu data
    dashboard_data: {}, // data used for dashboard
    displayed_data: "users"
  }

  switchDataOnDashboard = this.switchDataOnDashboard.bind(this);
  selectMenuDataForDashboard = this.selectMenuDataForDashboard.bind(this);
  selectUsersDataForDashboard = this.selectUsersDataForDashboard.bind(this);
  // selectId = this.getId.bind(this);

  getId (id) {
    console.log(id)
  }
  getUsersData() {
    if (this.state.users_data) {       
        return Object.keys(this.state.users_data).map( (id) => { // pour tout les id
          return <tr>
            <td onClick={this.getId(id)}>{id}</td>
            <td>{this.state.users_data[id]["email"]}</td>
            <td>{this.state.users_data[id]["firstname"]}</td>
            <td>{this.state.users_data[id]["lastname"]}</td>
            <td>{this.state.users_data[id]["password"]}</td>
            <td>{this.state.users_data[id]["phone"]}</td>
            <td>{this.state.users_data[id]["type"]}</td>
          </tr>;
          // return Object.keys(this.state.users_data[id]).map( (key) => { // afficher tout les champs
          //   return <td>{this.state.users_data[id][key]}</td>;                                  
        // });
      });
    } else {
        return <p>data is not available</p>;
    }
  }

  getMenuData() {
    if (this.state.menu_data) {
        return Object.keys(this.state.menu_data).map( (id) => {
          return <tr>
            <td>{id}</td>
            <td>{this.state.menu_data[id]["name"]}</td>
            <td>{this.state.menu_data[id]["description"]}</td>
            <td>{this.state.menu_data[id]["price"]}</td>
            <td>{this.state.menu_data[id]["type"]}</td>
          </tr>;
        });
    } else {
        return <p>data is not available</p>;
    }
  }

  switchDataOnDashboard() {
    if (this.state.displayed_data==="users") {
      this.setState({
        displayed_data: "menu"
      })
    } 
    else if (this.state.displayed_data==="menu"){
      this.setState({
        displayed_data: "users"
      })
    }
    
  }

  componentDidMount(){
    // TODO : si pas connecter alors redirection vers login sinon on lance bien le dashboard (home)
    // TODO : si connecter alors charger les données menu & users

    var axios = require('axios');

    var config = {
      method: 'get',
      url: 'http://localhost:5000/users'
    };
    
    axios(config)
    .then(response => this.setState({
      users_data: response.data
    }))
    .catch(function (error) {
      console.log(error);
    });    
    
    config = {
      method: 'get',
      url: 'http://localhost:5000/menu'
    };
    
    axios(config)
    .then(response => this.setState({
      menu_data: response.data
    }))
    .catch(function (error) {
      console.log(error);
    }); 
  } 

  selectMenuDataForDashboard() {
    this.setState({
      displayed_data: "menu"
    })
  }
  

  selectUsersDataForDashboard() {
    this.setState({
      displayed_data: "users"
    })
  }
  
  // TODO : pour le dashbaord créer un tableau dynamique

  render() {    
    return (
      <div>      
        {/* style={{alignItems: "center", justifyContent: "center"}}   */}
        <div style={{textAlign: "center"}}>
          <button style={{width: "50%"}} onClick={this.selectUsersDataForDashboard}>Users</button>
          <button style={{width: "50%"}} onClick={this.selectMenuDataForDashboard}>Menu</button>
        </div>
          
        <table style={{width: "100%"}} border={2} cellPadding={5}>
          <thead>
            {
              this.state.displayed_data==="users" ?
              <tr>
                <td>id</td>
                <td>email</td>
                <td>firstname</td>
                <td>lastname</td>
                <td>password</td>
                <td>phone</td>
                <td>type</td>
              </tr> :
              <tr>
                <td>id</td>
                <td>description</td>
                <td>name</td>
                <td>price</td>
                <td>type</td>
              </tr>              
            }            
          </thead>
          <tbody>
          { 
            this.state.displayed_data==="users" ?
            this.getUsersData():
            this.getMenuData()
          }
          </tbody> 
        </table>
                
      </div>     
    );
  }
}