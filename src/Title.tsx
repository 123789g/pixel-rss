import "./Title.css";
import { appWindow } from "@tauri-apps/api/window";
import Close from "./assets/titlebar/Close.png"
import Maximize from "./assets/titlebar/Maximize.png"
import Minimize from "./assets/titlebar/Minimize.png"

function Title() {

  // Window Functions abstracted to their own functions because calling them inline onClick made them unresponsive.
  const minimizeWindow = () => {
    appWindow.minimize()
  }
  const maximizeWindow = () => {
    appWindow.toggleMaximize()
  }
  const closeWindow = () => {
    appWindow.close()
  }

  return (
    <div className="container">
      <body>
        <div data-tauri-drag-region className="titlebar">
          <div className="titlebar-button" id="titlebar-minimize">
            <img
              src={Minimize}
              alt="minimize"
              onClick={minimizeWindow}
            />
          </div>
          <div className="titlebar-button" id="titlebar-maximize">
            <img
              src={Maximize}
              alt="maximize"
              onClick={maximizeWindow}
            />
          </div>
          <div className="titlebar-button" id="titlebar-close">
            <img src={Close} alt="close" onClick={closeWindow} />
          </div>
        </div>
      </body>
    </div>
  );
}

export default Title;
