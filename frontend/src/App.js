import React, {useEffect, useState} from "react"
import Hero from "./components/Hero"
  // const [response, setResponse] = useState({
  //   res:"",
  //   emotion:""
  // })
  // useEffect(()=>{
  //   fetch("/output")
  //   .then(response => response.json()
  //   .then(data => {
  //     setResponse({
  //       res :data.res,
  //       emotion: data.emotion
  //     })
  //   }))
  // })

    export default function App() {
      return (
        <h1 className="App">
          <Hero />
        </h1>
      )
    }

