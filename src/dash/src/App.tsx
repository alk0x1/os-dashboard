import { useState } from 'react'
import { MachineInfo } from "./components/MachineInfo";
import { ProcessesList } from "./components/ProcessesList";
import Stack from 'react-bootstrap/Stack';

export const App = () => {

  return (
    <Stack className='m-5' direction="horizontal" gap={3}>
      <ProcessesList />
      <MachineInfo />
    </Stack>
  )
}

export default App
