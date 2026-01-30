import React from 'react';
import TodoItem from './TodoItem';

const TodoListView = (props) => {
    return (
        <React.Fragment>
            {props.todoList.map((todo, i) => <TodoItem key={i} todo={todo} />)}
        </React.Fragment>
    )
}

export default TodoListView;
