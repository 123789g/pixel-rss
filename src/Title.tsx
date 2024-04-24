import "./Title.css";
import { appWindow } from "@tauri-apps/api/window";

function Title() {

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
              src="https://api.iconify.design/mdi:window-minimize.svg"
              alt="minimize"
              onClick={minimizeWindow}
            />
          </div>
          <div className="titlebar-button" id="titlebar-maximize">
            <img
              src="https://api.iconify.design/mdi:window-maximize.svg"
              alt="maximize"
              onClick={maximizeWindow}
            />
          </div>
          <div className="titlebar-button" id="titlebar-close">
            <img src="https://api.iconify.design/mdi:close.svg" alt="close" onClick={closeWindow} />
          </div>
        </div>
      </body>
    </div>
  );
}

export default Title;
