import React, { useState } from "react";
import ReactDOM from "react-dom/client";
import Title from "./Title";
import Feed from "./Feed";
import Articles from "./Articles";
import "./styles.css";
import "./main.css";

ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(
  <React.StrictMode>
    <Title />
    <div className="flex-container">
      <div className="articles">
        <Articles />
      </div>
      <div className="feed">
        <Feed />
      </div>
    </div>
  </React.StrictMode>
);
