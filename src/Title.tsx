import "./Title.css";
import { appWindow } from "@tauri-apps/api/window";

function Title() {

  return (
    <div className="container">
      <body>
        <div data-tauri-drag-region className="titlebar">
          <div className="titlebar-button" id="titlebar-minimize">
            <img
              src="https://api.iconify.design/mdi:window-minimize.svg"
              alt="minimize"
              onClick={appWindow.minimize}
            />
          </div>
          <div className="titlebar-button" id="titlebar-maximize">
            <img
              src="https://api.iconify.design/mdi:window-maximize.svg"
              alt="maximize"
              onClick={appWindow.toggleMaximize}
            />
          </div>
          <div className="titlebar-button" id="titlebar-close">
            <img src="https://api.iconify.design/mdi:close.svg" alt="close" onClick={appWindow.close} />
          </div>
        </div>
      </body>
    </div>
  );
}

export default Title;
