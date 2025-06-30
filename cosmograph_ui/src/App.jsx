import React, { useEffect } from 'react'
import { Cosmograph } from '@cosmograph/react'

export default function App({ data }) {
  return (
    <Cosmograph
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
  )
}
