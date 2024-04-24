import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import Title from "./Title";
import Feed from "./Feed";
import "./styles.css";

ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(
  <React.StrictMode>
    <Title />
    <Feed/>
    {/* <App /> */}
  </React.StrictMode>,
);
