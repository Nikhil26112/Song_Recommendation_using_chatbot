import React, { useState } from 'react';

function Chatbot() {
    const [chatHistory, setChatHistory] = useState([]);
    const [inputText, setInputText] = useState('');

    function handleSubmit(event) {
        event.preventDefault();
        setChatHistory([...chatHistory, { text: inputText, sender: 'user' }]);
        setInputText('');
    }

    return (
        <div>
            <div> <p>hello from chatbot!!!</p></div>
            {/* chat history */}
            {chatHistory.map((message, index) => (
                <div key={index}>
                    <span>{message.sender}: </span>
                    <span>{message.text}</span>
                </div>
            ))}
            {/* input field */}
            <form onSubmit={handleSubmit}>
                <input value={inputText} onChange={event => setInputText(event.target.value)} />
                <button type="submit">Send</button>
            </form>
        </div>
    );
}


export default Chatbot;
