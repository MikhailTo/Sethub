import React, { useEffect } from 'react';
import favicon from './assets/icons/favicons/favicon.ico';
import './App.css'

const App: React.FC = () => {
  useEffect(() => {
    const link: HTMLLinkElement | null = document.querySelector("link[rel~='icon']");
    if (link) {
      link.href = favicon;
    }
  }, []);

  return (
    <div className="app-container">
      <header className="app-header">
        <h3 className="logo">Sethub</h3>
      </header>
      <main className="app-main"> 
        <h1>Main page</h1>
      </main>
    </div>
  );
};

export default App;
