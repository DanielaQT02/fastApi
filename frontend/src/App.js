import './App.css';
import React, {Component} from 'react';
import Menu from './components/Menu'
import Todo from './components/Todo'

class App extends Component{
  render(){
    return (
      <div className="App">
        <Menu />
        <Todo />
      </div>
    );
  }
}
export default App;

