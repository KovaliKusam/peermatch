 
import React, { useState } from 'react';
 
const Chatbot = ({ apiKey, environmentUrl }) => {
    const [isOpen, setIsOpen] = useState(false);
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState('');
    const [loading, setLoading] = useState(false);
 
    const handleToggle = () => {
        setIsOpen(!isOpen);
    };
 
    const handleSend = async (e) => {
        e.preventDefault();
        if (input.trim()) {
            // Add user message to chat
            setMessages([...messages, { text: input, sender: 'user' }]);
            setInput('');
            setLoading(true);
 
            try {
                // Send message to Spark Assist API
                const url = `${environmentUrl}/v1/sparkassist/openai/deployments/gpt-4o-mini/chat/completions?api_version=2024-02-01`;
                const payload = {
                    messages: [
                        { role: "system", content: "You are a helpful assistant." },
                        { role: "user", content: input }
                    ],
                    temperature: 0.2,
                    n: 1,
                    stream: false,
                    presence_penalty: 0,
                    frequency_penalty: 0,
                    top_p: 1
                };
 
                const response = await fetch(url, {
                    method: 'POST',
                    headers: {
                        'api-key': apiKey,
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(payload)
                });
 
                const data = await response.json();
 
                // Check if the response contains the expected structure
                if (data.choices && data.choices.length > 0 && data.choices[0].message) {
                    // Add Spark Assist response to chat
                    setMessages((prevMessages) => [
                        ...prevMessages,
                        { text: data.choices[0].message.content, sender: 'bot' },
                    ]);
                } else {
                    throw new Error("Unexpected response structure");
                }
 
            } catch (error) {
                console.error("Error communicating with Spark Assist:", error);
                setMessages((prevMessages) => [
                    ...prevMessages,
                    { text: "Sorry, I couldn't get a response. Please try again.", sender: 'bot' },
                ]);
            } finally {
                setLoading(false);
            }
        }
    };
 
    return (
        <div>
            <button
                onClick={handleToggle}
                className="fixed bottom-4 right-4 bg-blue-500 text-white p-3 rounded-full shadow-lg hover:bg-blue-600 transition duration-200"
            >
                Chat
            </button>
 
            {isOpen && (
                <div className="fixed bottom-16 right-4 w-80 bg-white shadow-lg rounded-md">
                    <div className="p-4 border-b">
                        <h2 className="text-lg font-bold">Chatbot</h2>
                        <button onClick={handleToggle} className="absolute top-2 right-2 text-gray-500">
                            &times;
                        </button>
                    </div>
                    <div className="p-4 h-48 overflow-y-auto">
                        {messages.map((message, index) => (
                            <div key={index} className={`mb-2 ${message.sender === 'user' ? 'text-right' : 'text-left'}`}>
                                <span className={`inline-block px-3 py-1 rounded-full ${message.sender === 'user' ? 'bg-blue-500 text-white' : 'bg-gray-200 text-gray-800'}`}>
                                    {message.text}
                                </span>
                            </div>
                        ))}
                        {loading && <div className="text-center text-gray-500">Bot is typing...</div>}
                    </div>
                    <form onSubmit={handleSend} className="flex p-2 border-t">
                        <input
                            type="text"
                            value={input}
                            onChange={(e) => setInput(e.target.value)}
                            placeholder="Type a message..."
                            className="flex-1 border border-gray-300 rounded p-2"
                        />
                        <button type="submit" className="ml-2 bg-blue-500 text-white p-2 rounded hover:bg-blue-600 transition duration-200">
                            Send
                        </button>
                    </form>
                </div>
            )}
        </div>
    );
};
 
export default Chatbot;
 