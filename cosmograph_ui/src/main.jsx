import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'

const container = document.getElementById('cosmograph-root')

const graphData = {
  nodes: JSON.parse(container.dataset.nodes || "[]"),
  links: JSON.parse(container.dataset.links || "[]"),
}

ReactDOM.createRoot(container).render(<App data={graphData} />)
