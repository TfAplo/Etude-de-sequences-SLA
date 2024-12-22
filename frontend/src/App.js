import React, { useEffect, useState } from "react";
import axios from "axios";

function App() {
    const [message, setMessage] = useState("");

    useEffect(() => {
        axios.get("http://127.0.0.1:8000/")
            .then((response) => {
                setMessage(response.data.message);
            })
            .catch((error) => {
                console.error("Error fetching data:", error);
            });
    }, []);

    return (
        <div>
            <h1>React + FastAPI</h1>
            <p>Backend says: {message}</p>
        </div>
    );
}

export default App;
