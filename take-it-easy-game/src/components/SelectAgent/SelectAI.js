import * as React from 'react';
import Box from '@mui/material/Box';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';

export default function BasicSelect({ agent, setAgent }) {
  const handleChange = (event) => {
    setAgent(event.target.value);
  };

  return (
    <Box sx={{ minWidth: 200 }}>
      <FormControl fullWidth>
        <InputLabel id="demo-simple-select-label">Agent</InputLabel>
        <Select value={agent} label="Agent" onChange={handleChange}>
          <MenuItem value={'RL'}>Reinforcement Learning</MenuItem>
          <MenuItem value={'A-star'}>A-star</MenuItem>
          <MenuItem value={'Monte Carlo'}>Monte Carlo</MenuItem>
          <MenuItem value={'Random'}>Random</MenuItem>
        </Select>
      </FormControl>
    </Box>
  );
}
