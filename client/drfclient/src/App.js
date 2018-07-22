import React, { Component } from 'react';
import axios from 'axios';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  constructor(props) {
    super(props);

    this.testSocket = new WebSocket(
      'ws://' + '127.0.0.1:8000' +
      '/ws/test/');

    this.testSocket.onOpen = function(e) {
      console.log('opened connection...')
    }

    this.testSocket.onmessage = function(e) {
        var data = JSON.parse(e.data);
        var message = data['message'];
        console.log(message);
    };

    this.testSocket.onclose = function(e) {
        console.error('Chat socket closed unexpectedly');
    };

    this.state = {name:'', colour:''};

    this.handleNameInput = this.handleNameInput.bind(this);
    this.handleColourInput = this.handleColourInput.bind(this);
    this.handleClick = this.handleClick.bind(this);
  }

  handleNameInput(event) {
    const text = event.target.value;
    this.setState({name: text});
  }

  handleColourInput(event) {
    const text = event.target.value;
    this.setState({colour: text});
  }

  handleClick() {
    const name = this.state.name;
    const colour = this.state.colour;
    axios.post('http://127.0.0.1:8000/api/animals/', {name: name, colour: colour});
  }
  
  
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to React</h1>
        </header>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>
        <div>
        Name: 
        <input type="text" value={this.state.name} onChange={this.handleNameInput}/>
        </div>
        <div>
        Colour:
        <input type="text" value={this.state.colour} onChange={this.handleColourInput}/>
        </div>
        <button onClick={this.handleClick}>Click</button>
      </div>
    );
  }
}

export default App;
