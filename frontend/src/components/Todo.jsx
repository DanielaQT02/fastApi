import React, { useState, useEffect } from 'react';
import { Button, Form, Container } from 'react-bootstrap';
import axios from 'axios';
import TodoListView from './TodoListView';


function Todo() {
    const [todoList, setTodoList] = useState([{}]);
    const [title, setTitle] = useState("");
    const [desc, setDesc] = useState("");
    console.log(todoList);

    // READ ALL TODOS 
    useEffect(() => {
        axios.get('http://localhost:8000/api/todo')
            .then(res => {
                setTodoList(res.data);
            });
    });



    // POST A TODO 
    const addTodoHandler = () => {
        axios.post('http://localhost:8000/api/todo', { 'title': title, "description": desc })
            .then(res => console.log(res))

    }

    return (
        <div className="Todo">
            <br /><br />
            <Container>
                <h2 className="text-white">Task Manager</h2>
                <p className="text-white">Add a new task</p>
                <Form.Group className="mb-3" controlId="formBasicEmail">
                    <Form.Label className="text-white">Title</Form.Label>
                    <Form.Control onChange={e=> setTitle(e.target.value)} type="email" placeholder="Enter email" />
                </Form.Group>
                <Form.Group className="mb-3" controlId="exampleForm.ControlTextarea1">
                    <Form.Label className="text-white" >Description</Form.Label>
                    <Form.Control onChange={e=> setDesc(e.target.value)} as="textarea" rows={2} />
                </Form.Group>
                <Button onClick={addTodoHandler} variant="primary" type="submit">
                    Submit
                </Button>
                <br /><br />
                <TodoListView todoList={todoList} />
            </Container>
        </div>
    )
}

export default Todo;
