import React, { useEffect,useRef } from 'react'
import { Cosmograph,CosmographProvider } from '@cosmograph/react'

export default function App({ data }) {
  const cosmographRef = useRef(null)
  const graphRef = useRef(null);

  const playPause = () => {
        if ((cosmographRef.current)?.isSimulationRunning) {
            (cosmographRef.current)?.pause();
        } else {
            (cosmographRef.current)?.start();
        }
    }
  const fitView = () => {
        (cosmographRef.current)?.fitView();
        graphRef.current?.scrollIntoView({ behavior: 'smooth' });
    }

  return (
    <div ref={graphRef}>
    <CosmographProvider>
    <Cosmograph
      ref={cosmographRef}
      backgroundColor="transparent"
      nodes={data.nodes}
      links={data.links}
      linkArrows={false}
      nodeColor={(d) => d.colour ?? "blue"}
      nodeSize={(d) => d.size ?? 5}
      scaleNodesOnZoom={false}
      nodeLabelColor={(d) => d.colour ?? "#cccccc"}
      nodeLabelAccessor={(d) => d.label}
      simulationGravity={0.25}
      simulationRepulsion={1}
      simulationRepulsionTheta={1.15}
      simulationLinkDistance={10}
      simulationFriction={0.85}

    />
      <div className="controls">
        <button
          onClick={playPause}
          className="control-button"
        >
          Pause/Play
        </button>
        <button
          onClick={fitView}
          className="control-button"
        >
          Fit
        </button>
      </div>
    </CosmographProvider>
    </div>
  )
}
