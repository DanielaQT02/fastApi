import axios from 'axios';
import React from 'react';
import { Alert, Button } from 'react-bootstrap';

const TodoItem = (props) => {
    const deleteTodoHandler = (title) => {
        console.log(title);
        axios.delete(`http://localhost:8000/api/todo/${title}`)
            .then(res => console.log("Deleted - ",res.data))
            .catch(err=>console.log(err))
    }
    return (
        <React.Fragment>
            <Alert variant="success">
                <Alert.Heading>{props.todo.title}</Alert.Heading>
                <p>{props.todo.description}</p>
                <hr />
                <div className="d-flex justify-content-end">
                    <Button onClick={() => deleteTodoHandler(props.todo.title)} variant="outline-danger"> Delete</Button>
                </div>
            </Alert>
        </React.Fragment>
    )
}

export default TodoItem;
