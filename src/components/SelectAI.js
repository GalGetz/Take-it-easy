import * as React from 'react';
import Box from '@mui/material/Box';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';

export default function BasicSelect() {
  const [agent, setAgent] = React.useState('');

  const handleChange = (event) => {
    setAgent(event.target.value);
  };

  return (
    <Box sx={{ minWidth: 120 }}>
      <FormControl fullWidth>
        <InputLabel id="demo-simple-select-label">Agent</InputLabel>
        <Select
          value={agent}
          label="Agent"
          onChange={handleChange}
        >
          <MenuItem value={10}>RL</MenuItem>
          <MenuItem value={20}>A-star</MenuItem>
          <MenuItem value={30}>Monte Carlo</MenuItem>
        </Select>
      </FormControl>
    </Box>
  );
}