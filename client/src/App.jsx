import React, { useState, useEffect } from 'react'
import './App.css'
import axios from 'axios';

function App() {

  const [data, setData] = useState([])

  const fetchApi = async () => {
    const response = await axios.get("http://127.0.0.1:5000/api");
    setData(response.data.users)
    console.log(response.data.users);
  }

  useEffect(() => {
    fetchApi();
  },[])



  return (
    <>
      <div>
        React - {data}
      </div>
    </>
  )
}

export default App
